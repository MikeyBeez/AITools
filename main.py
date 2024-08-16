import asyncio
from modules.utils.input_util import ai_friendly_prompt
from modules.utils.response import process_response
from pathlib import Path
import sys
import logging

# Set logging level to ERROR to suppress debug messages
logging.basicConfig(level=logging.ERROR)

# Add the project root to the Python path
project_root = Path(__file__).parent
sys.path.append(str(project_root))

async def main():
    while True:
        prompt = await ai_friendly_prompt("Enter your prompt (or 'exit' to quit): ")
        if prompt.lower() == "exit":
            break
        process_response(prompt)

if __name__ == "__main__":
    asyncio.run(main())
