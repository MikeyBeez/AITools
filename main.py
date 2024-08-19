import asyncio
import sys
# import os
from pathlib import Path
import logging
from modules.utils.input_util import ai_friendly_prompt
from modules.utils.response import process_response
from modules.utils.banner import setup_console, print_welcome_banner, print_separator
from modules.utils.slash import setup_slash_commands
from modules.utils.initialize import initialize

# Add the project root to the Python path
project_root = Path(__file__).parent
sys.path.append(str(project_root))


def setup_logging():
    project_root = Path(__file__).parent
    log_dir = project_root / "logs"
    log_dir.mkdir(exist_ok=True)
    log_file = log_dir / "aitools.log"

    # Remove any existing handlers to avoid duplication
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    # Create a file handler for all log levels
    file_handler = logging.FileHandler(log_file, mode='w', encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)

    # Create a formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Get the root logger and add the handler
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    root_logger.addHandler(file_handler)

    # Suppress INFO messages from specific modules
    logging.getLogger('httpcore').setLevel(logging.WARNING)
    logging.getLogger('httpx').setLevel(logging.WARNING)

    # print(f"Log file is located at: {log_file}")


# Call logging setup
setup_logging()

# Initialize logger and config
logger, config = initialize()


async def main():
    logger.info("Starting AITools")

    console = setup_console()
    print_welcome_banner(console, config['user_name'])
    print_separator(console)

    slash_handler = setup_slash_commands(console)

    while True:
        prompt = await ai_friendly_prompt(f"{config['user_name']}> ")

        if prompt is None:
            logger.info("Exiting AITools due to user interrupt")
            break

        if prompt.startswith('/'):
            result = slash_handler.handle_command(prompt)
            if result == "exit":
                break
            elif result:
                continue

        logger.info(f"Processing prompt: {prompt}")
        response = process_response(prompt, config['model_name'], config['user_name'])
        print(response)  # Only print the LLM's response
        print_separator(console)

    logger.info("AITools session ended")

if __name__ == "__main__":
    asyncio.run(main())
