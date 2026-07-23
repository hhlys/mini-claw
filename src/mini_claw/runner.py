from mini_claw.agent import AgentBase
from mini_claw.config import AgentConfig
from mini_claw.factory import create_agent_from_config
from mini_claw.message import Msg


class AgentRunner:
    def __init__(self, config: AgentConfig, session_id: str = "default_session_id"):
        self.agent: AgentBase = create_agent_from_config(config=config)
        self.session_id = session_id

    async def run(self, user_text: str) -> Msg:
        msg = Msg("user", user_text, "user")
        reply = await self.agent.reply(msg=msg)
        return reply


class MultiSessionAgentRunner:
    def __init__(self, config: AgentConfig) -> None:
        self.sessions: dict[str, AgentRunner] = {}
        self.config = config

    def get_session(self, session_id: str) -> AgentRunner:
        if session_id not in self.sessions:
            self.sessions[session_id] = AgentRunner(
                config=self.config,
                session_id=session_id,
            )
        return self.sessions[session_id]

    async def run(self, session_id: str, user_text: str) -> Msg:
        runner = self.get_session(session_id)
        return await runner.run(user_text=user_text)
