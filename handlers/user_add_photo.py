from loader import db, dp
from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from states.user import GetPhoto

@dp.message_handler(text = ['Rasm Joylash'])
async def add_photo(message: types.Message):
    result = db.get_photo_by_chat_id(message.chat.id)
    if result:
        photo = result[2]
        await message.answer_photo(photo)
    else:
        text = 'Send a picture! '
        await GetPhoto.get_photo.set()
        await message.answer(text)


@dp.message_handler(state = GetPhoto.get_photo, content_types=types.ContentTypes.PHOTO)
async def get_photo(message:types.Message, state: FSMContext):
    await state.update_data(photo = message.photo[-1].file_id, chat_id = message.chat.id)
    data = await state.get_data()
    db.add_user_photo(data)
    text = 'Photo uploaded✅'
    await message.answer(text)
    await state.finish()