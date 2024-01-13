# from aiogram import Bot, Dispatcher
# from aiogram.filters import BaseFilter
# from aiogram.types import Message
#
#
# # Список с ID администраторов бота. !!!Замените на ваш!!!
# admin_ids: list[int] = [173901673]
#
#
# # Собственный фильтр, проверяющий юзера на админа
# class IsAdmin(BaseFilter):
#     def __init__(self, admin_ids: list[int]) -> None:
#         # В качестве параметра фильтр принимает список с целыми числами
#         self.admin_ids = admin_ids
#
#     async def __call__(self, message: Message) -> bool:
#         return message.from_user.id in self.admin_ids
#
#
# # Этот хэндлер будет срабатывать, если апдейт от админа
# @dp.message(IsAdmin(admin_ids))
# async def answer_if_admins_update(message: Message):
#     await message.answer(text='Вы админ')


