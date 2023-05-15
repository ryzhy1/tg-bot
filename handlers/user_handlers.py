from aiogram import Router
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import Message
from keyboards.keyboards import kb, kb1, back_button
from lexicon.lexicon import LEXICON_RU
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery

router: Router = Router()

command_dict = {"clothes": False,
                "shoes": False}


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=kb.as_markup(resize_keyboard=True), parse_mode='HTML')


@router.callback_query(Text(text='number_one_pressed'))
async def information(callback: CallbackQuery):
    command_dict["shoes"] = True
    await callback.message.edit_text(text=LEXICON_RU['number one'], reply_markup=back_button.as_markup(resize_keyboard=True),
                                     parse_mode='HTML')
    await callback.answer()


@router.callback_query(Text(text='number_two_pressed'))
async def consultation(callback: CallbackQuery):
    await callback.message.edit_text(text=LEXICON_RU['number two'], reply_markup=kb1.as_markup(resize_keyboard=True),
                                     parse_mode='HTML')
    await callback.answer()


@router.callback_query(Text(text='bought_pressed'))
async def from_panteric(callback: CallbackQuery):
    await callback.message.edit_text(text=LEXICON_RU['from panteric'], reply_markup=back_button.as_markup(resize_keyboard=True),
                                     parse_mode='HTML')
    await callback.answer()


@router.callback_query(Text(text='not_buy_pressed'))
async def not_from_panteric(callback: CallbackQuery):
    await callback.message.edit_text(text=LEXICON_RU['not from panteric'],
                                     reply_markup=back_button.as_markup(resize_keyboard=True),
                                     parse_mode='HTML')
    await callback.answer()

@router.callback_query(Text(text='back_button_pressed'))
async def back(callback:CallbackQuery):
    await callback.message.edit_text(text=LEXICON_RU['/start'], reply_markup=kb.as_markup(resize_keyboard=True),
                                     parse_mode='HTML')
    await callback.answer()


@router.callback_query(Text(text=['number_two_pressed', 'number_one_pressed', 'bought_pressed , not_buy_pressed','back_button_pressed' ]))
async def callbacks(callback: CallbackQuery):
    await callback.answer()
