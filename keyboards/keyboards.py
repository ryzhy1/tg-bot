from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from aiogram.filters import Text
from aiogram.utils.keyboard import InlineKeyboardBuilder

builder = InlineKeyboardBuilder()
builder_two = InlineKeyboardBuilder()
builder_back = InlineKeyboardBuilder()

kb = builder.row(InlineKeyboardButton(text='#1', callback_data='number_one_pressed'),
                 InlineKeyboardButton(text='#2', callback_data='number_two_pressed'))

kb1 = builder_two.row(InlineKeyboardButton(text='#1', callback_data='bought_pressed'),
                      InlineKeyboardButton(text='#2', callback_data='not_buy_pressed'))
kb1 = builder_two.row(InlineKeyboardButton(text='в главное меню', callback_data='back_button_pressed'))
back_button = builder_back.row(InlineKeyboardButton(text='в главное меню', callback_data='back_button_pressed'))
