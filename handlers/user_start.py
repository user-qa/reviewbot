from keyboards.default.user import user_main_menu
from aiogram.dispatcher import FSMContext
from loader import dp, db
from aiogram import types
from states.user import RegisterState
@dp.message_handler(commands=['start'])
async def user_start(message: types.Message):
    user_info = db.get_user_chat_id(message.chat.id)
    if user_info:
        text = f'Assalomu alaykum, xush kelibsiz, {user_info[2].upper()}'
        await message.answer(text, reply_markup=user_main_menu)

    else:
        text = "Assalomu alaykum, ismingizni kiriting! "
        await message.answer(text)

        await RegisterState.full_name.set()

@dp.message_handler(state=RegisterState.full_name)
async def get_full_name(message: types.Message, state: FSMContext):
    await state.update_data(full_name = message.text, chat_id = message.chat.id)
    text = 'Telefon raqamingizni kiriting'
    await message.answer(text)

    await RegisterState.phone_number.set()

@dp.message_handler(state=RegisterState.phone_number)
async def get_phone_number(message: types.Message, state: FSMContext):
    await state.update_data(phone_number = message.text)
    text = 'Locationni kiriting! '
    await message.answer(text)

    await RegisterState.location.set()


@dp.message_handler(state = RegisterState.location)
async def get_location(message: types.Message, state: FSMContext):
    await state.update_data(location = message.text)
    data = await state.get_data()
    db.add_user(data)
    text = 'Successfully Registered✅'
    await message.answer(text, reply_markup=user_main_menu)
    await state.finish()



