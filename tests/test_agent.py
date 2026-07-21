import unittest

from mini_claw import AssistantAgent, MockModel, Msg


class AssistantAgentTest(unittest.IsolatedAsyncioTestCase):
    async def test_agent_reply_returns_message(self) -> None:
        agent = AssistantAgent("mini", MockModel())

        reply = await agent.reply(Msg("user", "hello", "user"))

        self.assertEqual(reply.name, "mini")
        self.assertEqual(reply.content, "I received: hello")
        self.assertEqual(reply.role, "assistant")

    async def test_agent_remembers_user_and_assistant_messages(self) -> None:
        agent = AssistantAgent("mini", MockModel())

        await agent.reply(Msg("user", "hello", "user"))

        messages = agent.memory.get_memory()

        self.assertEqual(len(messages), 2)
        self.assertEqual(messages[0].role, "user")
        self.assertEqual(messages[1].role, "assistant")


if __name__ == "__main__":
    unittest.main()