import logging
from .context import conversation_context
from rich.panel import Panel
from rich.table import Table
from rich.columns import Columns
from .search import DDGSearch
from .save_history import save_interaction
import config
import requests
import os
from .response import OllamaClient

logger = logging.getLogger(__name__)

class SlashCommandHandler:
    def __init__(self, console):
        self.console = console
        self.search_tool = DDGSearch()
        self.ollama_client = OllamaClient()
        self.commands = {
            "/exit": self.exit_command,
            "/e": self.exit_command,
            "/quit": self.exit_command,
            "/q": self.exit_command,
            "/help": self.help_command,
            "/h": self.help_command,
            "/clear": self.clear_command,
            "/c": self.clear_command,
            "/history": self.history_command,
            "/hi": self.history_command,
            "/search": self.search_command,
            "/s": self.search_command,
            "/truncate": self.truncate_command,
            "/tr": self.truncate_command,
            "/cm": self.change_model_command,
        }

    def handle_command(self, command):
        parts = command.split(maxsplit=1)
        cmd = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ""
        if cmd in self.commands:
            return self.commands[cmd](args)
        return False

    def exit_command(self, args):
        logger.info("Exiting AITools")
        self.console.print("Goodbye!", style="bold yellow")
        return "exit"

    def help_command(self, args):
        regular_table = Table(title="Available Commands", show_header=True, header_style="bold magenta")
        regular_table.add_column("Full Command", style="cyan", no_wrap=True)
        regular_table.add_column("Abbreviation", style="green", no_wrap=True)
        regular_table.add_column("Description", style="yellow")

        regular_table.add_row("/exit", "/e", "Exit the application")
        regular_table.add_row("/quit", "/q", "Exit the application (alias for /exit)")
        regular_table.add_row("/help", "/h", "Display this help message")
        regular_table.add_row("/clear", "/c", "Clear the conversation history")
        regular_table.add_row("/history", "/hi", "Display the conversation history")
        regular_table.add_row("/search <query>", "/s <query>", "Perform a web search")
        regular_table.add_row("/truncate <n>", "/tr <n>", "Truncate history to last <n> entries")
        regular_table.add_row("/cm", "", "Change the current Ollama model")

        regular_panel = Panel(regular_table, expand=True, border_style="bold blue")

        ms_table = Table(title="Memory Search Command", show_header=True, header_style="bold magenta")
        ms_table.add_column("Command", style="cyan", no_wrap=True)
        ms_table.add_column("Description", style="yellow")

        ms_table.add_row("?ms <n> <m> <query>", "Enable memory search for this query\n"
                         "n: number of top memories to retrieve\n"
                         "m: similarity threshold (0.0 to 1.0)\n"
                         "Example: ?ms 5 0.8 What is the capital of France?")

        ms_panel = Panel(ms_table, expand=True, border_style="bold green")

        columns = Columns([regular_panel, ms_panel], expand=True)
        self.console.print(columns)
        return True

    def clear_command(self, args):
        conversation_context.clear()
        logger.info("Conversation history cleared")
        self.console.print("Conversation history cleared.", style="bold green")
        return True

    def history_command(self, args):
        history = conversation_context.history
        count = len(history)
        if not history:
            self.console.print("No conversation history available.", style="bold yellow")
        else:
            self.console.print(f"Conversation History ({count} entries):", style="bold blue")
            for i, (prompt, response) in enumerate(history, 1):
                self.console.print(f"\n[{i}] Human: {prompt}", style="cyan")
                self.console.print(f"[{i}] AI: {response}", style="green")
        return True

    def search_command(self, query):
        if not query:
            self.console.print("Please provide a search query.", style="bold red")
            return True

        self.console.print(f"Searching for: {query}", style="bold blue")
        results = self.search_tool.run_search(query)

        search_response = ""
        if results:
            search_response += "Search Results:\n"
            for i, result in enumerate(results, 1):
                search_response += f"[{i}] {result}\n"
                self.console.print(f"[{i}] {result}", style="yellow")
        else:
            search_response += "No results found."
            self.console.print("No results found.", style="bold yellow")

        conversation_context.add_interaction(f"/search {query}", search_response.strip())
        save_interaction(f"/search {query}", search_response.strip(), config.USER_NAME, "Search")

        return True

    def truncate_command(self, args):
        if not args:
            self.console.print("Please specify the number of entries to keep.", style="bold red")
            return True
        try:
            n = int(args)
            if n < 0:
                raise ValueError
            conversation_context.truncate(n)
            self.console.print(f"Conversation history truncated to last {n} entries.", style="bold green")
        except ValueError:
            self.console.print("Invalid argument. Please provide a non-negative integer.", style="bold red")
        return True

    def get_ollama_models(self):
        try:
            response = requests.get("http://localhost:11434/api/tags")
            if response.status_code == 200:
                models = response.json().get('models', [])
                return [model['name'] for model in models]
            else:
                logger.error(f"Failed to fetch Ollama models. Status code: {response.status_code}")
                return []
        except requests.RequestException as e:
            logger.error(f"Error fetching Ollama models: {e}")
            return []

    def update_config_model(self, new_model):
        config_path = os.path.join(os.path.dirname(__file__), '..', '..', 'config.py')
        with open(config_path, 'r') as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            if line.startswith('MODEL_NAME'):
                lines[i] = f'MODEL_NAME = "{new_model}"\n'
                break

        with open(config_path, 'w') as file:
            file.writelines(lines)

        # Update the runtime configuration
        config.MODEL_NAME = new_model

    def change_model_command(self, args):
        models = self.get_ollama_models()
        if not models:
            self.console.print("No Ollama models found or unable to fetch models.", style="bold red")
            return True

        self.console.print("Available Ollama models:", style="bold blue")
        for i, model in enumerate(models, 1):
            self.console.print(f"[{i}] {model}", style="cyan")

        while True:
            choice = self.console.input("Enter the number of the model you want to use (or 'q' to quit): ")
            if choice.lower() == 'q':
                return True
            try:
                choice = int(choice)
                if 1 <= choice <= len(models):
                    new_model = models[choice - 1]
                    self.update_config_model(new_model)
                    self.ollama_client = OllamaClient()  # Reinitialize the Ollama client with the new model
                    self.console.print(f"Model changed to: {new_model}", style="bold green")
                    return True
                else:
                    self.console.print("Invalid number. Please try again.", style="bold red")
            except ValueError:
                self.console.print("Invalid input. Please enter a number or 'q'.", style="bold red")

def setup_slash_commands(console):
    return SlashCommandHandler(console)
