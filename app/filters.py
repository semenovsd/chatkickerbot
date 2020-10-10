from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message

from config import TG_OBSERVED_GROUP_ID, TG_MANAGED_CHANNEL_ID


class IsObservedGroup(BoundFilter):
    async def check(self, message: Message) -> bool:
        return message.chat.id == int(TG_OBSERVED_GROUP_ID)


class IsMangedChannel(BoundFilter):
    async def check(self, message: Message) -> bool:
        return message.chat.id == int(TG_MANAGED_CHANNEL_ID)


