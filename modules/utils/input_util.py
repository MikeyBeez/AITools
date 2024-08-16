from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
import asyncio


async def ai_friendly_prompt(prompt="> ", completions=None):
    session = PromptSession()

    if completions:
        completer = WordCompleter(completions)
    else:
        completer = None

    try:
        result = await session.prompt_async(prompt, completer=completer)
        return result
    except (KeyboardInterrupt, EOFError):
        return None


# Example usage
async def main():
    completions = ["help", "status", "exit"]
    result = await ai_friendly_prompt("Agent> ", completions)
    print(f"Received: {result}")


if __name__ == "__main__":
    asyncio.run(main())
