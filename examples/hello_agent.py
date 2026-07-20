from mini_claw import AssistantAgent, MockModel, Msg


def main() -> None:
    agent = AssistantAgent("mini", MockModel())

    user_msg = Msg("user", "hello mini-claw", "user")
    reply_msg = agent.reply(user_msg)

    print("Reply:")
    print(reply_msg)

    print()
    print("Memory:")
    for msg in agent.memory.get_memory():
        print(msg)


if __name__ == "__main__":
    main()