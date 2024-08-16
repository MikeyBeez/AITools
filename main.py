import asyncio
from modules.utils.input_util import ai_friendly_prompt
from modules.utils.response import process_response
from modules.utils.context import conversation_context
from pathlib import Path
import sys

# Add the project root to the Python path
project_root = Path(__file__).parent
sys.path.append(str(project_root))

async def main():
    while True:
        prompt = await ai_friendly_prompt("Enter your prompt (or 'exit' to quit): ")
        if prompt.lower() == "exit":
            break
        if prompt.lower() == "clear history":
            conversation_context.clear()
            print("Conversation history cleared.")
            continue
        process_response(prompt)
        print()  # Add a newline after each response

if __name__ == "__main__":
    asyncio.run(main())
