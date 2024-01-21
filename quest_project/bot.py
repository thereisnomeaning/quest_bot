import telebot
import json


from images import *
from additional_functions import *


token = '6597024761:AAFf12jYsWuCuZ7H8TO89eVx5WYmKb2ei2M'

bot = telebot.TeleBot(token=token)


with open('quest_plot.json', 'r', encoding='utf-8') as file:
    quest_plot = json.load(file)


with open('user_data.json', 'r') as file:
    try:
        user_data = json.load(file)
    except:
        user_data = {}


@bot.message_handler(commands=['start'])
def start(message):

    user_id = message.from_user.id
    start_text = starting_text
    user_data[user_id] = {}
    user_data[user_id]['current_location'] = 'beginning' # Мы смотрим, где наш пользователь остановился.
    bot.send_message(message.chat.id, text=start_text)

    markup = start_quest_markup(list(quest_plot['beginning']['options']))
    caption = quest_plot['beginning']['description']
    photo = images['image1']
    bot.send_photo(message.chat.id, photo, caption=caption, reply_markup=markup)

    with open('user_data.json', 'w') as file:
        json.dump(user_data, file)


@bot.message_handler(commands=['help'])
def helper(message):
    text = help_text
    bot.send_message(message.chat.id, text=text)


@bot.message_handler()
def quest(message):
    user_id = message.from_user.id
    current_location = user_data[user_id]['current_location']
    user_options = list(quest_plot[current_location]['options'])

    if message.text in user_options:

        user_data[user_id]['current_location'] = quest_plot[current_location]['options'][message.text]
        current_location = user_data[user_id]['current_location']
        photo = images[quest_plot[current_location]['image']]
        caption = quest_plot[current_location]['description']

        if current_location.startswith(('defeat', 'victory')):

            # Значит, что наша пользователь либо победил, либо проиграл и клавиатура нам больше не нужна.
            markup = types.ReplyKeyboardRemove()
        else:
            markup = quest_markup(list(quest_plot[user_data[user_id]['current_location']]['options']))

        bot.send_photo(message.chat.id, photo, caption=caption, reply_markup=markup)

    else:
        bot.send_message(message.chat.id, 'Вы отклонились от курса, выберите один из предложенных вариантов внизу')

    with open('user_data.json', 'w') as file:
        json.dump(user_data, file)


bot.polling()