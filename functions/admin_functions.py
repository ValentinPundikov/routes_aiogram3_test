from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from keyboard import keyboard
from config.config import ADMIN_ID
from sql.sql import *
from FSM.fsm_constructor import Registration, Role_user, Lock, Delete_user


router = Router()
sql = sql_request()


@router.message(F.text == "Получить список пользователей")
async def get_all_users(message: Message):
    if str(ADMIN_ID) == str(message.from_user.id):
        await message.answer("Получаю список пользователей")
        await message.answer(sql.get_all_users())
    else:
        await message.answer("У Вас недостаточно прав для выполнения данной операции!")


@router.message(F.text == "Заблокировать/Разблокировать пользователя")
async def lock_user_unlock(message: Message, state: FSMContext):
    if str(ADMIN_ID) == str(message.from_user.id):
        await message.answer("Введите ID пользователя:",reply_markup=keyboard.lock_unlock_user_1())
        await state.set_state(Lock.lock())
    else:
        await message.answer("У Вас недостаточно прав для выполнения данной операции!")

async def lock_user_unlock_2(message: Message, state: FSMContext):
    if str(ADMIN_ID) == str(message.from_user.id):
        data = state.update_data(message.text)
        await state.update_data(Lock.lock())
        if str(sql.get_id(data)) == "None":
            await message.answer("Такого пользователя нету", reply_markup=keyboard.admin_kb())
        else:
            await message.answer("Выберите опцию для пользователя", reply_markup=keyboard.lock_unlock_user_2())
    else:
        await message.answer("У Вас недостаточно прав для выполнения данной операции!")


@router.callback_query(F.data == "lock_user")
async def lock_user_state(callback: CallbackQuery, state: FSMContext):
    if str(ADMIN_ID) == str(callback.message.from_user.id):
        user_data = await state.get_data()
        sql.unlock_lock_user(user_data,1)
        await callback.message.answer("Пользователь заблокирован!", reply_markup=keyboard.admin_kb())
    else:
        await callback.message.answer("У Вас недостаточно прав для выполнения данной операции!")


@router.callback_query(F.data == "unlock_user")
async def lock_user_state(callback: CallbackQuery, state: FSMContext):
    if str(ADMIN_ID) == str(callback.message.from_user.id):
        user_data = await state.get_data()
        sql.unlock_lock_user(user_data,0)
        await callback.message.answer("Пользователь разблокирован!", reply_markup=keyboard.admin_kb())
    else:
        await callback.message.answer("У Вас недостаточно прав для выполнения данной операции!")



@router.message(F.text == "Дать права пользователю")
async def setter_role_user(message: Message, state_1: FSMContext):
    if str(ADMIN_ID) == str(message.from_user.id):
        await message.answer("Введите ID пользователя:",reply_markup=keyboard.lock_unlock_user_1())
        await state_1.set_state(Role_user.enter_role())
    else:
        await message.answer("У Вас недостаточно прав для выполнения данной операции!")

async def setter_role_user_1(message: Message, state: FSMContext):
    if str(ADMIN_ID) == str(message.from_user.id):
        data = state.update_data(message.text)
        await state.update_data(Lock.lock())
        if str(sql.get_id(data)) == "None":
            await message.answer("Такого пользователя нету", reply_markup=keyboard.admin_kb())
        else:
            await message.answer("Выберите опцию для пользователя", reply_markup=keyboard.lock_unlock_user_2())
    else:
        await message.answer("У Вас недостаточно прав для выполнения данной операции!")


@router.callback_query(F.data == "role_user_0")
async def lock_user_state(callback: CallbackQuery, state: FSMContext):
    if str(ADMIN_ID) == str(callback.message.from_user.id):
        user_data = await state.get_data()
        sql.set_role(user_data,0)
        await callback.message.answer("Права админа выданы!", reply_markup=keyboard.admin_kb())
    else:
        await callback.message.answer("У Вас недостаточно прав для выполнения данной операции!")


@router.callback_query(F.data == "role_user_1")
async def lock_user_state(callback: CallbackQuery, state: FSMContext):
    if str(ADMIN_ID) == str(callback.message.from_user.id):
        user_data = await state.get_data()
        sql.set_role(user_data,1)
        await callback.message.answer("Права пользователя выданы!", reply_markup=keyboard.admin_kb())
    else:
        await callback.message.answer("У Вас недостаточно прав для выполнения данной операции!")




@router.message(F.text == "Дать права пользователю")
async def delete_user(message: Message, state_1: FSMContext):
    if str(ADMIN_ID) == str(message.from_user.id):
        await message.answer("Введите ID пользователя:",reply_markup=keyboard.lock_unlock_user_1())
        await state_1.set_state(Role_user.enter_role())
    else:
        await message.answer("У Вас недостаточно прав для выполнения данной операции!")

async def delete_user_1(message: Message, state: FSMContext):
    if str(ADMIN_ID) == str(message.from_user.id):
        data = state.update_data(message.text)
        await state.update_data(Lock.lock())
        if str(sql.get_id(data)) == "None":
            await message.answer("Такого пользователя нету", reply_markup=keyboard.admin_kb())
        else:
            await message.answer("Выберите опцию для пользователя", reply_markup=keyboard.lock_unlock_user_2())
    else:
        await message.answer("У Вас недостаточно прав для выполнения данной операции!")


@router.callback_query(F.data == "role_user_0")
async def lock_user_state(callback: CallbackQuery, state: FSMContext):
    if str(ADMIN_ID) == str(callback.message.from_user.id):
        user_data = await state.get_data()
        sql.set_role(user_data,0)
        await callback.message.answer("Права админа выданы!", reply_markup=keyboard.admin_kb())
    else:
        await callback.message.answer("У Вас недостаточно прав для выполнения данной операции!")


@router.callback_query(F.data == "role_user_1")
async def lock_user_state(callback: CallbackQuery, state: FSMContext):
    if str(ADMIN_ID) == str(callback.message.from_user.id):
        user_data = await state.get_data()
        sql.set_role(user_data,1)
        await callback.message.answer("Права пользователя выданы!", reply_markup=keyboard.admin_kb())
    else:
        await callback.message.answer("У Вас недостаточно прав для выполнения данной операции!")



@router.message(F.text == "Удалить пользователя")
async def delete_user(message: Message, state_1: FSMContext):
    if str(ADMIN_ID) == str(message.from_user.id):
        await message.answer("Введите ID пользователя:",reply_markup=keyboard.lock_unlock_user_1())
        await state_1.set_state(Delete_user.delete_us())
    else:
        await message.answer("У Вас недостаточно прав для выполнения данной операции!")

async def del_user(message: Message, state: FSMContext):
    if str(ADMIN_ID) == str(message.from_user.id):
        data = state.update_data(message.text)
        await state.update_data(Delete_user.delete_us())
        if str(sql.get_id(data)) == "None":
            await message.answer("Такого пользователя нету", reply_markup=keyboard.admin_kb())
        else:
            await message.answer("Удалить пользователя", reply_markup=keyboard.delete_user_by_admin())
    else:
        await message.answer("У Вас недостаточно прав для выполнения данной операции!")


@router.callback_query(F.data == "deluser")
async def del_user_by_adm(callback: CallbackQuery, state: FSMContext):
    if str(ADMIN_ID) == str(callback.message.from_user.id):
        user_data = await state.get_data()
        sql.delete_user(user_data)
        await callback.message.answer("Пользователь удален", reply_markup=keyboard.admin_kb())
    else:
        await callback.message.answer("У Вас недостаточно прав для выполнения данной операции!")

