from aiogram.fsm.state import StatesGroup, State


class Registration(StatesGroup):
    setup_username = State()
    setup_number = State()
    setup_location = State()


class Lock(StatesGroup):
    lock = State()

class Role_user(StatesGroup):
    enter_role = State()


class Delete_user(StatesGroup):
    delete_us = State()




