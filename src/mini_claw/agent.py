from mini_claw.model import MockModel
from mini_claw.model import ChatResponse
from mini_claw.memory import InMemoryMemory
from mini_claw.message import Msg


class AssistantAgent:
    def __init__(self,name:str,model:MockModel):
        self.name = name;
        self.model = model;
        self.memory = InMemoryMemory()

    def reply(self,msg:Msg):
        self.memory.add(msg)
        res = self.model(self.memory.get_memory())

        reply_msg = Msg(self.name, res.text, "assistant")
        self.memory.add(reply_msg)

        return res


if __name__ == "__main__":
    agent = AssistantAgent("assistant_agent",MockModel("mockModel"))
    print(agent.reply(Msg("user","hello","user")))
    print(agent.memory.get_memory())