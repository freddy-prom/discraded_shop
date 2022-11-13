from aiogram import types
from aiogram.dispatcher import FSMContext

from database import crud
from loader import dp, bot, logger
from states.user import UserStates
from swtichers import UserSwitchers
from view import buttons, keyboards, messages

from config import settings


@dp.message_handler(commands=["start"], state="*")
async def start(message: types.Message):
    try:
        crud.create_user(message.from_user.id, "@" + message.from_user.username)
    except Exception:
        pass
    await UserSwitchers.main_menu(message)
