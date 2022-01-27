from bot import dp
from aiogram import types
import keyboards as kb
from privacy import privacy


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!", reply_markup=kb.markup_main)


@dp.message_handler(text='Политика конфиденциальности')
async def text_handler(message: types.Message):
    await message.reply(privacy)


@dp.message_handler(text='Cписок предложений')
async def text_handler(message: types.Message):
    await message.reply('Кнопка список предложений')


@dp.message_handler(text='Мои объявления')
async def process_command_1(message: types.Message):
    await message.reply("Первая инлайн кнопка", reply_markup=kb.markup_3)


@dp.callback_query_handler(lambda c: c.data == 'Остановить')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text='button_3_1')
    await bot.send_message(callback_query.from_user.id, 'Нажата первая кнопка!')