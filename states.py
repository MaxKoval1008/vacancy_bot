from aiogram.dispatcher.filters.state import State, StatesGroup


class AnnouncementForm(StatesGroup):
    WorkType = State()
    NameVacancy = State()
    Description = State()
    Salary = State()
    TelNumber = State()
    User = State()


class SummaryForm(StatesGroup):
    UserName = State()
    Skills = State()
    District = State()
    TelNumber = State()
    UserID = State()
