import logging
from aiogram import Bot, Dispatcher, executor, types
from keyboards import keyboards as kb
from privacy import privacy
from config import API_TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!", reply_markup=kb.markup3)


@dp.message_handler(content_types=['text'])
async def text_handler(message: types.Message):
    if message.text == 'Политика конфиденциальности':
        await message.reply(privacy)

#
# @dp.callback_query_handler(func=lambda c: c.data == 'button_0')
# async def process_callback_button1(callback_query: types.CallbackQuery):
#     await bot.answer_callback_query(callback_query.id)
#     await bot.send_message(callback_query.from_user.id, 'Нажата первая кнопка!')


# @dp.callback_query_handler(func=lambda c: c.data == 'button_1')
# async def process_callback_button1(callback_query: types.CallbackQuery):
#     await bot.answer_callback_query(callback_query.id)
#     await bot.send_message(callback_query.from_user.id, 'Нажата вторая кнопка!')
#
#
# @dp.callback_query_handler(func=lambda c: c.data == 'button_2')
# async def process_callback_button1(callback_query: types.CallbackQuery):
#     await bot.answer_callback_query(callback_query.id)
#     await bot.send_message(callback_query.from_user.id, 'Нажата третья кнопка!')
#
#
# @dp.callback_query_handler(func=lambda c: c.data == 'button_3')
# async def process_callback_button1(callback_query: types.CallbackQuery):
#     await bot.answer_callback_query(callback_query.id)
#     await bot.send_message(callback_query.from_user.id, 'Нажата четвертая кнопка!')
#
#
# @dp.callback_query_handler(func=lambda c: c.data == 'button_4')
# async def process_callback_button1(callback_query: types.CallbackQuery):
#     await bot.answer_callback_query(callback_query.id)
#     await bot.send_message(callback_query.from_user.id, 'Нажата пятая кнопка!')

#
# @dp.message_handler(commands=['hi1'])
# async def process_hi1_command(message: types.Message):
#     await message.reply("Первое - изменяем размер клавиатуры", reply_markup=kb.greet_kb1)


@dp.message_handler(commands=['hi2'])
async def process_hi2_command(message: types.Message):
    await message.reply("Второе - прячем клавиатуру после одного нажатия", reply_markup=kb.greet_kb2)


@dp.message_handler(commands=['hi3'])
async def process_hi3_command(message: types.Message):
    await message.reply("Третье - добавляем больше кнопок", reply_markup=kb.markup3)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
