from aiogram.filters import BaseFilter
from aiogram.types import Message


# Собственный фильтр, проверяющий юзера на админа
class IsAdmin(BaseFilter):
    def __init__(self, admin_id: str) -> None:
        # В качестве параметра фильтр принимает список с целыми числами
        self.admin_id = admin_id

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id == self.admin_id




