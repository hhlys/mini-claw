import asyncio

from mini_claw import MultiSessionAgentRunner, get_default_agent_config


async def main() -> None:
    config = get_default_agent_config()
    runner = MultiSessionAgentRunner(config=config)

    await runner.run("Default", "hello, my name is dudu")
    reply_msg = await runner.run("Default", "what is my name?")

    print("Reply1:")
    print(reply_msg)
    print("Memory1:")
    for msg in runner.get_session("Default").agent.memory.get_memory():
        print(msg)

    reply_msg = await runner.run("QA", "what is my name?")
    print("Reply2:")
    print(reply_msg)

    print("Memory2:")
    for msg in runner.get_session("QA").agent.memory.get_memory():
        print(msg)


if __name__ == "__main__":
    asyncio.run(main())
