import requests
import json
from rich.live import Live
from rich.console import Console
from rich.text import Text
import logging
import sys
from .context import conversation_context
from .save_history import save_interaction  # Add this import

logging.basicConfig(level=logging.ERROR)


class OllamaClient:
    def __init__(self, base_url="http://localhost:11434"):
        """
        Initialize the OllamaClient.

        Args:
            base_url (str): The base URL for the Ollama API.
        """
        self.base_url = base_url
        self.console = Console()

    def process_response(self, prompt, model, username):
        # Add username parameter
        """
        Process a prompt and generate a response using the Ollama API.

        Args:
            prompt (str): The user's input prompt.
            model (str): The name of the model to use.
            username (str): The username of the current user.
        """
        url = f"{self.base_url}/api/generate"
        headers = {"Content-Type": "application/json"}

        context = conversation_context.get_context_string()
        full_prompt = f"{context}\nHuman: {prompt}\nAI:"

        data = {"model": model, "prompt": full_prompt}

        try:
            with Live(console=self.console, refresh_per_second=4) as live:
                with requests.post(url, headers=headers, json=data, stream=True) as response:
                    if response.status_code == 200:
                        full_response = ""
                        for line in response.iter_lines():
                            if line:
                                json_response = json.loads(line)
                                if "response" in json_response:
                                    full_response += json_response["response"]
                                    live.update(Text(full_response))
                                if json_response.get("done", False):
                                    break
                        conversation_context.add_interaction(prompt, full_response.strip())

                        # Save the interaction to a JSON file
                        save_interaction(prompt, full_response.strip(), username, model)
                    else:
                        self.console.print(f"Error: Received status code {response.status_code}")
        except requests.RequestException as e:
            self.console.print(f"Error connecting to Ollama: {e}")


# Create a default client instance
default_client = OllamaClient()


def process_response(prompt, model, username):  # Add username parameter
    """
    Process a response using the default Ollama client.

    Args:
        prompt (str): The user's input prompt.
        model (str): The name of the model to use.
        username (str): The username of the current user.
    """
    default_client.process_response(prompt, model, username)


if __name__ == "__main__":
    default_model = "llama2:latest"
    if len(sys.argv) > 1:
        model = sys.argv[1]
    else:
        model = default_model

    print(f"Testing with model: {model}")
    process_response("Hello, world!", model, "TestUser")  # Add a test username
