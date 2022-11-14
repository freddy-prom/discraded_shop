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

        if message.from_user.username:
            name = "@" + message.from_user.username
        else:
            name = (message.from_user.first_name if message.from_user.first_name else ""
                    ) + " " + (
                       message.from_user.first_name if message.from_user.last_name else "")

        if message.text.split()[-1] != '/start':
            referer = int(message.text.split()[-1])
        else:
            referer = None
        crud.create_user(message.from_user.id, name, referer)
    except Exception:
        pass
    await UserSwitchers.main_menu(message)


@dp.message_handler(text=buttons.contacts, state=UserStates.MAIN_MENU)
async def contacts(message: types.Message):
    await message.answer(messages.CONTACTS)


@dp.message_handler(text=buttons.referal, state=UserStates.MAIN_MENU)
async def referal(message: types.Message):
    await message.answer(messages.REFERALS_INFO.format(user_id=message.from_user.id,
                                                       points=crud.get_user(message.from_user.id).points))
