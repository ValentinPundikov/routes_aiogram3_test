from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from keyboard import keyboard
from config.config import ADMIN_ID
from sql.sql import *
from FSM.fsm_constructor import Registration, Role_user, Lock


router = Router()
sql = sql_request()

@router.message(F.text == "Посмотреть информацию о себе")
async def delete_user(message: Message):
    await message.answer("Получение информации о себе",reply_markup=keyboard.main_kb())
    result = sql.get_my_info(str(message.from_user.id))
    await message.answer(result)


@router.message(F.text == "Изменить данные")
async def change_my_info_0(message: Message):
    pass


