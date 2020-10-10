import logging

from aiogram.types import Message, ContentType
from aiogram.utils.callback_data import CallbackData
from aiogram.utils.exceptions import BadRequest, TelegramAPIError

from config import TG_ADMINS_ID, TG_MANAGED_CHANNEL_ID
from filters import IsMangedChannel, IsObservedGroup
from load_all import dp, bot

club_cb = CallbackData('deposit', 'club')
withdraw_cb = CallbackData('withdraw', 'action', 'club', 'method')


# @dp.channel_post_handler()
# async def new_member(message: Message):
#     await bot.send_message(TG_ADMINS_ID[0], f'Сообщение из канала! : {message}')
#
#
@dp.message_handler(IsObservedGroup())
async def new_member(message: Message):
    await bot.send_message(TG_ADMINS_ID[0], f'Сообщение из группы! : {message.chat.id}')


# @dp.message_handler(IsObservedGroup(), content_types=ContentType.LEFT_CHAT_MEMBER)
@dp.message_handler(IsObservedGroup(), content_types=ContentType.LEFT_CHAT_MEMBER)
async def banned_member(message: Message):
    """
    Проверяем кого кикнули из группы и кикаем его из канала!
    :param message:
    :return:
    """
    await bot.send_message(TG_ADMINS_ID[0], f'{message.left_chat_member.id}')
    return await kick_member(message)


async def kick_member(message: Message):
    # кикнули из группы, кикаем из канала
    # TODO make exception handler
    try:
        await bot.kick_chat_member(TG_MANAGED_CHANNEL_ID, message.left_chat_member.id)
    except TelegramAPIError as e:
        logging.info(f'\n\nERROR не удалось удалить пользователя {message.left_chat_member.id} по причине: {e}\n\n')
    else:
        await bot.send_message(TG_ADMINS_ID[0], f'Удаляем пользователя: {message.left_chat_member.id} '
                                                f'из канала: {message.chat.id}')
