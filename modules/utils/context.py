from collections import deque


class ConversationContext:
    def __init__(self, max_history=15):
        self.history = deque(maxlen=max_history)
        self.max_history = max_history

    def add_interaction(self, prompt, response):
        self.history.append((prompt, response))

    def get_context_string(self):
        context = ""
        for prompt, response in self.history:
            context += f"Human: {prompt}\nAI: {response}\n\n"
        return context.strip()

    def clear(self):
        self.history.clear()

    def truncate(self, n):
        if n < len(self.history):
            self.history = deque(list(self.history)[-n:], maxlen=self.max_history)
# If n is greater than or equal to the current history length, no action is needed


# Create a global instance of ConversationContext
conversation_context = ConversationContext()
