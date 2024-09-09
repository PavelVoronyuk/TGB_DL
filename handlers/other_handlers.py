from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import F, Router
from lexicon.lexicon import LEXICON_RU
from aiogram.filters import Command, CommandStart

router = Router()

button1 = KeyboardButton(text="Иди нахуй")
button2 = KeyboardButton(text="Прикольный фокус")

nahui_keyboard = ReplyKeyboardMarkup(keyboard=[[button1], [button2]],
                                      resize_keyboard=False, one_time_keyboard=True)

url_button = InlineKeyboardButton(text="Твой новый дом", url="https://ru.wikipedia.org/wiki/Бахмут")

inline_keyb = InlineKeyboardMarkup(inline_keyboard=[[url_button]])

@router.message(CommandStart())
async def process_start(message: Message):
    await message.answer(text=LEXICON_RU["/start"], reply_markup=nahui_keyboard)

@router.message(Command(commands=["help"]))
async def process_help(message: Message):
    await message.answer(text=LEXICON_RU["/help"])

@router.message(F.photo)
async def process_photo(message: Message):
    await message.answer_photo(message.photo[0].file_id)
    await message.answer(text=LEXICON_RU["photo_answ"])

@router.message(F.text == "Иди нахуй")
async def poslanie_obratno(message: Message):
    await message.answer(text="Сам иди чмо ссаное")
    fak_url = r"https://www.google.com/imgres?q=%D1%84%D0%B0%D0%BA&imgurl=https%3A%2F%2Femojio.ru%2Fimages%2Fapple-b%2F1f595.png&imgrefurl=https%3A%2F%2Femojio.ru%2Fsmileys-people%2Fd83ddd95-1f595-fakyu-sredniy-palets.html&docid=RCOuEwOt9tUeSM&tbnid=S7prBIdVKY-PZM&vet=12ahUKEwjU2eGAvsGGAxUySfEDHfxHBFwQM3oECEYQAA..i&w=160&h=160&hcb=2&ved=2ahUKEwjU2eGAvsGGAxUySfEDHfxHBFwQM3oECEYQAA"
    await message.reply_photo(photo=fak_url, caption="Не охуевай")

@router.message(F.text == "Прикольный фокус")
async def poslanie_obratno(message: Message):
    voenkom_url = r"https://n1s1.hsmedia.ru/ea/50/22/ea5022ec4bed45fd6606af35dd8e00ec/656x438_1:5723_c4f7bf563bb6c72a5017db30950f185a@1696x1130_0xQ7NVDhKJ_5740836382648465481.jpg.webp"
    await message.answer_photo(photo=voenkom_url)
    await message.answer(text="Ля ты петух твой номер уже в военкомате", reply_markup=inline_keyb)


@router.message()
async def baza_reply(message):
    await message.answer(text=LEXICON_RU["nahui"])