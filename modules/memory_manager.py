from collections import deque
 
class MemoryManager:
    def __init__(self, max_memory_size=10):
        self.memory = deque(maxlen=max_memory_size)
 
    def add_to_memory(self, user_input: str, bot_response: str):
        self.memory.append((user_input, bot_response))
 
    def get_memory(self):
        return list(self.memory)
