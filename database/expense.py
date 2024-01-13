from dataclasses import dataclass
from datetime import datetime


@dataclass
class Expense:
    name: str | None
    subname: str | None
    price: float | None
    today: datetime | None
    raw: str
    user_id: int | None
    flag: bool|None

    def __repr__(self):
        return f'{self.__sizeof__()}'







