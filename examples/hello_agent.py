from mini_claw import AssistantAgent, DeepSeekModel, Msg

import asyncio


async def main() -> None:
    agent = AssistantAgent("mini", DeepSeekModel(), "You are a helpful assistant.")

    user_msg = Msg("user", "hello ， who are you?", "user")
    reply_msg = await agent.reply(user_msg)

    print("Reply:")
    print(reply_msg)

    print()
    print("Memory:")
    for msg in agent.memory.get_memory():
        print(msg)


if __name__ == "__main__":
    asyncio.run(main())