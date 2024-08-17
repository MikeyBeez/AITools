import logging
from .context import conversation_context
from rich.panel import Panel
from rich.table import Table
from .search import DDGSearch
from .save_history import save_interaction
import config  # Import the config file directly

logger = logging.getLogger(__name__)


class SlashCommandHandler:
    def __init__(self, console):
        self.console = console
        self.search_tool = DDGSearch()
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
        table = Table(title="Available Commands", show_header=True, header_style="bold magenta")
        table.add_column("Full Command", style="cyan", no_wrap=True)
        table.add_column("Abbreviation", style="green", no_wrap=True)
        table.add_column("Description", style="yellow")

        table.add_row("/exit", "/e", "Exit the application")
        table.add_row("/quit", "/q", "Exit the application (alias for /exit)")
        table.add_row("/help", "/h", "Display this help message")
        table.add_row("/clear", "/c", "Clear the conversation history")
        table.add_row("/history", "/hi", "Display the conversation history")
        table.add_row("/search <query>", "/s <query>", "Perform a web search")

        panel = Panel(table, expand=False, border_style="bold blue")
        self.console.print(panel)
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

        # Add search command and results to conversation history
        conversation_context.add_interaction(f"/search {query}", search_response.strip())

        # Save the search interaction to a JSON file
        save_interaction(f"/search {query}", search_response.strip(), config.USER_NAME, "Search")

        return True


def setup_slash_commands(console):
    return SlashCommandHandler(console)
