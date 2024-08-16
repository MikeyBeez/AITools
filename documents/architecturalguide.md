# AITools

## Architecture Guide

AITools is designed with modularity, threading, and asynchronous operations in mind. This architecture allows for efficient, non-blocking interactions with AI models while maintaining a simple and extensible codebase.

### Key Architectural Principles

1. **Modularity**: The project is organized into small, manageable files, each with a specific purpose. This modular approach makes the codebase easy to understand, maintain, and extend.

2. **Asynchronous Input**: User input is handled asynchronously using Python's `asyncio` library. This allows the application to remain responsive even while waiting for user input.

3. **Threaded Output**: The response from the AI model is processed and displayed in a separate thread, using the `rich` library's `Live` display. This enables real-time streaming of the AI's response without blocking the main application thread.

4. **API Abstraction**: The interaction with the Ollama API is encapsulated within the `OllamaClient` class. This abstraction makes it easy to switch to different AI models or APIs in the future by simply creating new client classes.

5. **Extensibility**: The project's structure is designed to be easily extensible. New features can be added by creating new modules within the existing directory structure.

    ### Current Implementation

- `main.py`: The entry point of the application. It runs an asynchronous event loop that handles user input and initiates AI responses.
- `modules/utils/input_util.py`: Contains the asynchronous input handling logic.
- `modules/utils/response.py`: Manages the threaded interaction with the AI model and handles response streaming.
- `modules/utils/mprint.py`: Implements the `WordAwareStreamPrinter` class for handling threaded, formatted console output. (Note: This file is no longer actively used as we've switched to the `rich` library for output, but it's kept for reference and potential future use.)

### Future Extensibility

The current architecture provides a solid foundation for adding more features and functionality:

1. **Additional AI Models**: New AI model integrations can be added by creating new client classes similar to `OllamaClient`.

2. **Enhanced Input Processing**: The `input_util.py` module can be expanded to include more sophisticated input handling, such as command parsing or context management.

3. **Output Formatting**: The response handling in `response.py` can be extended to support different output formats or to process the AI's response before displaying it.

4. **Agents and Models**: The `agents/` and `models/` directories are prepared for future implementations of more complex AI agents and custom language models.

5. **Data Handling**: The `data/` directory and corresponding module can be used to implement data processing, storage, or caching mechanisms as the project grows.

6. **Plugin System**: A plugin architecture could be implemented to allow for easy addition of new commands or features without modifying the core codebase.

As we continue to develop AITools, we will adhere to this modular, threaded, and asynchronous approach. New features will be implemented in small, manageable files that integrate seamlessly with the existing architecture. This approach ensures that the project remains easy to understand and maintain, even as it grows in complexity and capability.

