import ssl

from aiogram import Dispatcher
from aiogram.utils.executor import start_webhook

from config import (TG_ADMINS_ID, WEBAPP_HOST, WEBAPP_PORT, WEBHOOK_HOST,
                    WEBHOOK_PORT,
                    WEBHOOK_PATH, SSL_DIR, SSL_CERT, SSL_PRIV)
from database import create_db
from load_all import bot

WEBHOOK_URL = f'{WEBHOOK_HOST}:{WEBHOOK_PORT}{WEBHOOK_PATH}'


async def on_startup(dispatcher: Dispatcher):
    await create_db()

    # Check webhook
    webhook = await bot.get_webhook_info()

    # If URL is bad
    if webhook.url != WEBHOOK_URL:
        # If URL doesnt match current - remove webhook
        if not webhook.url:
            await bot.delete_webhook()

    # # Set new URL for webhook
    await bot.set_webhook(WEBHOOK_URL, certificate=open(f'{SSL_DIR}{SSL_CERT}', 'rb').read())

    # Send message to admin
    await bot.send_message(TG_ADMINS_ID[0], "Я запущен!")


async def on_shutdown(dispatcher: Dispatcher):
    # insert code here to run it before shutdown

    # Send message to admin
    await bot.send_message(TG_ADMINS_ID[0], "Я выключен!")

    # Close bot
    await bot.close()
    #
    # Close DB connection (if used)
    await dp.storage.close()
    await dp.storage.wait_closed()


if __name__ == '__main__':
    # forwarding dp from handlers
    from handlers_main import dp
    from handlers_cancel import dp

    # Generate SSL context.
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain(f'{SSL_DIR}{SSL_CERT}', f'{SSL_DIR}{SSL_PRIV}')

    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
        ssl_context=context
    )
