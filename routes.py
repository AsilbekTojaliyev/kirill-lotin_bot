from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from functions import kirilldan_lotinga, lotindan_kirillga, tekshir


router = Router()


@router.message(CommandStart())
async def start(mg: Message):
    await mg.reply(f"salom {mg.from_user.first_name}, bot kirilldan lotinga va lotindan kirillga o'tkazadi.")


@router.message(Command("/help"))
async def yordam(mg: Message):
    return mg.answer("/help - yordam buyrug'i\n/start - botni ishga tushirish")


@router.message()
async def kirill(mg: Message):
    check = tekshir(mg.text)
    if check == "Kirill":
        await mg.reply(kirilldan_lotinga(mg.text))
    elif check == "Lotin":
        await mg.reply(lotindan_kirillga(mg.text))
    else:
        await mg.reply("iltimos bir alifbodan foydalaning!!!")

