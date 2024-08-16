# AITools

AITools is a Python project that provides utilities and tools for working with AI agents.

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
│       └── input_util.py
└── tests/
    └── input_util_test.py
```

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

## Running the Application

To run the main application:

```
python main.py
```

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

## Features

- `input_util.py`: Provides an AI-friendly prompt function that supports asynchronous input and auto-completion.

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

