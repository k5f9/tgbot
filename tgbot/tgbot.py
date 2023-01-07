import telebot
from telebot import types
import time
import random

# токен
token = ''
bot = telebot.TeleBot(token)

#назначение разных функций
@bot.message_handler(commands=['start'])
def butt(but):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("програмирование")
    item3 = types.KeyboardButton("спам")
    item4 = types.KeyboardButton("аватарка")
    item5 = types.KeyboardButton("сохранение")
    item6 = types.KeyboardButton("стоп бот")
    item7 = types.KeyboardButton("мой чат id")
    markup.add(item1, item3, item4, item5, item6, item7)
    bot.send_message(but.chat.id, "Привет, это бот богдашки")
    bot.send_message(but.chat.id, "выберай кнопочку<3", reply_markup=markup)

#по приколу сделал
@bot.message_handler(commands=['print'])
def mess(messenge):
    bot.send_message(messenge.chat.id, 'хахаха')


@bot.message_handler(commands=['clear'])
def miss(massenge):
    if massenge.chat.id == :
        path = 'save.txt'

        try:
            with open(path, 'r+') as f:
                f.truncate()
        except IOError:
            print('хз')

        bot.send_message(massenge.chat.id, "всё очищено!")

    else:
        bot.send_message(massenge.chat.id, "вам нельзя!")




#всё чудо происходит здесь)
@bot.message_handler(content_types='text')
def message_reply(message):

    if message.text == "мой чат id":
        chat = open('chatid.txt', 'a+')

        chatids = str(message.chat.id)
        chha = chatids + '\n'


        chat.write(str(message.from_user.first_name) + ' : ' + chha)
        bot.send_message(message.chat.id, "вот, держи: " + chatids)




    elif message.text == "стоп бот":
        if message.chat.id == 2136972038:
            bot.send_message(message.chat.id, "как скажете богдан")
            bot.stop_polling()
        else:
            bot.send_message(message.chat.id, "тебе нельзя!")

    if message.text == "сохранение":
        def saved(mess):
            messange_save = mess.text
            file = open('save.txt', 'a+')
            file.write(messange_save + '\n')
            file.close()
            mis = open('save.txt', 'r')
            while True:
                line = mis.readline()
                if not line:
                    break
                bot.send_message(message.chat.id, line.strip())
        sent = bot.reply_to(message, "напиши что нибудь(только на англ)")
        bot.register_next_step_handler(sent, saved)

    elif message.text == "програмирование":
        mark = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="c#", url='https://itproger.com/course/csharp')
        btn2 = types.InlineKeyboardButton(text="python", url='https://itproger.com/course/python')
        mark.add(btn1, btn2)
        bot.send_message(message.chat.id, "вот держи", reply_markup=mark)
    elif message.text == "спам":
        bot.send_message(message.chat.id, "лови)")
        for i in range(2000):
            time.sleep(0.1)
            bot.send_message(message.chat.id, "1000 - 7")
            

    elif message.text == "аватарка":
        i = random.randrange(0, 5)
        file1 = open('png1.jpg', 'rb')
        file2 = open('png2.jpg', 'rb')
        file3 = open('png3.jpg', 'rb')
        file4 = open('png4.jpg', 'rb')
        file5 = open('png5.jpg', 'rb')
        ava = [file1, file2, file3, file4, file5]
        bot.send_photo(message.chat.id, ava[i], "держи")





bot.polling(none_stop=True)