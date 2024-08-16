import queue
import threading
import logging

logging.basicConfig(level=logging.ERROR)

class WordAwareStreamPrinter:
    def __init__(self, max_line_width=80):
        self.queue = queue.Queue()
        self.max_line_width = max_line_width
        self.stop_event = threading.Event()
        self.consumer_thread = None
        self.buffer = ""
        self.current_line = ""

    def start(self):
        if self.consumer_thread is None or not self.consumer_thread.is_alive():
            self.stop_event.clear()
            self.consumer_thread = threading.Thread(target=self._consumer)
            self.consumer_thread.start()

    def add_text(self, text):
        for char in text:
            self.queue.put(char)

    def stop(self):
        self.stop_event.set()
        if self.consumer_thread:
            self.consumer_thread.join()
        self._flush_buffer()
        if self.current_line:
            print(self.current_line.rstrip())
            self.current_line = ""

    def _consumer(self):
        while not self.stop_event.is_set():
            try:
                char = self.queue.get(timeout=0.1)
                if char.isspace() and not self.buffer:
                    continue
                self.buffer += char
                if char in ['.', '!', '?', '\n'] or len(self.buffer) >= self.max_line_width:
                    self._flush_buffer()
            except queue.Empty:
                if self.buffer:
                    self._flush_buffer()
        self._flush_buffer()

    def _flush_buffer(self):
        if self.buffer:
            words = self.buffer.split()
            for word in words:
                if len(self.current_line) + len(word) + 1 > self.max_line_width:
                    print(self.current_line.rstrip())
                    self.current_line = word + " "
                else:
                    self.current_line += word + " "
            
            if self.buffer[-1] in ['.', '!', '?', '\n']:
                print(self.current_line.rstrip())
                self.current_line = ""
            
            self.buffer = ""
