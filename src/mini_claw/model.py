from typing import List
from mini_claw.message import Msg

class ChatResponse:
    def __init__(self,text:str):
        self.text = text

    def __repr__(self):
        return f"ChatResponse(text={self.text!r})"

class MockModel:
    def __init__(self,model_name:str):
        self.model_name = model_name;

    def __call__(self, messages:List[Msg]):
        last_msg =  messages[-1]
        return ChatResponse(f"I received: {last_msg.get_text_content()}")

if __name__ == "__main__":
    messages = [
        Msg("user", "hello", "user"),
        Msg("assistant", "hi", "assistant"),
        Msg("user", "how are you?", "user"),
    ]

    model = MockModel("mockModel")
    response = model(messages)

    print(response)
    print(response.text)
