import asyncio
import sys
from pathlib import Path
from modules.utils.input_util import ai_friendly_prompt
from modules.utils.response import process_response
from modules.utils.banner import setup_console, print_welcome_banner, print_separator
from modules.utils.slash import setup_slash_commands
from modules.utils.initialize import initialize

# Add the project root to the Python path
project_root = Path(__file__).parent
sys.path.append(str(project_root))

logger, config = initialize()


async def main():
    logger.info("Starting AITools")

    console = setup_console()
    print_welcome_banner(console, config['user_name'])
    print_separator(console)

    slash_handler = setup_slash_commands(console)

    while True:
        prompt = await ai_friendly_prompt(f"{config['user_name']}> ")

        if prompt.startswith('/'):
            result = slash_handler.handle_command(prompt)
            if result == "exit":
                break
            elif result:
                continue

        logger.info(f"Processing prompt: {prompt}")
        process_response(prompt, config['model_name'])
        print_separator(console)

if __name__ == "__main__":
    asyncio.run(main())
