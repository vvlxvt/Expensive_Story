import logging, sys
import config
from keyboards import set_main_menu
from aiohttp import web
import handlers
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application

conf = config.load_config(None)
# TOKEN = conf.tg_bot.token
TOKEN = '6541851084:AAFIsmRzvzndK-x2vZxyFra-P40yZtPkbnw'
ADMIN_IDS = [541172529, 1194999116]
# ADMIN_IDS = conf.tg_bot.admin_ids


WEB_SERVER_HOST = "0.0.0.0"
WEB_SERVER_PORT = 80

WEBHOOK_PATH = f"/{TOKEN}"
BASE_WEBHOOK_URL = 'https://6180-94-43-154-7.ngrok-free.app'
# BASE_WEBHOOK_URL = "https://expensive-story-vvlxvt.amvera.io"

async def on_startup(bot: Bot) -> None:
    await bot.set_webhook(f"{BASE_WEBHOOK_URL}{WEBHOOK_PATH}",)
    await set_main_menu(bot)


def main() -> None:
    dp = Dispatcher()
    dp.include_router(handlers.user_handlers.router)
    dp.include_router(handlers.other_handlers.router)

    # Register startup hook to initialize webhook
    dp.startup.register(on_startup)

    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)


    # Create aiohttp.web.Application instance
    app = web.Application()

    # Create an instance of request handler
    webhook_requests_handler = SimpleRequestHandler(dispatcher=dp, bot=bot,)
    # Register webhook handler on application
    webhook_requests_handler.register(app, path=WEBHOOK_PATH)

    # Mount dispatcher startup and shutdown hooks to aiohttp application
    setup_application(app, dp, bot=bot)


    # And finally start webserver
    web.run_app(app, host=WEB_SERVER_HOST, port=WEB_SERVER_PORT,)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    main()

# Tanya_user-Id = '1194999116'