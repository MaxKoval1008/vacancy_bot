from aiogram.dispatcher.filters.state import State, StatesGroup


class AnnouncementForm(StatesGroup):
    WorkType = State()
    NameVacancy = State()
    Description = State()
    Salary = State()
    TelNumber = State()
    User = State()
    IsActive = State()
    Approved = State()


class SummaryForm(StatesGroup):
    UserName = State()
    Skills = State()
    District = State()
    TelNumber = State()
    UserID = State()
    IsActive = State()
    Approved = State()


class AdminPassword(StatesGroup):
    Password = State()
