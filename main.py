import asyncio
import json
import time

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from creds import T_token, id_chat

bot = Bot(token=T_token)
dp = Dispatcher()


@dp.message(CommandStart())
async def get_start(message: Message):
    uid = message.from_user.id
    await message.answer(str(uid))


@dp.message(Command(commands=["mess"]))
async def get_help(message: Message):
    await message.answer(message.text)
    await message.answer(message.from_user.username)


async def main():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(dp.start_polling(bot, handle_signals=False))

if __name__ == "__main__":
    asyncio.run(main())

application = asyncio.run(main())
