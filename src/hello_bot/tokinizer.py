import re
from typing import Callable


class Token:
    @classmethod
    @property
    def nikname(cls):
        def matcher(value) -> str | None:
            nikname = re.match(r"@(\w+)", value)
            if nikname:
                return nikname.group(1)
            return None
        return cls(matcher)

    def __init__(self, expression: Callable[[str], str | None]) -> None:
        self.expression = expression

    def catch(self, value: str):
        return self.expression(value)
