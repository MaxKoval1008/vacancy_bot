from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

button_0 = KeyboardButton('Политика конфиденциальности')
button_1 = KeyboardButton('Cписок предложений')
button_2 = KeyboardButton('Список резюме')
button_3 = KeyboardButton('Мои объявления')
button_4 = KeyboardButton('Мои резюме')

markup_main = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=False
).insert(button_0)
markup_main.row(button_1, button_2)
markup_main.row(button_3, button_4)


button_3_1 = InlineKeyboardButton('Изменить', callback_data='change_ann')
button_3_2 = InlineKeyboardButton('Остановить', callback_data='brake_ann')
button_3_3 = InlineKeyboardButton('Активировать', callback_data='activate_ann')
markup_3_1 = InlineKeyboardMarkup(row_width=2).insert(button_3_1)
markup_3_1.insert(button_3_2)
markup_3_2 = InlineKeyboardMarkup(row_width=2).insert(button_3_1)
markup_3_2.insert(button_3_3)


button_4_1 = InlineKeyboardButton('Изменить', callback_data='change_sum')
button_4_2 = InlineKeyboardButton('Остановить', callback_data='brake_sum')
button_4_3 = InlineKeyboardButton('Активировать', callback_data='activate_sum')
markup_4_1 = InlineKeyboardMarkup(row_width=2).insert(button_4_1)
markup_4_1.insert(button_4_2)
markup_4_2 = InlineKeyboardMarkup(row_width=2).insert(button_4_1)
markup_4_2.insert(button_4_3)

button_work = InlineKeyboardButton('Работа', callback_data='Работа')
button_half_work = InlineKeyboardButton('Подработка', callback_data='Подработка')

markup_choiсe = InlineKeyboardMarkup(row_width=2).insert(button_work)
markup_choiсe.insert(button_half_work)
