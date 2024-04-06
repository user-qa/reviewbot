from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

user_main_menu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text='Rasmlar'),
            KeyboardButton(text='Rasm Joylash')
        ]
    ], resize_keyboard=True
)