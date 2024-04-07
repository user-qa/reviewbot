from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


user_main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Photos"),
            KeyboardButton(text="Upload Photo"),
        ]
    ], resize_keyboard=True
)

phone_number_share = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Send Phone Number", request_contact=True)
        ]
    ], resize_keyboard=True
)

location_share = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Manzilni jo'natish", request_location=True)
        ]
    ], resize_keyboard=True
)