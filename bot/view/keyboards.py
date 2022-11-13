from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                           KeyboardButton, ReplyKeyboardMarkup)
from view import buttons

main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(KeyboardButton(buttons.shop))
main_menu.add(KeyboardButton(buttons.referal))
main_menu.add(KeyboardButton(buttons.contacts))
