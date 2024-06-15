from loader import dp, bot
from aiogram import types

from functions.transliterate import to_cyrillic, to_latin
from data.config import CHAT_ID


@dp.message_handler(lambda message: message.chat.id == CHAT_ID)
async def check_message_handler(message: types.Message):
    text = message.text.lower()
    text_list = text.split()

    word = "teotimur"
    word2 = "teotemur"
    word3 = "teo"

    if word.isascii():
        word_latin = word
        word_cyrlic = to_cyrillic(word_latin)

        del word
    else:
        word_cyrlic = word
        word_latin = to_latin(word_cyrlic)

        del word

    if word2.isascii():
        word2_latin = word2
        word2_cyrlic = to_cyrillic(word2_latin)

        del word2
    else:
        word2_cyrlic = word2
        word2_latin = to_latin(word2_cyrlic)

        del word2
    
    if word3.isascii():
        word3_latin = word3
        word3_cyrlic = to_cyrillic(word3_latin)

        del word3
    else:
        word3_cyrlic = word3
        word3_latin = to_latin(word3_cyrlic)

        del word3

    if not len(text_list) > 30:
        if (
            (word_latin in text_list) or (word_cyrlic in text_list) or
            (word2_latin in text_list) or (word2_cyrlic in text_list) or
            (word3_latin in text_list) or (word3_cyrlic in text_list)
        ):
            await message.answer(
                text = f"""<b>Foydalanuvchi {message.from_user.full_name}, siz guruhda taqiqlangan so'zdan foydalandingiz 🚫</b>"""
            )
            await message.delete()
    else:
        await message.answer(
                text = f"""<b>Foydalanuvchi {message.from_user.full_name}, guruhda 30 ta so'zdan oshiq xabar yozish taqiqlanadi 🚫</b>"""
            )
        await message.delete()

    