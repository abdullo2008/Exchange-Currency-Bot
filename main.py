import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from app.handlers import setup_handlers

from app.handlers import router
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()
dp.include_router(router)
setup_handlers(dp, bot)


async def main():
    try:
        await dp.start_polling(bot)
    except asyncio.CancelledError:
        logging.error("Опрос был отменен. Проверьте проблемы с управлением задачами.")
    except Exception as e:
        logging.error(f"Произошла ошибка: {e}")
    finally:
        logging.info("Бот остановлен.")


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.INFO, encoding="utf-8")

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info('Бот остановлен вручную с помощью KeyboardInterrupt')
    except Exception as e:
        logging.error(f"Произошла непредвиденная ошибка: {e}")
