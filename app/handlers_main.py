import logging

from aiogram.types import Message, ContentType
from aiogram.utils.exceptions import BadRequest, TelegramAPIError

from config import TG_ADMINS_ID, TG_MANAGED_CHANNEL_ID, TG_OBSERVED_GROUP_ID
from filters import IsMangedChannel, IsObservedGroup
from load_all import dp, bot


# @dp.channel_post_handler()
# async def new_member(message: Message):
#     """
#     Данный хэндлер ловит любое сообщение из канала из отправляет админу сообщение с его айди.
#     :param message:
#     :return:
#     """
#     await bot.send_message(TG_ADMINS_ID[0], f'Сообщение из канала: {message.chat.id}')
#
#
@dp.message_handler(IsObservedGroup())
async def new_member(message: Message):
    """
    Данный хэндлер ловит любое сообщение из группы из отправляет админу сообщение с его айди.
    :param message:
    :return:
    """
    await bot.send_message(TG_ADMINS_ID[0], f'Сообщение из группы: {message.chat.id}')


@dp.message_handler(IsObservedGroup(), content_types=ContentType.LEFT_CHAT_MEMBER)
async def banned_member(message: Message):
    """
    Функция ловит сервисное сообщение о выходе/удалении пользователя из группы и передаёт его для удаления из канала.
    :param message:
    :return:
    """
    await bot.send_message(TG_ADMINS_ID[0], f'Пользователь вышел: {message.left_chat_member.id}')
    return await kick_member(message)


async def kick_member(message: Message):
    """
    Функция удаляет пользователя из канала по ID из сервисного сообщения из группы.
    :param message:
    :return:
    """
    try:
        await bot.kick_chat_member(TG_MANAGED_CHANNEL_ID, message.left_chat_member.id)
    except TelegramAPIError as e:
        logging.info(f'\n\nERROR не удалось удалить пользователя {message.left_chat_member.id} по причине: {e}\n\n')
    else:
        logging.info(f'\n\nПользователь: {message.left_chat_member.id} удалён из канала: {message.chat.id}\n\n')
        await bot.send_message(TG_ADMINS_ID[0], f'Удаляем пользователя: {message.left_chat_member.id} '
                                                f'из канала: {message.chat.id}')
