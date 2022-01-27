from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

button_0 = KeyboardButton('Политика конфиденциальности')
button_1 = KeyboardButton('Cписок предложений')
button_2 = KeyboardButton('Список вакансий')
button_3 = KeyboardButton('Мои объявления')
button_4 = KeyboardButton('Мои резюме')

markup_main = ReplyKeyboardMarkup(
    one_time_keyboard=False
).insert(button_0)
markup_main.row(button_1, button_2)
markup_main.row(button_3, button_4)

button_3_1 = InlineKeyboardButton('Остановить', callback_data='Остановить')
button_3_2 = InlineKeyboardButton('Активировать', callback_data='Активировать')
markup_3 = InlineKeyboardMarkup(row_width=2).insert(button_3_1)
markup_3.insert(button_3_2)



button_hi = KeyboardButton('Привет! 👋')

greet_kb2 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True
).add(button_hi)
