# add send broadcast. Add get data
import logging
from asyncio import sleep

from aiogram.utils import exceptions

from load_all import bot


async def send_messages(message: str, users_id: list):
    log = logging.getLogger('broadcast')
    for user_id in users_id:
        try:
            await bot.send_message(user_id, message)
            await sleep(0.05)  # Telegram limit 30 message per second, here set 20 msg per second
        except exceptions.BotBlocked:
            log.error(f"Target [ID:{user_id}]: blocked by user")
        except exceptions.ChatNotFound:
            log.error(f"Target [ID:{user_id}]: invalid user ID")
        except exceptions.RetryAfter as e:
            log.error(f"Target [ID:{user_id}]: Flood limit is exceeded. Sleep {e.timeout} seconds.")
            await sleep(e.timeout)
            return await send_messages(message, user_id)
        except exceptions.UserDeactivated:
            log.error(f"Target [ID:{user_id}]: user is deactivated")
        except exceptions.TelegramAPIError:
            log.exception(f"Target [ID:{user_id}]: failed")
            pass
        else:
            log.info(f"Target [ID:{user_id}]: success")
