from datetime import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext

from config import settings
from database import crud
from states.user import UserStates
from view import keyboards, messages


async def main_menu(message: types.Message):
    await UserStates.MAIN_MENU.set()
    await message.answer(messages.IN_MAIN_MENU, reply_markup=keyboards.main_menu)

