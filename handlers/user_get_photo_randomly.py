from loader import db, dp
from aiogram import types


@dp.message_handler(text = ['Rasmlar'])
async def add_photo(message: types.Message):
    result = db.get_random_photo(message.chat.id)[2]
    await message.answer_photo(result)