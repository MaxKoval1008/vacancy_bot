import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import keyboards as kb
from privacy import privacy

API_TOKEN = '5273284238:AAEXBxZTxeDIWXJZXMktNJlk0otuMZamUqA'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


if __name__ == '__main__':
    from handlers import dp
    executor.start_polling(dp, skip_updates=True)
