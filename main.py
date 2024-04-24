from aiogram import Bot, Dispatcher, types, html, filters, utils, F
from config import BOT_API
import asyncio
from aiogram.utils.keyboard import   ReplyKeyboardBuilder,InlineKeyboardBuilder
import re


bot = Bot(BOT_API, parse_mode="HTML")
dp = Dispatcher()

@dp.message(filters.Command("start"))
async def start(message: types.Message):
    bldr = InlineKeyboardBuilder()
    #button_booking = types.InlineKeyboardButton(text="Book Time", url="https://www.youtube.com/")
    button_pricing = types.InlineKeyboardButton(text="Pricelist", callback_data="pricelist")
    button_login = types.InlineKeyboardButton(text="Log in", callback_data="login")
    button_reg = types.InlineKeyboardButton(text="Register", callback_data="register")
    
    bldr.row(button_reg)
    #bldr.row(button_booking)
    bldr.row(button_pricing)
    bldr.row(button_login)
    # keyboard = [
    #     [button_booking],
    #     [button_pricing],
    #     [button_login]
    # ]
    

    await message.answer(
        text="Thank you for using our bot,\n\n You can click\
pricelist button for up-to-date information\n\
Logged in users can also check their bonuses and reserve time.",
        reply_markup=bldr.as_markup()
    )

@dp.message(filters.Command("contact_administrator"))
async def start(message: types.Message):
    lst = [
        [
            types.KeyboardButton(text="Yes"),
            types.KeyboardButton(text="No")
        ]
    ]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard = lst,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="click"
    )
    await message.answer("Do you want our administrator to contact you?", reply_markup=keyboard)
@dp.message(F.text.lower() == "yes")
async def mda(message: types.Message):
    await message.answer("Our administrator will contact soon!")

@dp.callback_query(lambda query: query.data == "pricelist")
async def send_price(callback_query: types.CallbackQuery):
    await callback_query.message.answer_photo(types.FSInputFile("bot_bss.png"))

@dp.callback_query(lambda query: query.data == "register")
async def check(callback_query: types.CallbackQuery):
    
    await callback_query.message.answer("Please enter your phone number:")

@dp.callback_query(lambda query: query.data == "login")
async def check(callback_query: types.CallbackQuery):
    
    await callback_query.message.answer("Please enter your name:")
        
@dp.message(F.text.lower() == "lare humanoske")
async def pas(message: types.Message):
    
    bldr = InlineKeyboardBuilder()
    button_booking = types.InlineKeyboardButton(text="Book Time", url="https://www.fresha.com/a/krasota-hamburg-hamburg-zeughausmarkt-21-ju9odhzc/all-offer?menu=true&rwg_token=AAh05qY-OrI4ZqVFgk_wRkm82YS-785kILGmM0nRTZVf5WBNfNmAOL3QM2I8MViy3JB7LjsOib4wN9MsgNmZILsM4BzFBiyC-zV3At1i6tokwfKMqdNumt0%3D")
    button_pricing = types.InlineKeyboardButton(text="Pricelist", callback_data="pricelist")
    button_login = types.InlineKeyboardButton(text="Log in", callback_data="login")
    button_bonuses = types.InlineKeyboardButton(text="Bonuses", callback_data="bonus")
    
    bldr.row(button_booking)
    bldr.row(button_pricing)
    #bldr.row(button_login)
    bldr.row(button_bonuses)
    # keyboard = [
    #     [button_booking],
    #     [button_pricing],
    #     [button_login]
    # ]
    

    await message.answer(
        text="Thank you for using our bot, lare humanoske\n\n You can click\
pricelist button for up-to-date information\n\
Logged in users can also check their bonuses and reserve time.",
        reply_markup=bldr.as_markup()
    )

@dp.callback_query(lambda query: query.data == "bonus")
async def check(callback_query: types.CallbackQuery):
    
    await callback_query.message.answer("Dear lare humanoske, \nYou have 312 bonuses available for future use.\n\nBonus status: Silver 7%")


@dp.message()
async def valid_phone_handler(message: types.Message):
    # Regular expression pattern to match phone numbers consisting only of numbers and with length less than 9
        mes = message.text
        pattern = r'^\d{0,8}$'
        if(re.match(pattern, mes)):
            await message.answer("Thank you for registration, now you can log in")
        else:
            await message.answer("You can use the menu button on the bottom to navigate, if you have any further questions and would like a call back please use /contact_administrator.")
    # else:
    #     await message.answer("Invald Number")
        
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())