import unittest
from unittest.mock import patch, MagicMock
import asyncio
import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules.utils.input_util import ai_friendly_prompt
from prompt_toolkit.completion import WordCompleter

class TestAiFriendlyPrompt(unittest.TestCase):
    def setUp(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)

    def tearDown(self):
        self.loop.close()

    @patch('modules.utils.input_util.PromptSession')
    def test_ai_friendly_prompt_normal_input(self, mock_prompt_session):
        # Set up the mock
        mock_session = MagicMock()
        mock_session.prompt_async.return_value = asyncio.Future()
        mock_session.prompt_async.return_value.set_result("test input")
        mock_prompt_session.return_value = mock_session

        # Run the test
        result = self.loop.run_until_complete(ai_friendly_prompt())
        
        # Assert the result
        self.assertEqual(result, "test input")
        mock_session.prompt_async.assert_called_once_with('> ', completer=None)

    @patch('modules.utils.input_util.PromptSession')
    def test_ai_friendly_prompt_with_completions(self, mock_prompt_session):
        # Set up the mock
        mock_session = MagicMock()
        mock_session.prompt_async.return_value = asyncio.Future()
        mock_session.prompt_async.return_value.set_result("test input")
        mock_prompt_session.return_value = mock_session

        # Run the test
        completions = ['help', 'status', 'exit']
        result = self.loop.run_until_complete(ai_friendly_prompt('Agent> ', completions))
        
        # Assert the result
        self.assertEqual(result, "test input")
        mock_session.prompt_async.assert_called_once()
        args, kwargs = mock_session.prompt_async.call_args
        self.assertEqual(args[0], 'Agent> ')
        self.assertIsInstance(kwargs['completer'], WordCompleter)

    @patch('modules.utils.input_util.PromptSession')
    def test_ai_friendly_prompt_keyboard_interrupt(self, mock_prompt_session):
        # Set up the mock to raise KeyboardInterrupt
        mock_session = MagicMock()
        mock_session.prompt_async.side_effect = KeyboardInterrupt()
        mock_prompt_session.return_value = mock_session

        # Run the test
        result = self.loop.run_until_complete(ai_friendly_prompt())
        
        # Assert the result
        self.assertIsNone(result)

    @patch('modules.utils.input_util.PromptSession')
    def test_ai_friendly_prompt_eof_error(self, mock_prompt_session):
        # Set up the mock to raise EOFError
        mock_session = MagicMock()
        mock_session.prompt_async.side_effect = EOFError()
        mock_prompt_session.return_value = mock_session

        # Run the test
        result = self.loop.run_until_complete(ai_friendly_prompt())
        
        # Assert the result
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
