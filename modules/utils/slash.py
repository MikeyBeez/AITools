import logging
from .context import conversation_context

logger = logging.getLogger(__name__)

class SlashCommandHandler:
    def __init__(self, console):
        self.console = console
        self.commands = {
            "/exit": self.exit_command,
            "/help": self.help_command,
            "/clear": self.clear_command,
        }

    def handle_command(self, command):
        cmd = command.split()[0].lower()
        if cmd in self.commands:
            return self.commands[cmd](command)
        return False

    def exit_command(self, command):
        logger.info("Exiting AITools")
        self.console.print("Goodbye!", style="bold yellow")
        return "exit"

    def help_command(self, command):
        help_text = """
        Available commands:
        /exit - Exit the application
        /help - Display this help message
        /clear - Clear the conversation history
        """
        self.console.print(help_text, style="bold green")
        return True

    def clear_command(self, command):
        conversation_context.clear()
        logger.info("Conversation history cleared")
        self.console.print("Conversation history cleared.", style="bold green")
        return True

def setup_slash_commands(console):
    return SlashCommandHandler(console)
