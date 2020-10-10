from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message

from config import TG_NOTICE_GROUP_ID, TG_MANAGEDCHANNEL_ID


class IsObservedGroup(BoundFilter):
    async def check(self, message: Message) -> bool:
        return message.chat.id == TG_NOTICE_GROUP_ID


class IsMangedChannel(BoundFilter):
    async def check(self, message: Message) -> bool:
        return message.chat.id == TG_MANAGEDCHANNEL_ID


