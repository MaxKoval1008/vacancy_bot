from aiogram.dispatcher import FSMContext
from bot import dp
from aiogram import types
import keyboards as kb
from privacy import privacy_text
from data_base import UsersBase
from states import AnnouncementForm as ann
from states import SummaryForm as sum
from states import AdminPassword
from .admin_settings import is_admin

db = UsersBase('users.db')
admin = []


@dp.message_handler(commands=['is_admin'])
async def process_start_command(message: types.Message):
    await message.answer(f"Для доступа в кабинет администратора нажмите кнопку и введите пароль",
                         reply_markup=kb.markup_is_admin)


@dp.callback_query_handler(lambda c: c.data == 'admin_keyboard')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await callback_query.message.answer("Введите пароль:")
    await AdminPassword.Password.set()


@dp.message_handler(state=AdminPassword.Password)
async def process_start_command(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Password'] = message.text
    data = await state.get_data()
    if is_admin(list(data.values())[0]):
        await message.answer('Добро пожаловать в кабинет администратора!', reply_markup=kb.markup_admin_keyboard)
        if message.from_user.id not in admin:
            admin.append(message.from_user.id)
    else:
        await message.answer('Неправильный пароль.')
    await state.finish()


@dp.message_handler(text=['Объявления'])
async def process_start_command(message: types.Message):
    if message.from_user.id in admin:
        all_announcements = db.all_announcements()
        for i in all_announcements:
            text = f'''\n
                    ID: {i[0]}\n
                    Тип работы: {i[1]}\n
                    Название вакансии: {i[2]}\n
                    Описание вакансии: {i[3]}\n
                    Зарплатные ожидания: {i[4]}\n
                    Телефон: {i[5]}\n
                    Пользователь: {i[6]}\n
                    Статус: {i[7]}\n
                    Подтверждение: {i[8]} \n'''
            await message.answer(text)
        await message.answer('Для активации нажмите кнопку ниже', reply_markup=kb.markup_admin_change_ann)
    else:
        await message.answer('Отказано в доступе')


@dp.callback_query_handler(lambda c: c.data in ['markup_admin_change_ann', 'more_ann'])
async def process_callback_button1(callback_query: types.CallbackQuery):
    text_value = db.disapproved_user_announcement()
    try:
        text = f'''\nID: {text_value[0][0]}
        Тип работы: {text_value[0][1]}
        Название вакансии: {text_value[0][2]}
        Описание вакансии: {text_value[0][3]}
        Зарплатные ожидания: {text_value[0][4]}
        Телефон: {text_value[0][5]}
        Пользователь: {text_value[0][6]}
        Статус: {text_value[0][7]}
        Подтверждение: {text_value[0][8]}'''
        await callback_query.message.answer(text, reply_markup=kb.markup_change_mode_ann)
    except IndexError:
        await callback_query.message.answer('Все объявления подтверждены.')


@dp.callback_query_handler(lambda c: c.data == 'approve_ann')
async def process_callback_button1(callback_query: types.CallbackQuery):
    disapproved_user_announcement = db.disapproved_user_announcement()
    try:
        id = disapproved_user_announcement[0][0]
        db.approving_announcement(id)
        await callback_query.message.answer('Объявление подтверждено', reply_markup=kb.markup_more_ann)
    except IndexError:
        await callback_query.message.answer('Все объявления подтверждены.')


@dp.callback_query_handler(lambda c: c.data == 'disapprove_ann')
async def process_callback_button1(callback_query: types.CallbackQuery):
    approved_user_announcement = db.approved_user_announcement()
    try:
        id = approved_user_announcement[0][0]
        db.disapproving_announcement(id)
        await callback_query.message.answer('Объявление удалено', reply_markup=kb.markup_more_ann)
    except IndexError:
        await callback_query.message.answer('Все объявления удалены.')


@dp.message_handler(text=['Резюме'])
async def process_start_command(message: types.Message):
    if message.from_user.id in admin:
        all_summary = db.all_summary()
        for i in all_summary:
            text = f'''\n
            ID: {i[0]}\n
            ФИО: {i[1]}\n
            Навыки: {i[2]}\n
            Район: {i[3]}\n
            Телефон: {i[4]}\n
            Пользователь: {i[5]}\n
            Статус: {i[6]}\n
            Подтверждение: {i[7]} \n'''
            await message.answer(text)
        await message.answer('Для активации нажмите кнопку ниже', reply_markup=kb.markup_admin_change_sum)
    else:
        await message.answer('Отказано в доступе')


@dp.callback_query_handler(lambda c: c.data in ['markup_admin_change_sum', 'more_sum'])
async def process_callback_button1(callback_query: types.CallbackQuery):
    text_value = db.disapproved_user_summary()
    await callback_query.message.answer(text_value)
    try:
        text = f'''\n
        ID: {text_value[0][0]}\n
        ФИО: {text_value[0][1]}\n
        Навыки: {text_value[0][2]}\n
        Район: {text_value[0][3]}\n
        Телефон: {text_value[0][4]}\n
        Пользователь: {text_value[0][5]}\n
        Статус: {text_value[0][6]}\n
        Подтверждение: {text_value[0][7]} \n'''
        await callback_query.message.answer(text, reply_markup=kb.markup_change_mode_sum)
    except IndexError:
        await callback_query.message.answer('Все резюме подтверждены.')


@dp.callback_query_handler(lambda c: c.data == 'approve_sum')
async def process_callback_button1(callback_query: types.CallbackQuery):
    disapproved_user_summary = db.disapproved_user_summary()
    try:
        id = disapproved_user_summary[0][0]
        db.approving_summary(id)
        await callback_query.message.answer('Резюме подтверждено', reply_markup=kb.markup_more_sum)
    except IndexError:
        await callback_query.message.answer('Все резюме подтверждены.')


@dp.callback_query_handler(lambda c: c.data == 'disapprove_sum')
async def process_callback_button1(callback_query: types.CallbackQuery):
    approved_user_summary = db.approved_user_summary()
    try:
        id = approved_user_summary[0][0]
        db.disapproving_summary(id)
        await callback_query.message.answer('Резюме удалено', reply_markup=kb.markup_more_sum)
    except IndexError:
        await callback_query.message.answer('Все резюме удалены.')


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    db.create_table_users()
    user_id = message.from_user.id
    user_name = message.from_user.username
    if not db.exists_user(user_id):
        db.add_to_db_users(user_id, user_name)
    await message.reply(f"Привет!", reply_markup=kb.markup_main)


@dp.message_handler(commands=['profile'])
async def get_text_messages(message: types.Message):
    user_profile = db.profile_user(message.from_user.id)
    await message.answer(f'User ID: {user_profile[0]}, Имя пользователя: {str(user_profile[1])}')


@dp.message_handler(text='Пользователи')
async def get_text_messages(message: types.Message):
    if message.from_user.id in admin:
        all_users = db.get_all_users()
        await message.answer(all_users)
    else:
        await message.answer('Отказано в доступе')


@dp.message_handler(text='Выйти')
async def get_text_messages(message: types.Message):
    if message.from_user.id in admin:
        admin.remove(message.from_user.id)
        await message.answer('Выход', reply_markup=kb.markup_main)
    else:
        await message.answer('Отказано в доступе')


@dp.message_handler(text=['Мои объявления'])
async def process_start_command(message: types.Message):
    db.create_table_announcement()
    if db.check_users_announcement(message.from_user.id):
        all_user_announcement = db.all_user_announcement(message.from_user.id)
        if all_user_announcement[-1][-2] == 'Active':
            await message.reply(all_user_announcement, reply_markup=kb.markup_3_1)
        else:
            await message.reply(all_user_announcement, reply_markup=kb.markup_3_2)
    else:
        await ann.WorkType.set()
        await message.answer("Пожалуйста, сделайте выбор, используя клавиатуру ниже.", reply_markup=kb.markup_choiсe)


@dp.callback_query_handler(lambda c: c.data in ['brake_ann', 'activate_ann'])
async def process_callback_button1(callback_query: types.CallbackQuery):
    all_user_announcement = db.all_user_announcement(callback_query.from_user.id)
    id = all_user_announcement[0][0]
    db.change_status_announcements(id)
    await callback_query.answer("Изменение сохранено.")


@dp.callback_query_handler(lambda c: c.data in ['Работа', 'Подработка'], state=ann.WorkType)
async def process_callback_button1(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['WorkType'] = callback_query.data
    await ann.NameVacancy.set()
    await callback_query.message.answer("Пожалуйста, укажите название вакансии.")


@dp.callback_query_handler(lambda c: c.data == 'change_ann')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await ann.WorkType.set()
    await callback_query.message.answer("Пожалуйста, сделайте выбор, используя клавиатуру ниже.",
                                        reply_markup=kb.markup_choiсe)


@dp.message_handler(state=ann.NameVacancy)
async def process_start_command(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['NameVacancy'] = message.text
    await ann.Description.set()
    await message.answer("Пожалуйста, укажите описание вакансии.")


@dp.message_handler(state=ann.Description)
async def process_start_command(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Description'] = message.text
    await ann.Salary.set()
    await message.answer("Пожалуйста, укажите ожидаему заработную плату.")


@dp.message_handler(state=ann.Salary)
async def process_start_command(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Salary'] = message.text
    await ann.TelNumber.set()
    await message.answer("Пожалуйста, укажите Ваш номер телефона.")


@dp.message_handler(state=ann.TelNumber)
async def process_start_command(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['TelNumber'] = message.text
        data['User'] = message.from_user.id
        data['IsActive'] = 'Active'
        data['Approved'] = 'Disapproved'
    await message.answer("Спасибо, вакансия сохранена.")
    data = await state.get_data()
    if db.check_users_announcement(message.from_user.id):
        all_user_announcement = db.all_user_announcement(message.from_user.id)
        id = all_user_announcement[0][0]
        data_list = list(data.values())
        data_list.append(id)
        db.change_user_announcement(data_list)
    else:
        db.add_to_db_announcement(list(data.values()))
    await state.finish()


@dp.message_handler(text='Политика конфиденциальности')
async def text_handler(message: types.Message):
    await message.answer(privacy_text)


@dp.message_handler(text='Cписок предложений')
async def text_handler(message: types.Message):
    all_vacancy = db.all_announcements()
    for i in all_vacancy:
        text = f'''\n
        ID: {i[0]}\n
        Тип работы: {i[1]}\n
        Название вакансии: {i[2]}\n
        Описание вакансии: {i[3]}\n
        Зарплатные ожидания: {i[4]}\n
        Телефон: {i[5]}\n
        Пользователь: {i[6]}\n
        Статус: {i[7]}\n
        Подтверждение: {i[8]} \n'''
        await message.answer(text)


@dp.message_handler(text='Мои резюме')
async def process_start_command(message: types.Message):
    db.create_table_summary()
    if db.check_users_summary(message.from_user.id):
        all_user_summary = db.all_user_summary(message.from_user.id)
        if all_user_summary[-1][-2] == 'Active':
            await message.reply(all_user_summary, reply_markup=kb.markup_4_1)
        else:
            await message.reply(all_user_summary, reply_markup=kb.markup_4_2)
    else:
        await message.answer("Пожалуйста, введите Ваше ФИО.")
        await sum.UserName.set()


@dp.callback_query_handler(lambda c: c.data == 'change_sum')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await sum.UserName.set()
    await callback_query.message.answer("Пожалуйста, введите Ваше ФИО.")


@dp.callback_query_handler(lambda c: c.data in ['brake_sum', 'activate_sum'])
async def process_callback_button1(callback_query: types.CallbackQuery):
    all_user_summary = db.all_user_summary(callback_query.from_user.id)
    id = all_user_summary[0][0]
    db.change_status_summary(id)
    await callback_query.answer("Изменение сохранено.")


@dp.message_handler(state=sum.UserName)
async def process_start_command(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['UserName'] = message.text
    await sum.Skills.set()
    await message.answer("Пожалуйста, укажите Ваши основные навыки.")


@dp.message_handler(state=sum.Skills)
async def process_start_command(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Skills'] = message.text
    await sum.District.set()
    await message.answer("Пожалуйста, укажите район проживания.")


@dp.message_handler(state=sum.District)
async def process_start_command(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['District'] = message.text
    await sum.TelNumber.set()
    await message.answer("Пожалуйста, укажите Ваш номер телефона.")


@dp.message_handler(state=sum.TelNumber)
async def process_start_command(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['TelNumber'] = message.text
        data['UserID'] = message.from_user.id
        data['IsActive'] = 'Active'
        data['Approved'] = 'Disapproved'
    await message.answer("Спасибо, резюме сохранено.")
    data = await state.get_data()
    if db.check_users_summary(message.from_user.id):
        all_users_summary = db.all_user_summary(message.from_user.id)
        id = all_users_summary[0][0]
        data_list = list(data.values())
        data_list.append(id)
        db.change_user_summary(data_list)
    else:
        db.add_to_db_summary(list(data.values()))
    await state.finish()


@dp.message_handler(text='Список резюме')
async def text_handler(message: types.Message):
    all_summary = db.all_summary()
    for i in all_summary:
        text = f'''\n
        ID: {i[0]}\n
        ФИО: {i[1]}\n
        Навыки: {i[2]}\n
        Район: {i[3]}\n
        Телефон: {i[4]}\n
        Пользователь: {i[5]}\n
        Статус: {i[6]}\n
        Подтверждение: {i[7]} \n'''
        await message.answer(text)
