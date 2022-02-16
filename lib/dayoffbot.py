#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
from django_booking.credentials import BOT_TOKEN
from telebot import TeleBot, types

##### Здесь, просто наброски и варианты текстов.

hello_text = """ Привет, я помогу тебе подобрать место для отдыха на природе.
"""
search_type_text = """ Чтобы приступить к поиску выберите один из 3х вариантов поиска:
    1. Поиск по типу отдыха
    2. Поиск всех мест отдыха в определенном районе
"""
rest_types = ["Беседка", "Мангал", "Срака"]

marked_text = """
*bold \*text*
_italic \*text_
__underline__
~strikethrough~
||spoiler||
*bold _italic bold ~italic bold strikethrough ||italic bold strikethrough spoiler||~ __underline italic bold___ bold*
[Google_maps_link](http://www.example.com/)
[inline mention of a user](tg://user?id=123456789)
`inline fixed-width code`
```
pre-formatted fixed-width code block
```
```python
pre-formatted fixed-width code block written in the Python programming language
```
"""
places_view_template = """
*Название места отдыха*
_Локация_: Парк Отрадный
_Услуги_: Оренда мангала, оренда беседок
_Дополнительно_: `wifi`, `кальян`, `сральня` 
_Цены_: 400\-800 грн
_Телефон_: \+380730737373
[Подробнее]more\_info\_id\_этого\_места
"""


##### Здесь, просто наброски и варианты текстов.

def get_bot_instance(BOT_TOKEN):
    return TeleBot(BOT_TOKEN)


bot = get_bot_instance(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, hello_text)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, )
    button1 = types.KeyboardButton("Тип отдыха")
    button2 = types.KeyboardButton("Район")
    markup.add(button1)
    markup.add(button2)
    bot.send_message(message.chat.id, search_type_text, reply_markup=markup)


@bot.message_handler(content_types=['text'])
def search_by_type_or_district(message):
    if message.text == "Тип отдыха":
        bot.send_message(message.chat.id, "Что именно вы ищите?", reply_markup=button_binder(rest_types))
    if message.text == "Район":
        bot.send_message(message.chat.id, places_view_template, reply_markup=button_binder(rest_types),
                         parse_mode="MarkdownV2")


def button_binder(button_list: list):
    buttons_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, )
    buttons_pool = [types.KeyboardButton(name) for name in button_list]
    for button in buttons_pool:
        buttons_markup.add(button)
    return buttons_markup


def run():
    bot.polling()


if __name__ == '__main__':
    run()
