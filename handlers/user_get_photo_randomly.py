from loader import db, dp
from aiogram import types
from keyboards.inline.user import like_dislike_inline_keyboard_def


@dp.message_handler(text = ['Rasmlar'])
async def get_random_photo(message: types.Message):
    result = db.get_random_photo(message.chat.id)
    if result:
        k = db.get_liked_and_disliked_photos(result[2])
        likes, dislikes = k[0][0], k[1][0]
        reply_markup_like_dislike = await like_dislike_inline_keyboard_def(likes, dislikes)
        await message.answer_photo(photo = result[2],  reply_markup= reply_markup_like_dislike)
    else:
        text = 'No active photos'
        await message.answer(text=text)

