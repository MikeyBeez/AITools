import requests
import json
from .mprint import WordAwareStreamPrinter
import logging

logging.basicConfig(level=logging.ERROR)

class OllamaClient:
    def __init__(self, base_url="http://localhost:11434", model="llama3.1:latest"):
        self.base_url = base_url
        self.model = model
        self.printer = WordAwareStreamPrinter(max_line_width=80)

    def process_response(self, prompt):
        url = f"{self.base_url}/api/generate"
        headers = {"Content-Type": "application/json"}
        data = {"model": self.model, "prompt": prompt}

        try:
            self.printer.start()
            with requests.post(url, headers=headers, json=data, stream=True) as response:
                if response.status_code == 200:
                    for line in response.iter_lines():
                        if line:
                            json_response = json.loads(line)
                            if "response" in json_response:
                                self.printer.add_text(json_response["response"])
                            if json_response.get("done", False):
                                break
                else:
                    print(f"Error: Received status code {response.status_code}")
        except requests.RequestException as e:
            print(f"Error connecting to Ollama: {e}")
        finally:
            self.printer.stop()
            # Removed the extra print() statement here

default_client = OllamaClient()

def process_response(prompt):
    default_client.process_response(prompt)

if __name__ == "__main__":
    process_response("Hello, world!")
