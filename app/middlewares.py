import logging

from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.utils.exceptions import MessageNotModified, MessageError


class ObserverMiddleware(BaseMiddleware):

    def __init__(self):
        super().__init__()

    async def on_pre_process_message(self, message: types.Message, data: dict, *arg, **kwargs):
        logging.info(f'{message=} \n\n\n data {data=}')

    async def on_pre_process_callback_query(self, callback_query: types.CallbackQuery, data: dict, *arg, **kwargs):
        logging.info(f'{callback_query=} \n\n\n data {data=}')

    async def on_pre_process_update(self, update: types.Update, data: dict, *arg, **kwargs):
        logging.info(f'{update=} \n\n\n data {data=}')
