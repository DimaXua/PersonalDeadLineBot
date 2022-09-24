import time

import telebot
import config
import datetime
import random

bot = telebot.TeleBot(config.TokenBot)
chat_id = 565567440


def getday():
    dl = config.DeadLineDate.split('-')
    day = datetime.date(int(dl[0]), int(dl[1]), int(dl[2])) - datetime.date.today()
    return int(day.days)


def send_message():
    deadlineday = getday()
    if deadlineday > 0:
        bot.send_message(chat_id, config.DayMessage + str(deadlineday))
    elif deadlineday == 0:
        bot.send_message(chat_id, config.DeadLineZerro)
    else:
        bot.send_message(chat_id, config.DeadLineMinus + str(abs(deadlineday)))
    nmess = random.randrange(0, len(config.RandomMessage))
    bot.send_message(chat_id, config.RandomMessage[nmess])


@bot.message_handler(commands=['start'])
def start_message():
    bot.send_message(chat_id, config.StartMessage)
    send_message()


while True:
    hournow = datetime.datetime.now().hour
    minnow = datetime.datetime.now().minute
    hourconf = int(config.WriteTime[:2])
    minconf = int(config.WriteTime[3:])
    if hournow == hourconf:
        if minnow == minconf:
            print("print")
            send_message()
            time.sleep(90)
    time.sleep(10)