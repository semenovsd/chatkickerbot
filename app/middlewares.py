"""Аутентификация пользователей — проверяем есть ли пользователь с таким телеграмм ID в бд"""
from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware

from database import User


class AccessMiddleware(BaseMiddleware):

    def __init__(self):
        super().__init__()

    async def on_pre_process_message(self, message: types.Message, data: dict):
        data['user'] = await User().get_or_create(message)

    async def on_pre_process_callback_query(self, call: types.CallbackQuery, data: dict):
        data['user'] = await User().get_or_create(call)
