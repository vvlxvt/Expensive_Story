from dataclasses import dataclass


@dataclass
class Expense:
    name: str | None
    subname: str | None
    price: float | None
    today: str | None
    raw: str
    flag: bool|None

    def __repr__(self):
        return f'{self.name!r}, {self.subname!r}, {self.price!r}, {self.today!r}'






