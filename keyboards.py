from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

button_0 = KeyboardButton('Политика конфиденциальности')
button_1 = KeyboardButton('Cписок предложений')
button_2 = KeyboardButton('Список резюме')
button_3 = KeyboardButton('Мои объявления')
button_4 = KeyboardButton('Мои резюме')
admin_button = InlineKeyboardButton('Кабинет администратора', callback_data='admin_keyboard')
markup_is_admin = InlineKeyboardMarkup().insert(admin_button)
admin_change_ann = InlineKeyboardButton('Режим активации', callback_data='markup_admin_change_ann')
markup_admin_change_ann = InlineKeyboardMarkup().row(admin_change_ann)
button_change_ann_1 = InlineKeyboardButton('Подтвердить', callback_data='approve_ann')
button_change_ann_2 = InlineKeyboardButton('Отклонить', callback_data='disapprove_ann')
button_change_ann_3 = InlineKeyboardButton('Еще', callback_data='more_ann')

markup_change_mode_ann = InlineKeyboardMarkup(row_width=2).row(button_change_ann_1, button_change_ann_2)
markup_more_ann = InlineKeyboardMarkup().row(button_change_ann_3)

admin_change_sum = InlineKeyboardButton('Режим активации', callback_data='markup_admin_change_sum')
markup_admin_change_sum = InlineKeyboardMarkup().row(admin_change_ann)
button_change_sum_1 = InlineKeyboardButton('Подтвердить', callback_data='approve_sum')
button_change_sum_2 = InlineKeyboardButton('Отклонить', callback_data='disapprove_sum')
button_change_sum_3 = InlineKeyboardButton('Еще', callback_data='more_sum')

markup_change_mode_sum = InlineKeyboardMarkup(row_width=2).row(button_change_sum_1, button_change_sum_2)
markup_more_sum = InlineKeyboardMarkup().row(button_change_sum_3)

admin_button_1 = KeyboardButton('Объявления')
admin_button_2 = KeyboardButton('Резюме')
admin_button_3 = KeyboardButton('Пользователи')
admin_button_4 = KeyboardButton('Выйти')

markup_admin_keyboard = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=False
)
markup_admin_keyboard.row(admin_button_1, admin_button_2, admin_button_3)
markup_admin_keyboard.insert(admin_button_4)


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

markup_choice = InlineKeyboardMarkup(row_width=2).insert(button_work)
markup_choice.insert(button_half_work)

