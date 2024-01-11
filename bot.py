import logging, sys
import config
from handlers import other_handlers, user_handlers
from aiohttp import web
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application

conf = config.load_config(None)
TOKEN = conf.tg_bot.token
ADMIN_ID = conf.tg_bot.admin_id

WEB_SERVER_HOST = "0.0.0.0"
WEB_SERVER_PORT = 80

WEBHOOK_PATH = "/6006947703:AAFiIBqbYWhmZUl6l1crqb3ZbQI4CpiXkoU"
BASE_WEBHOOK_URL = 'https://045c-94-43-154-7.ngrok-free.app'
# BASE_WEBHOOK_URL = "https://expensive-story-vvlxvt.amvera.io"

async def on_startup(bot: Bot) -> None:
    await bot.set_webhook(f"{BASE_WEBHOOK_URL}{WEBHOOK_PATH}",)


def main() -> None:
    dp = Dispatcher()
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

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