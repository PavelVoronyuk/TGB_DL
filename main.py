import logging
import asyncio

from aiogram import Dispatcher, Bot, F
from config_data.config import Config, load_config
from handlers import other_handlers
from lexicon.lexicon import LEXICON_RU



logger = logging.getLogger(__name__)

async def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')
    logger.info('Starting bot')
    config: Config = load_config()
    bot = Bot(token = config.tg_bot.token)
    dp = Dispatcher()
    dp.include_router(other_handlers.router)
    await dp.start_polling(bot)



asyncio.run(main())
