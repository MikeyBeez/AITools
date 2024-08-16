import asyncio
import logging
from pathlib import Path
import sys
from modules.utils.input_util import ai_friendly_prompt
from modules.utils.response import process_response
from modules.utils.banner import setup_console, print_welcome_banner, print_separator
from modules.utils.slash import setup_slash_commands

# Add the project root to the Python path
project_root = Path(__file__).parent
sys.path.append(str(project_root))

# Set up logging
log_dir = project_root / "logs"
log_dir.mkdir(exist_ok=True)
log_file = log_dir / "aitools.log"

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


async def main():
    logger.info("Starting AITools")

    console = setup_console()
    print_welcome_banner(console)
    print_separator(console)

    slash_handler = setup_slash_commands(console)

    while True:
        prompt = await ai_friendly_prompt("Enter your prompt (or '/help' for commands): ")

        if prompt.startswith('/'):
            result = slash_handler.handle_command(prompt)
            if result == "exit":
                break
            elif result:
                continue

        logger.info(f"Processing prompt: {prompt}")
        process_response(prompt)
        print_separator(console)

if __name__ == "__main__":
    asyncio.run(main())
