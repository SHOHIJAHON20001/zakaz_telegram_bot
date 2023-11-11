import sys
import logging
import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram import F
from aiogram.enums import ParseMode
from aiogram.filters import Command 
from aiogram.types import Message 
from aiogram.utils.markdown import hbold
from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton
from config import TOKEN

dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    kb = (
            [types.KeyboardButton(text="Rangli chop etish")],
            [types.KeyboardButton(text="Rangsiz chop etish")]
        )
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer(f"Xush Kelibsiz, {hbold(message.from_user.full_name)}", reply_markup=keyboard)
    

@dp.message(F.text == "Rangli chop etish")
async def rangli(message: types.Message):
    # Create a ReplyKeyboardMarkup with the "Ortga" button
    ortga_kb = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Ortga")]],
        resize_keyboard=True,
    )
    await message.answer("Rangsiz printer 100 sumdan hisoblaydi har bir varoq uchun. Varoqlar sonini kiriting (faqat raqam kiriting): ", reply_markup=ortga_kb)

@dp.message(F.text == "Umumiy")
async def umumiy(message: types.Message):
    # Assuming cost_per_varoq is the cost returned from the rangli function
    cost_per_varoq = 200 

    try:
        varoq_count = int(message.text)  # Assuming the user enters the number of varoqs
        total_cost = cost_per_varoq * varoq_count
        await message.answer(f"Umumiy narxi: {total_cost}")
    except ValueError:
        await message.answer("Varoq sonini raqam bilan kiriting.")

@dp.message(F.text == "Ortga")
async def ortga(message: types.Message):
    # Handle the "Ortga" button press
    kb = (
        [types.KeyboardButton(text="Rangli chop etish")],
        [types.KeyboardButton(text="Rangsiz chop etish")]
    )
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer("Bosh menu", reply_markup=keyboard)

@dp.message(F.text == "Rangsiz chop etish")
async def rangsiz(message: types.Message):
    ortga = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Ortga")]],
        resize_keyboard=True
    )
    await message.answer("Rangsiz printer uchun 200 sumdan hisoblanadi. Varoqlar sonini kiriting (faqat raqam kiriting): ", reply_markup=ortga)

async def main():
    bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())