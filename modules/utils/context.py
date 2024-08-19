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

    def get_relevant_context(self, query):
        if query.startswith("?ms "):
            logger.info(f"Processing memory search query: {query}")
            try:
                _, top_k, similarity_threshold, *query_parts = query.split()
                top_k = int(top_k)
                similarity_threshold = float(similarity_threshold)
                actual_query = " ".join(query_parts)
                logger.info(f"Memory search parameters: top_k={top_k}, similarity_threshold={similarity_threshold}, query='{actual_query}'")
                full_prompt = self._get_context_with_memory_search(actual_query, top_k, similarity_threshold)
            except ValueError:
                logger.error("Invalid ?ms command format. Using default context.")
                full_prompt = self._get_default_context(query)
        else:
            full_prompt = self._get_default_context(query)

        logger.info(f"Full assembled context: {full_prompt[:500]}...")  # Log first 500 chars
        return full_prompt

    def _get_default_context(self, query):
        context = self.get_context_string()
        full_prompt = f"{context}\n\nHuman: {query}\nAI:"
        logger.info(f"Using default context for query: {query}")
        return full_prompt

    def _get_context_with_memory_search(self, query, top_k, similarity_threshold):
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
                logger.info(f"Retrieved Memory {memory_count + 1}: Similarity={memory['similarity']:.4f}, Prompt='{memory['prompt'][:50]}...', Response='{memory['response'][:50]}...'")
                memory_count += 1
            if memory_count >= top_k:
                break
        
        if memory_count == 0:
            logger.info("No relevant memories found above the similarity threshold.")
        
        full_prompt = f"{context}\nHuman: {query}\nAI:"
        logger.info(f"Memory search context generated for query: {query}")
        return full_prompt

    def clear(self):
        self.history.clear()

    def truncate(self, n):
        if n < len(self.history):
            self.history = deque(list(self.history)[-n:], maxlen=self.max_history)

# Create a global instance of ConversationContext
conversation_context = ConversationContext()
