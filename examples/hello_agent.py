from mini_claw import AssistantAgent, DeepSeekModel, Msg
from mini_claw import get_default_agent_config,create_agent_from_config


import asyncio


async def main() -> None:
    config = get_default_agent_config();
    agent = create_agent_from_config(config)

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