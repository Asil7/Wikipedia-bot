import logging
import wikipedia
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5758994979:AAEzCAklI3y-Lb7aZfRQfqQEPWICTW_MaNw'
# t.me/wikipediauz_new_bot

wikipedia.set_lang('uz')

logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):

    await message.reply("Salom.Wikipedia Botiga xush kelibsiz !!!\n\nO'zingizga kerakli maqola nomini kiriting👇")


@dp.message_handler()
async def send(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bu mavzuga oid maqola topilmadi")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
