import requests
import json
import logging
import sys
from .context import conversation_context
from .save_history import save_interaction

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class OllamaClient:
    def __init__(self, base_url="http://localhost:11434"):
        self.base_url = base_url
        logger.info(f"OllamaClient initialized with base_url: {base_url}")

    def process_response(self, prompt, model, username):
        logger.info(f"Processing response for user: {username}, model: {model}")
        url = f"{self.base_url}/api/generate"
        headers = {"Content-Type": "application/json"}

        full_prompt = conversation_context.get_relevant_context(prompt)
        
        data = {"model": model, "prompt": full_prompt}

        try:
            with requests.post(url, headers=headers, json=data, stream=True) as response:
                if response.status_code == 200:
                    full_response = ""
                    for line in response.iter_lines():
                        if line:
                            json_response = json.loads(line)
                            if "response" in json_response:
                                full_response += json_response["response"]
                            if json_response.get("done", False):
                                break
                    conversation_context.add_interaction(prompt, full_response.strip())
                    save_interaction(prompt, full_response.strip(), username, model)
                    logger.info(f"Response generated and saved for prompt: {prompt[:50]}...")
                    return full_response.strip()
                else:
                    error_msg = f"Error: Received status code {response.status_code}"
                    logger.error(error_msg)
                    return error_msg
        except requests.RequestException as e:
            error_msg = f"Error connecting to Ollama: {e}"
            logger.error(error_msg)
            return error_msg

# Create a default client instance
default_client = OllamaClient()

def process_response(prompt, model, username):
    logger.info(f"Processing response: prompt='{prompt[:50]}...', model={model}, username={username}")
    return default_client.process_response(prompt, model, username)

if __name__ == "__main__":
    default_model = "llama2:latest"
    if len(sys.argv) > 1:
        model = sys.argv[1]
    else:
        model = default_model

    logger.info(f"Testing with model: {model}")
    response = process_response("Hello, world!", model, "TestUser")
    print(response)
