import logging
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

API_TOKEN = '5273284238:AAEXBxZTxeDIWXJZXMktNJlk0otuMZamUqA'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


if __name__ == '__main__':
    from handlers.main_handlers import dp
    executor.start_polling(dp, skip_updates=True)
