# AITools

## Note:  It's my hope that this architecture will allow me to keep track of all the code as well as possible.  It's important that ony core functionality exist in each module.

## Architecture Guide

AITools is designed with modularity, threading, and asynchronous operations in mind. This architecture allows for efficient, non-blocking interactions with AI models while maintaining a simple and extensible codebase.

### Key Architectural Principles

1. **Modularity**: The project is organized into small, manageable files, each with a specific purpose. This modular approach makes the codebase easy to understand, maintain, and extend.

2. **Asynchronous Input**: User input is handled asynchronously using Python's `asyncio` library and the `prompt_toolkit` package. This allows the application to remain responsive even while waiting for user input.  `prompt_toolkit` has a lot of features to help edit the prompt -- including completions.  

3. **Threaded Output**: The response from the AI model is processed and displayed in a separate thread, using the `rich` library's `Live` display. This enables real-time streaming of the AI's response without blocking the main application thread.

4. **API Abstraction**: The interaction with the Ollama API is encapsulated within the `OllamaClient` class. This abstraction makes it easy to switch to different AI models or APIs in the future by simply creating new client classes.

5. **Extensibility**: The project's structure is designed to be easily extensible. New features can be added by creating new modules within the existing directory structure.

6. **Context Management**: The conversation history is managed separately, allowing for context-aware interactions with the AI model without complicating the main logic.

### Current Implementation

- `main.py`: The entry point of the application. It runs an asynchronous event loop that handles user input and initiates AI responses.
- `modules/utils/input_util.py`: Contains the asynchronous input handling logic.
- `modules/utils/response.py`: Manages the threaded interaction with the AI model and handles response streaming.
- `modules/utils/mprint.py`: Implements the `WordAwareStreamPrinter` class for handling threaded, formatted console output. (Note: This file is no longer actively used as we've switched to the `rich` library for output, but it's kept for reference and potential future use.)
- `modules/utils/context.py`: Manages the conversation history using a FIFO queue, providing context for AI responses.

### Context Management and Conversation Flow

The context management system is a key feature of AITools, allowing for more coherent and context-aware conversations with the AI model. Here's how it works:

1. **Context Storage**:
   - The `ConversationContext` class in `context.py` maintains a FIFO queue (implemented using `collections.deque`) of the last 15 interactions.
   - Each interaction is stored as a tuple of (prompt, response).

2. **Adding Context**:
   - After each successful interaction, the prompt and the AI's response are added to the context queue in the `OllamaClient.process_response` method.
   - If the queue is full, the oldest interaction is automatically removed to make room for the new one.

3. **Using Context in Prompts**:
   - Before sending a new prompt to the AI model, the `OllamaClient.process_response` method retrieves the current context.
   - The context is prepended to the new prompt, formatted as a conversation history.
   - This allows the AI model to consider previous interactions when generating its response.

4. **Context Clearing**:
   - Users can type "clear history" as a prompt to reset the conversation context.
   - This is handled in the main loop, calling the `ConversationContext.clear()` method.

5. **Flow of a Conversation**:
   a. User enters a prompt.
   b. The prompt is combined with the conversation history.
   c. The combined prompt is sent to the AI model.
   d. The AI's response is received and displayed.
   e. The new interaction (prompt + response) is added to the context queue.
   f. The process repeats for the next user prompt.

This context management system allows the AI to maintain a sense of conversation flow, refer back to previous information, and provide more coherent and contextually relevant responses.

### Future Extensibility

The current architecture provides a solid foundation for adding more features and functionality:

1. **Additional AI Models**: New AI model integrations can be added by creating new client classes similar to `OllamaClient`.

2. **Enhanced Input Processing**: The `input_util.py` module can be expanded to include more sophisticated input handling, such as command parsing or context management.

3. **Output Formatting**: The response handling in `response.py` can be extended to support different output formats or to process the AI's response before displaying it.

4. **Agents and Models**: The `agents/` and `models/` directories are prepared for future implementations of more complex AI agents and custom language models.

5. **Data Handling**: The `data/` directory and corresponding module can be used to implement data processing, storage, or caching mechanisms as the project grows.

6. **Plugin System**: A plugin architecture could be implemented to allow for easy addition of new commands or features without modifying the core codebase.

As we continue to develop AITools, we will adhere to this modular, threaded, and asynchronous approach. New features will be implemented in small, manageable files that integrate seamlessly with the existing architecture. This approach ensures that the project remains easy to understand and maintain, even as it grows in complexity and capability.

