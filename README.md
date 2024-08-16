# AITools

This is a new project that isn't released yet -- so don't expect too much.

AITools is a Python project that provides utilities and tools for working with AI agents, specifically using the Ollama API. It features a clean, easy-to-understand structure and uses modern Python libraries for efficient console-based interactions.

## Project Structure

```
AITools/
├── README.md
├── data/
├── main.py
├── modules/
│   ├── __init__.py
│   ├── agents/
│   │   └── __init__.py
│   ├── data/
│   │   └── __init__.py
│   ├── models/
│   │   └── __init__.py
│   └── utils/
│       ├── __init__.py
│       ├── input_util.py
│       ├── response.py
│       ├── mprint.py
│       └── context.py
└── tests/
    └── input_util_test.py
```

## Features

- Asynchronous input handling with auto-completion support
- Streaming responses from AI models
- Clean and editable console cwinputoutput using the `prompt_tools` library
- Clean and readable console output using the `rich` library
- Easy-to-extend framework for AI interactions
- `input_util.py`: Provides an AI-friendly prompt function that supports asynchronous input and auto-completion
- Conversation history management with a FIFO queue for context-aware responses
- Logging system that writes to both console and file

## Architecture Guide

AITools is designed with modularity, threading, and asynchronous operations in mind. This architecture allows for efficient, non-blocking interactions with AI models while maintaining a simple and extensible codebase.  There;s an architectural guide in the documents directory.

### Key Architectural Principles

1. **Modularity**: The project is organized into small, manageable files, each with a specific purpose. This modular approach makes the codebase easy to understand, maintain, and extend.

2. **Asynchronous Input**: User input is handled asynchronously using Python's `asyncio` library. This allows the application to remain responsive even while waiting for user input.

3. **Threaded Output**: The response from the AI model is processed and displayed in a separate thread, using the `rich` library's `Live` display. This enables real-time streaming of the AI's response without blocking the main application thread.

4. **API Abstraction**: The interaction with the Ollama API is encapsulated within the `OllamaClient` class. This abstraction makes it easy to switch to different AI models or APIs in the future by simply creating new client classes.

5. **Extensibility**: The project's structure is designed to be easily extensible. New features can be added by creating new modules within the existing directory structure.

### Current Implementation

- `main.py`: The entry point of the application. It runs an asynchronous event loop that handles user input and initiates AI responses.
- `modules/utils/input_util.py`: Contains the asynchronous input handling logic and uses the prompt_tools library.
- `modules/utils/response.py`: Manages the threaded interaction with the AI model and handles response streaming.
- `modules/utils/mprint.py`: Implements the `WordAwareStreamPrinter` class for handling threaded, formatted console output. (Note: This file is no longer actively used as we've switched to the `rich` library for output, but it's kept for reference and potential future use.)
- `modules/utils/context.py`: Manages the conversation history using a FIFO queue, providing context for AI responses.

### Conversation History

The project includes a conversation history feature:
- The last 15 prompts and responses are stored in a FIFO queue.
- This history is used to provide context for each new prompt sent to the AI model.
- Users can clear the conversation history by typing "clear history" as a prompt.

### Future Extensibility

The current architecture provides a solid foundation for adding more features and functionality:

1. **Additional AI Models**: New AI model integrations can be added by creating new client classes similar to `OllamaClient`.

2. **Enhanced Input Processing**: The `input_util.py` module can be expanded to include more sophisticated input handling, such as command parsing or context management.

3. **Output Formatting**: The response handling in `response.py` can be extended to support different output formats or to process the AI's response before displaying it.

4. **Agents and Models**: The `agents/` and `models/` directories are prepared for future implementations of more complex AI agents and custom language models.

5. **Data Handling**: The `data/` directory and corresponding module can be used to implement data processing, storage, or caching mechanisms as the project grows.

6. **Plugin System**: A plugin architecture could be implemented to allow for easy addition of new commands or features without modifying the core codebase.

As we continue to develop AITools, we will adhere to this modular, threaded, and asynchronous approach. New features will be implemented in small, manageable files that integrate seamlessly with the existing architecture. This approach ensures that the project remains easy to understand and maintain, even as it grows in complexity and capability.

### Logging System

AITools implements a logging system that writes log messages to both the console and a file:

- Log files are stored in the `logs` directory at the project root.
- The main log file is named `aitools.log`.
- Logging is set up in `main.py` and uses Python's built-in `logging` module.
- Log messages include timestamps, logger name, log level, and the log message.
- The current logging level is set to INFO, which captures all informational messages, warnings, and errors.

This logging system allows for easier debugging and monitoring of the application's behavior, especially when running in production or when diagnosing issues reported by users.

## Setup

1. Clone the repository:

   ```
   git clone https://github.com/MikeyBeez/AITools.git
   cd AITools
   ```

2. Create a conda environment:

   ```
   conda create --name aitools python=3.12
   conda activate aitools
   ```

3. Install the required dependencies:

   ```
   conda install --file requirements.txt
   ```

   Note: If some packages are not available via conda, you may need to use pip:

   ```
   pip install -r requirements.txt
   ```

## Usage

To run the main application:

```
python main.py
```

This will start an interactive session where you can enter prompts and receive responses from the AI model. You can use the "clear history" command to reset the conversation context.

## Running Tests

To run all tests:

```
python -m unittest discover tests
```

To run a specific test file:

```
python -m unittest tests.input_util_test
```

Or, if you're in the `tests` directory:

```
python input_util_test.py
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Contact

MikeyBeez

Project Link: [https://github.com/MikeyBeez/AITools](https://github.com/MikeyBeez/AITools)
