
from aiogram.types import Message, ContentType
from aiogram.utils.callback_data import CallbackData

from config import TG_ADMINS_ID, TG_NOTICE_CHANNEL_ID, TG_NOTICE_GROUP_ID
from filters import IsMangedChannel, IsObservedGroup
from load_all import dp, bot

club_cb = CallbackData('deposit', 'club')
withdraw_cb = CallbackData('withdraw', 'action', 'club', 'method')


# goal - observe users in group and kick users in channel

"""
добавили в группу ничего не делаем.
удалили из группы - удаляем из канала
добавился в канал - проверяет есть ли в группе, если нет, то кик
"""


@dp.channel_post_handler()
async def new_member(message: Message):
    await bot.send_message(TG_ADMINS_ID[0], f'Сообщение из канала! : {message}')


@dp.message_handler()
async def new_member(message: Message):
    await bot.send_message(TG_ADMINS_ID[0], f'Сообщение из группы! : {message}')


@dp.channel_post_handler(chat_id=TG_NOTICE_CHANNEL_ID, content_types=ContentType.NEW_CHAT_MEMBERS)
async def new_member(message: Message):
    """
    Если зашёл в канал, надо проверить, есть ли он в группе, если нет, то кикнуть!
    :param message:
    :return:
    """
    await message.reply(f'В чат зашёл юзер {[user.get_mention(as_html=True) for user in message.new_chat_members]}')
    # return add_member(message)


@dp.message_handler(chat_id=TG_NOTICE_GROUP_ID, content_types=ContentType.LEFT_CHAT_MEMBER)
async def banned_member(message: Message):
    """
    Проверяем кого кикнули из группы, его же надо кикнуть из канала!
    :param message:
    :return:
    """
    await message.reply(f'В чат удалён юзер {message.left_chat_member.get_mention(as_html=True)}')
    # return kick_member(message)


async def add_member(message: Message):
    # проверяем есть ли в группе, если нет, то кикаем из канала
    await message.reply(f'Этот пользователь есть в группе {await message.chat.get_member(message.from_user.id)}')
    # await message.chat.kick(user_id=...)


async def kick_member(message: Message):
    # кикнули из группы, кикаем из канала
    await message.reply(f'В чат удалён юзер {message.left_chat_member.get_mention(as_html=True)}')

