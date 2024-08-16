from collections import deque

class ConversationContext:
    def __init__(self, max_history=15):
        self.history = deque(maxlen=max_history)

    def add_interaction(self, prompt, response):
        self.history.append((prompt, response))

    def get_context_string(self):
        context = ""
        for prompt, response in self.history:
            context += f"Human: {prompt}\nAI: {response}\n\n"
        return context.strip()

    def clear(self):
        self.history.clear()

# Create a global instance of ConversationContext
conversation_context = ConversationContext()
