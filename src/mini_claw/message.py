class Msg:
    def __init__(self, name: str, content: str, role: str) -> None:
        self.name = name
        self.content = content
        self.role = role

    def get_text_content(self) -> str:
        return self.content

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "content": self.content,
            "role": self.role,
        }

    def __repr__(self) -> str:
        return f"Msg(name={self.name!r}, content={self.content!r}, role={self.role!r})"

    @classmethod
    def from_dict(cls, data: dict) -> "Msg":
        return cls(data["name"], data["content"], data["role"])


if __name__ == "__main__":
    msg = Msg("user", "hello", "user")
    print(msg)
