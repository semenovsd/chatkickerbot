from typing import Dict, Union

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, Message, ContentType
from aiogram.utils.callback_data import CallbackData
from aiogram.utils.exceptions import MessageNotModified

from database import User
from load_all import bot, dp

club_cb = CallbackData('deposit', 'club')
withdraw_cb = CallbackData('withdraw', 'action', 'club', 'method')


@dp.callback_query_handler(text='start')
@dp.message_handler(CommandStart())
async def start_cmd_handler(message: Union[Message, CallbackQuery], state: FSMContext, user: User):
    """
    Стартовый экран приветствия.
    :param message:
    :param state:
    :param user:
    :return:
    """
    pass
