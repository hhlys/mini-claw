class ModelConfig:
    def __init__(
        self,
        provider: str,
        model_name: str,
    ) -> None:
        self.provider = provider
        self.model_name = model_name

    def __repr__(self) -> str:
        return f"ModelConfig(provider={self.provider!r}, model_name={self.model_name!r})"


class AgentConfig:
    def __init__(
        self,
        agent_id: str,
        name: str,
        sys_prompt: str,
        model: ModelConfig,
    ) -> None:
        self.agent_id = agent_id
        self.name = name
        self.sys_prompt = sys_prompt
        self.model = model

    def __repr__(self) -> str:
        return (
            "AgentConfig("
            f"agent_id={self.agent_id!r}, "
            f"name={self.name!r}, "
            f"sys_prompt={self.sys_prompt!r}, "
            f"model={self.model!r}"
            ")"
        )


def get_default_agent_config() -> AgentConfig:
    return AgentConfig(
        agent_id="default",
        name="mini",
        sys_prompt="You are a helpful assistant.",
        model=ModelConfig(
            provider="deepseek",
            model_name="deepseek-v4-pro",
        ),
    )


if __name__ == "__main__":
    config = get_default_agent_config()
    print(config)