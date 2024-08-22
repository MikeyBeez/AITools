import sys
import logging
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.spinner import Spinner
from rich.live import Live
from modules.utils.response import process_response
from modules.utils.mprint import print_user_prompt, print_agent_response, stop_printer
from modules.utils.context import conversation_context
from modules.utils.slash import setup_slash_commands
import config
import time

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def display_welcome_message():
    console = Console()
    welcome_text = Text()
    welcome_text.append("Your Intelligent Conversational Companion\n\n", style="bold cyan")
    welcome_text.append(f"Welcome, {config.USER_NAME}!\n", style="green")
    welcome_text.append("Enter /help to get help.", style="yellow")
    
    panel = Panel(welcome_text, expand=False, border_style="bold blue", title="OTTO", subtitle="AI Assistant")
    console.print(panel)

def show_thinking_indicator(console):
    print("Otto is thinking")

def main():
    display_welcome_message()
    console = Console()
    slash_handler = setup_slash_commands(console)

    while True:
        try:
            print_user_prompt(config.USER_NAME)
            user_input = console.input("[yellow]")  # Set input color to yellow

            if user_input.lower().startswith('/'):
                result = slash_handler.handle_command(user_input)
                if result == "exit":
                    break
                elif result:
                    continue

            show_thinking_indicator(console)
            console.print("\nOtto> ", end="", style="bold cyan")
            response = process_response(user_input, config.MODEL_NAME, config.USER_NAME)
            console.print()  # Add a newline after the response
            
            if response.lower() in ["goodbye!", "exit", "quit"]:
                print_agent_response("Goodbye! Have a great day!")
                break

        except KeyboardInterrupt:
            print("\nInterrupted by user. Exiting...")
            break
        except Exception as e:
            logger.error(f"An error occurred: {e}", exc_info=True)
            print_agent_response(f"An error occurred: {e}")

    stop_printer()
    print("\nThank you for using OTTO. Goodbye!")

if __name__ == "__main__":
    main()
