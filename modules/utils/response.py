import requests
import json
from rich.live import Live
from rich.console import Console
from rich.text import Text
import logging
from .context import conversation_context

logging.basicConfig(level=logging.ERROR)

class OllamaClient:
    def __init__(self, base_url="http://localhost:11434", model="llama3.1:latest"):
        self.base_url = base_url
        self.model = model
        self.console = Console()

    def process_response(self, prompt):
        url = f"{self.base_url}/api/generate"
        headers = {"Content-Type": "application/json"}
        
        # Include conversation history in the prompt
        context = conversation_context.get_context_string()
        full_prompt = f"{context}\nHuman: {prompt}\nAI:"
        
        data = {"model": self.model, "prompt": full_prompt}

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
                        # Add the interaction to the conversation context
                        conversation_context.add_interaction(prompt, full_response.strip())
                    else:
                        self.console.print(f"Error: Received status code {response.status_code}")
        except requests.RequestException as e:
            self.console.print(f"Error connecting to Ollama: {e}")

default_client = OllamaClient()

def process_response(prompt):
    default_client.process_response(prompt)

if __name__ == "__main__":
    process_response("Hello, world!")
