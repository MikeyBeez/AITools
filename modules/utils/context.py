import logging
from collections import deque
from .memory_search import search_memories

logger = logging.getLogger(__name__)

class ConversationContext:
    def __init__(self, max_history=15):
        self.history = deque(maxlen=max_history)
        self.max_history = max_history

    def add_interaction(self, prompt, response):
        self.history.append((prompt, response))

    def get_context_string(self):
        context = "Chat History:\n"
        for prompt, response in self.history:
            context += f"Human: {prompt}\nAI: {response}\n\n"
        return context.strip()

    def get_relevant_context(self, query, top_k=5, similarity_threshold=0.80):
        relevant_memories = search_memories(query, top_k)
        
        context = f"Current Query: {query}\n\n"
        context += self.get_context_string() + "\n\n"
        
        context += "Relevant Memories:\n"
        memory_count = 0
        for memory in relevant_memories:
            if memory['similarity'] >= similarity_threshold and memory_count < top_k:
                context += f"Memory {memory_count + 1} (Similarity: {memory['similarity']:.4f}):\n"
                context += f"Human: {memory['prompt']}\n"
                context += f"AI: {memory['response']}\n\n"
                memory_count += 1
            if memory_count >= top_k:
                break
        
        full_prompt = f"{context}\nHuman: {query}\nAI:"
        logger.info(f"Full context being sent to LLM:\n{full_prompt}")
        return full_prompt

    def clear(self):
        self.history.clear()

    def truncate(self, n):
        if n < len(self.history):
            self.history = deque(list(self.history)[-n:], maxlen=self.max_history)

# Create a global instance of ConversationContext
conversation_context = ConversationContext()
