from typing import List
from mini_claw.message import Msg
from abc import ABC,abstractmethod

class ChatResponse:
    def __init__(self,text:str):
        self.text = text

    def __repr__(self):
        return f"ChatResponse(text={self.text!r})"

class ChatModelBase(ABC):

    def __init__(self, model_name:str):
        self.model_name = model_name
    
    @abstractmethod
    def __call__(self, messages:List[Msg]):
        pass

class MockModel(ChatModelBase):
    def __init__(self,model_name:str = "mock-model"):
        super().__init__(model_name)

    def __call__(self, messages:List[Msg]):
        last_msg =  messages[-1]
        return ChatResponse(f"I received: {last_msg.get_text_content()}")

if __name__ == "__main__":
    model = MockModel()

    messages = [
        Msg("user", "hello", "user"),
    ]

    response = model(messages)
    print(response)