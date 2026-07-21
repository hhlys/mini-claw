from abc import ABC, abstractmethod

from mini_claw.message import Msg

import asyncio
import os
from openai import AsyncOpenAI
from mini_claw.formatter import OpenAIFormatter

class ChatResponse:
    def __init__(self, text: str) -> None:
        self.text = text

    def __repr__(self) -> str:
        return f"ChatResponse(text={self.text!r})"


class ChatModelBase(ABC):
    def __init__(self, model_name: str) -> None:
        self.model_name = model_name

    @abstractmethod
    async def __call__(self, messages: list[Msg]) -> ChatResponse:
        pass


class MockModel(ChatModelBase):
    def __init__(self, model_name: str = "mock-model") -> None:
        super().__init__(model_name)

    async def __call__(self, messages: list[Msg]) -> ChatResponse:
        await asyncio.sleep(1)

        last_msg = messages[-1]
        return ChatResponse(f"I received: {last_msg.get_text_content()}")

class DeepSeekModel(ChatModelBase):
    def __init__(
        self,
        model_name: str = "deepseek-v4-pro",
        formatter: OpenAIFormatter | None = None,
    ) -> None:
        super().__init__(model_name)
        self.formatter = formatter or OpenAIFormatter()
        self.client = AsyncOpenAI(
            api_key=os.environ["DEEPSEEK_API_KEY"],
            base_url="https://api.deepseek.com",
        )

    async def __call__(self, messages: list[Msg]) -> ChatResponse:
        response = await self.client.chat.completions.create(
            model=self.model_name,
            messages=self.formatter.format(messages),
            stream=False,
        )

        content = response.choices[0].message.content or ""
        return ChatResponse(content)


async def main() -> None:
    model = MockModel()

    messages = [
        Msg("user", "hello", "user"),
    ]

    response = await model(messages)
    print(response)


if __name__ == "__main__":
    asyncio.run(main())
