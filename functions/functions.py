from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from keyboard import keyboard
from config.config import ADMIN_ID
from sql.sql import *
from FSM.fsm_constructor import Registration, Role_user, Lock


router = Router()
sql = sql_request()


@router.message(F.text == "/start")
async def start_bot(message: Message):
    if str(sql.get_id(message.from_user.id)) == str(message.from_user.id):
        await message.answer(f"Здравствуйте, {message.from_user.id}", reply_markup=keyboard.main_kb())
    elif str(message.from_user.id) == str(ADMIN_ID):
         await message.answer("Здравствуйте, администратор!",reply_markup=keyboard.admin_kb())
    else:
        await message.answer("ОШИБКА! Вы не зарегистрированы!", reply_markup=keyboard.start_kb())


@router.message(F.text == "Регистрация")
async def registration(message: Message,state: FSMContext):
    await message.answer("Для начала напишите, как вас зовут?")
    await state.set_state(Registration.setup_username())


# @router.message(Registration.setup_username,F.text==Registration.setup_username)
async def username_choosen(message: Message, state: FSMContext):
    sql.set_or_update_username(message.text,message.from_user.id)
    await state.update_data(username=message.text.lower())
    await message.answer("Спасибо. Теперь, пожалуйста, поделитесь вашим номером:",reply_markup=keyboard.number_set())
    await state.set_state(Registration.setup_number())

@router.message(Registration.setup_number,F.contact)
async def contact_choosen(message: Message, state: FSMContext):
    number = F.contact
    sql.set_or_update_phone(message.from_user.id,F.contact)
    await state.update_data(number)
    # await message.answer("Спасибо. Теперь, пожалуйста, поделитесь геолокацией:",reply_markup=keyboard.number_set())
    # await state.set_state(Registration.setup_number())

@router.message(F.text == "Заблокировать пользователя")
async def lock_user_1(message: Message, state: FSMContext):
    await message.answer("Введите ID пользователя")
    await state.set_state(Role_user.enter_id())

@router.message(Role_user.enter_id)
async def lock_user_2(message: Message, state: FSMContext):
    await state.update_data(Role_user.enter_id())
    await message.answer("Теперь введите роль пользователя (0 = Пользователь, 1 = Админ)")
    await state.set_state(Role_user.enter_role)

@router.message(Role_user.enter_role)
async def lock_user_3(message: Message, state: FSMContext):
    if message.text == "0" or message.text == "1":
        await state.update_data(Role_user.enter_id())
        await message.answer("Теперь введите роль пользователя (0 = Пользователь, 1 = Админ)")
        sql.set_role(Role_user.enter_id,Role_user.enter_id)
        await message.answer("Права успешно выданы")
    else:
        await message.answer("Вы ввели неправильное число!")





