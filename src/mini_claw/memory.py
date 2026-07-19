from typing import List
from mini_claw.message import Msg


class InMemoryMemory:
    def __init__(self):
        self.messgaes:List[Msg] = []

    def add(self,msg:Msg):
        self.messgaes.append(msg)

    def clear(self):
        self.messgaes.clear();

    def get_memory(self)->List[Msg]:
        return self.messgaes;

if __name__ == "__main__":
    memory = InMemoryMemory()

    user_msg = Msg("user", "hello", "user")
    assistant_msg = Msg("assistant", "hi", "assistant")

    memory.add(user_msg)
    memory.add(assistant_msg)

    print(memory.get_memory())

    memory.clear()
    print(memory.get_memory())