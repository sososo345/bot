from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio
import random

bot = Bot(token="7255704116:AAFWY64huuMSXOm4wOknzgLoxsEFbnlIeQE")
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message:types.Message):
    await message.answer("hello")

@dp.message(Command("echo"))
async def echo(message:types.message):
     text = message.text.replace("/echo","").strip()
     if text:
          await message.answer(text)
     else:
          await message.answer("напиши после /echo")

          
@dp.message(Command("photobobra"))
async def cmd_img(message: types.Message):
     await message.answer_photo("https://i.pinimg.com/originals/88/b8/39/88b8396bc196fad7042a18c4e98875a1.jpg")


@dp.message(Command("rps"))
async def rps(message:types.message):
     botschoose=["камень","ножницы","бумага"]
     user = message.text.replace("/rps","").strip()
     bot = random.choice(botschoose)
     userin = botschoose.index(user)
     botin = botschoose.index(bot)
     if (bot==user):
          await message.answer("ничья")
     elif(botin-userin==1) or (user=="бумага"and bot=='камень'):
          await message.answer(f"вы выбрали {user}\n бот выбрал {bot} \n вы выйграли")
     else:
          await message.answer(f"вы выбрали {user} \n бот выбрал {bot} \n вы проиграли")
     

async def main():
    print('Запкск бота')
    await dp.start_polling(bot)

if __name__ == "__main__":
        asyncio.run(main())