import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import TGBOT_TOKEN
from middlewares import AccessMiddleware

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.DEBUG)

storage = MemoryStorage()

bot = Bot(token=TGBOT_TOKEN)
dp = Dispatcher(bot, storage=storage)

# get user tg ID and send to AccessMiddleware
dp.middleware.setup(AccessMiddleware())
