from aiogram.dispatcher import FSMContext
from bot import dp
from aiogram import types
import keyboards as kb
from privacy import privacy_text
from data_base import UsersBase
from states import AnnouncementForm as ann
from states import SummaryForm as sum

db = UsersBase('users.db')


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


@dp.message_handler(commands=['all_users'])
async def get_text_messages(message: types.Message):
    all_users = db.get_all_users()
    await message.answer(all_users)


@dp.message_handler(text=['Мои объявления'])
async def process_start_command(message: types.Message):
    db.create_table_announcement()
    if db.check_users_announcement(message.from_user.id):
        all_user_announcement = db.all_user_announcement(message.from_user.id)
        if all_user_announcement[-1][-1] == 1:
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
        data['Approved'] = 0
    await message.answer("Спасибо, вакансия сохранена.")
    data = await state.get_data()
    db.add_to_db_announcement(list(data.values()))
    await state.finish()


@dp.message_handler(text='Политика конфиденциальности')
async def text_handler(message: types.Message):
    await message.answer(privacy_text)


@dp.message_handler(text='Cписок предложений')
async def text_handler(message: types.Message):
    all_vacancy = db.all_announcements()
    await message.reply(all_vacancy)


@dp.message_handler(text='Мои резюме')
async def process_start_command(message: types.Message):
    db.create_table_summary()
    if db.check_users_summary(message.from_user.id):
        all_user_summary = db.all_user_summary(message.from_user.id)
        if all_user_summary[-1][-1] == 1:
            await message.reply(all_user_summary, reply_markup=kb.markup_4_1)
        else:
            await message.reply(all_user_summary, reply_markup=kb.markup_4_2)
    else:
        await message.answer("Пожалуйста, введите Ваше ФИО.")
        await sum.UserName.set()


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
        data['Approved'] = 0
    await message.answer("Спасибо, резюме сохранено.")
    data = await state.get_data()
    db.add_to_db_summary(list(data.values()))
    await state.finish()


@dp.message_handler(text='Список резюме')
async def text_handler(message: types.Message):
    all_summary = db.all_summary()
    await message.reply(all_summary)


@dp.message_handler(commands='11')
async def text_handler(message: types.Message):
    all_summary = db.all_summary()
    for i in all_summary:
        await message.reply(i[:-1])
