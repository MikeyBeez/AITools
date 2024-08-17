from collections import deque
from .memory_search import search_memories


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

    def get_relevant_context(self, query, top_k=3):
        relevant_memories = search_memories(query, top_k)
        context = "Relevant past interactions:\n\n"
        for memory in relevant_memories:
            context += f"Human: {memory['prompt']}\nAI: {memory['response']}\n\n"
        return context.strip()

    def clear(self):
        self.history.clear()

    def truncate(self, n):
        if n < len(self.history):
            self.history = deque(list(self.history)[-n:], maxlen=self.max_history)


# Create a global instance of ConversationContext
conversation_context = ConversationContext()
