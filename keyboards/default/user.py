from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

user_main_menu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text='Rasmlar'),
            KeyboardButton(text='Rasm Joylash')
        ]
    ], resize_keyboard=True
)



below_photo = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text = '10👍 10', callback_data="like" ),
            InlineKeyboardButton(text = '10👎 10', callback_data="dislike" ),
        ]
    ]
)