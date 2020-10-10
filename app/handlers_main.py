
from aiogram.types import Message, ContentType
from aiogram.utils.callback_data import CallbackData

from filters import IsMangedChannel, IsObservedGroup
from load_all import dp

club_cb = CallbackData('deposit', 'club')
withdraw_cb = CallbackData('withdraw', 'action', 'club', 'method')


# goal - observe users in group and kick users in channel

"""
добавили в группу ничего не делаем.
удалили из группы - удаляем из канала
добавился в канал - проверяет есть ли в группе, если нет, то кик
"""


# сделать два фильтра на группу и канал
@dp.message_handler()
async def new_member(message: Message):
    await message.reply(f'Сообщение из чата: {message=}')


# @dp.message_handler(IsMangedChannel(), content_types=ContentType.NEW_CHAT_MEMBERS)
@dp.message_handler(content_types=ContentType.NEW_CHAT_MEMBERS)
async def new_member(message: Message):
    await message.reply(f'В чат зашёл юзер {[user.get_mention(as_html=True) for user in message.new_chat_members]}')
    # return add_member(message)


# @dp.message_handler(IsObservedGroup(), content_types=ContentType.LEFT_CHAT_MEMBER)
@dp.message_handler(content_types=ContentType.LEFT_CHAT_MEMBER)
async def banned_member(message: Message):
    await message.reply(f'В чат удалён юзер {message.left_chat_member.get_mention(as_html=True)}')
    # return kick_member(message)


async def add_member(message: Message):
    # проверяем есть ли в группе, если нет, то кикаем из канала
    await message.reply(f'Этот пользователь есть в группе {await message.chat.get_member(message.from_user.id)}')


async def kick_member(message: Message):
    # кикнули из группы, кикаем из канала
    await message.reply(f'В чат удалён юзер {message.left_chat_member.get_mention(as_html=True)}')

