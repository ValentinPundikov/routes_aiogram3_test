from typing import Callable, Dict, Any

from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


def admin_kb() -> ReplyKeyboardMarkup:
    """

    :rtype: object
    """
    kb = ReplyKeyboardBuilder()
    kb.button(text="Посмотреть всех пользователей")
    kb.button(text="Дать права пользователю")
    kb.button(text="Заблокировать пользователя")
    kb.button(text="Удалить пользователя")
    kb.adjust(2, 2)
    return kb.as_markup(resize_keyboard=True)


def start_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Регистрация")
    kb.button(text="Посмотреть информацию")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)

def number_set() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Поделиться номером",request_contact=True,callback_data="send_my_number")
    kb.adjust(1,1)
    return kb.as_markup(resize_keyboard=True)
def main_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Посмотреть информацию о себе")
    kb.button(text="Изменить данные",)
    kb.button(text="Удалить информацию")
    kb.button(text="Получить местоположение", request_location=True)
    kb.adjust(2, 2)
    return kb.as_markup(resize_keyboard=True)

def enter_role_id():
    kb = InlineKeyboardBuilder()
    kb.button("Введите ID пользователя")
    kb.adjust(1, 1)

def enter_role_2():
    kb = InlineKeyboardBuilder()
    kb.button("Админ",callback_data="role_admin")
    kb.button("Пользователь",callback_data="role_user")
    kb.adjust(1, 1)

def lock_unlock_user_1():
    kb = InlineKeyboardBuilder()
    kb.button("Назад", callback_data="back_lock")
    kb.adjust(1, 1)

def lock_unlock_user_2():
    kb = InlineKeyboardBuilder()
    kb.button("Заблокировать",callback_data="lock_user")
    kb.button("Разблокировать",callback_data="unlock_user")
    kb.button("Назад", callback_data="back_lock")
    kb.adjust(2, 2)


def admin_set_role():
    kb = InlineKeyboardBuilder()
    kb.button("Права админа",callback_data="role_user_0")
    kb.button("Права пользователя",callback_data="role_user_1")
    kb.button("Назад", callback_data="back_lock")
    kb.adjust(2, 2)


def delete_user_by_admin():
    kb = InlineKeyboardBuilder()
    kb.button("Да", callback_data="deluser")
    kb.adjust(2, 2)


# def users_options() -> Callable[[dict[str, Any]], ReplyKeyboardMarkup]:
#     kb = ReplyKeyboardBuilder
#     kb.button(text="sss")
#     kb.adjust(1, 1)

