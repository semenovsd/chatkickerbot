from typing import Union

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from load_all import bot, dp


# Cancel button for all cases
@dp.message_handler(text='cancel', state='*')
@dp.callback_query_handler(text='cancel', state='*')
async def cancel_handler(message: Union[types.Message, types.CallbackQuery], state: FSMContext):
    await state.finish()
    keyboard_markup = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text='На главную', callback_data='start')]]
    )
    try:
        await bot.delete_message(message.from_user.id, message.message.message_id or message.message_id)
    except Exception:
        pass
    await bot.send_message(message.from_user.id,
                           text='Отменено. Вернитесь в галвное меню.',
                           reply_markup=keyboard_markup)
