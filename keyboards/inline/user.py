from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def like_dislike_inline_keyboard_def(likes, dislikes):
    below_photo = InlineKeyboardMarkup(
        inline_keyboard = [
            [
                InlineKeyboardButton(text = f'{likes}👍', callback_data="like" ),
                InlineKeyboardButton(text = f'{dislikes}👎', callback_data="dislike" ),
            ]
        ]
    )

    return below_photo