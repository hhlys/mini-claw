from typing import Any

from mini_claw.message import Msg


class OpenAIFormatter:
    def format(self, messages: list[Msg]) -> list[dict[str, Any]]:
        return [
            {
                "role": msg.role,
                "content": msg.get_text_content(),
            }
            for msg in messages
        ]