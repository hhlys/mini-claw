from mini_claw.message import Msg


class InMemoryMemory:
    def __init__(self) -> None:
        self.messages: list[Msg] = []

    def add(self, msg: Msg) -> None:
        self.messages.append(msg)

    def clear(self) -> None:
        self.messages.clear()

    def get_memory(self) -> list[Msg]:
        return self.messages


if __name__ == "__main__":
    memory = InMemoryMemory()

    user_msg = Msg("user", "hello", "user")
    assistant_msg = Msg("assistant", "hi", "assistant")

    memory.add(user_msg)
    memory.add(assistant_msg)

    print(memory.get_memory())

    memory.clear()
    print(memory.get_memory())
