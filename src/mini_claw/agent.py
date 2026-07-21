from mini_claw.memory import InMemoryMemory
from mini_claw.message import Msg
from mini_claw.model import ChatModelBase, MockModel
from abc import ABC, abstractmethod

import asyncio


class AgentBase:
    def __init__(self, name: str):
        self.name = name
        self.memory = InMemoryMemory()
    
    def observe(self, msg:Msg) -> None:
        self.memory.add(msg)

    @abstractmethod
    async def reply(self, msg: Msg) -> Msg:
        pass



class AssistantAgent(AgentBase):
    def __init__(self, name: str, model: ChatModelBase, sys_prompt:str | None = None) -> None:
        super().__init__(name)
        self.model = model
        self.sys_prompt = sys_prompt

        if sys_prompt:
            self.memory.add(Msg("system",sys_prompt,"system"))

    async def reply(self, msg: Msg) -> Msg:
        self.observe(msg)
        res = await self.model(self.memory.get_memory())

        reply_msg = Msg(self.name, res.text, "assistant")
        self.memory.add(reply_msg)

        return reply_msg

async def main() -> None:
    agent = AssistantAgent("assistant_agent", MockModel("mockModel"))
    res = await agent.reply(Msg("user", "hello", "user"))
    print(res)
    print(agent.memory.get_memory())


if __name__ == "__main__":
    asyncio.run(main())
