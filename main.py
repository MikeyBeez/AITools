import asyncio
import logging
from pathlib import Path
import sys
from modules.utils.input_util import ai_friendly_prompt
from modules.utils.response import process_response
from modules.utils.context import conversation_context

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
    while True:
        prompt = await ai_friendly_prompt("Enter your prompt (or 'exit' to quit): ")
        if prompt.lower() == "exit":
            logger.info("Exiting AITools")
            break
        if prompt.lower() == "clear history":
            conversation_context.clear()
            logger.info("Conversation history cleared")
            print("Conversation history cleared.")
            continue
        logger.info(f"Processing prompt: {prompt}")
        process_response(prompt)
        print()  # Add a newline after each response

if __name__ == "__main__":
    asyncio.run(main())
