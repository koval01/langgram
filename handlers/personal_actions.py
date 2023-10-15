from aiogram import types
from dispatcher import dp


@dp.message_handler(is_owner=True, commands="ping", commands_prefix="!/")
async def cmd_ping_bot(message: types.Message):
    await message.reply("<b>Up & Running!</b>")
