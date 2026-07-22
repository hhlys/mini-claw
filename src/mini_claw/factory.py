from mini_claw.model import ChatModelBase,MockModel,DeepSeekModel
from mini_claw.config import ModelConfig,AgentConfig
from mini_claw.agent import AgentBase,AssistantAgent



def create_model_from_config(config: ModelConfig) -> ChatModelBase:
    if (config.provider=="mock"):
        return MockModel(config.model_name)
    if (config.provider=="deepseek"):
        return DeepSeekModel(config.model_name) 
    raise ValueError(f"Unsupported model provider: {config.provider}")


def create_agent_from_config(config: AgentConfig) -> AgentBase:

    model = create_model_from_config(config.model)
    return AssistantAgent(name=config.name,model=model,sys_prompt=config.sys_prompt)

if __name__ == "__main__":
    from mini_claw.config import get_default_agent_config

    config = get_default_agent_config()
    agent = create_agent_from_config(config)

    print(config)
    print(agent.name)
    print(agent.model.model_name)
    print(agent.memory.get_memory())