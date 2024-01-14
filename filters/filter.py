from aiogram.filters import BaseFilter
from aiogram.types import Message


# Собственный фильтр, проверяющий на админа
class IsAdmin(BaseFilter):
    def __init__(self, admin_ids: str) -> None:
        # В качестве параметра фильтр принимает список с целыми числами
        self.admin_ids = admin_ids

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admin_ids




