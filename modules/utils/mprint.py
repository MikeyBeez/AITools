import queue
import threading
import logging
from rich.console import Console
from rich.text import Text

logging.basicConfig(level=logging.ERROR)

class WordAwareStreamPrinter:
    def __init__(self, max_line_width=80):
        self.queue = queue.Queue()
        self.max_line_width = max_line_width
        self.stop_event = threading.Event()
        self.consumer_thread = None
        self.buffer = ""
        self.current_line = ""
        self.console = Console()

    def start(self):
        if self.consumer_thread is None or not self.consumer_thread.is_alive():
            self.stop_event.clear()
            self.consumer_thread = threading.Thread(target=self._consumer)
            self.consumer_thread.start()

    def add_text(self, text, style="yellow"):
        for char in text:
            self.queue.put((char, style))

    def stop(self):
        self.stop_event.set()
        if self.consumer_thread:
            self.consumer_thread.join()
        self._flush_buffer()
        if self.current_line:
            self.console.print(Text(self.current_line.rstrip()))
            self.current_line = ""

    def _consumer(self):
        while not self.stop_event.is_set():
            try:
                char, style = self.queue.get(timeout=0.1)
                if char.isspace() and not self.buffer:
                    continue
                self.buffer += char
                if char in ['.', '!', '?', '\n'] or len(self.buffer) >= self.max_line_width:
                    self._flush_buffer(style)
            except queue.Empty:
                if self.buffer:
                    self._flush_buffer()
        self._flush_buffer()

    def _flush_buffer(self, style=None):
        if self.buffer:
            words = self.buffer.split()
            for word in words:
                if len(self.current_line) + len(word) + 1 > self.max_line_width:
                    self.console.print(Text(self.current_line.rstrip(), style=style))
                    self.current_line = word + " "
                else:
                    self.current_line += word + " "
            
            if self.buffer[-1] in ['.', '!', '?', '\n']:
                self.console.print(Text(self.current_line.rstrip(), style=style))
                self.current_line = ""
            
            self.buffer = ""

    def print_user_prompt(self, username):
        self.console.print(f"\n[bold blue]{username}>[/bold blue]", end=" ")

    def print_agent_prompt(self, agent_name):
        self.console.print(f"\n[bold red]{agent_name}>[/bold red] ", end="")

    def print_user_input(self, text):
        # This method is now only for logging or other purposes, not for display
        pass

    def print_agent_response(self, text):
        self.console.print(f"[yellow]{text}[/yellow] 🤖")

# Create a global instance of the printer
global_printer = WordAwareStreamPrinter()
global_printer.start()

# Functions to be used in other modules
def print_user_prompt(username):
    global_printer.print_user_prompt(username)

def print_agent_prompt(agent_name):
    global_printer.print_agent_prompt(agent_name)

def print_user_input(text):
    global_printer.print_user_input(text)

def print_agent_response(text):
    global_printer.print_agent_response(text)

def add_text(text, style=None):
    global_printer.add_text(text, style)

def stop_printer():
    global_printer.stop()
