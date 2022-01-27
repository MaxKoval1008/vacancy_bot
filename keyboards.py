from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

button_0 = KeyboardButton('Политика конфиденциальности')
button_1 = KeyboardButton('Cписок предложений')
button_2 = KeyboardButton('Список вакансий')
button_3 = KeyboardButton('Мои объявления')
button_4 = KeyboardButton('Мои резюме')

markup3 = ReplyKeyboardMarkup().insert(button_0)
markup3.row(button_1, button_2)
markup3.row(button_3, button_4)

button_hi = KeyboardButton('Привет! 👋')

greet_kb2 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True
).add(button_hi)

