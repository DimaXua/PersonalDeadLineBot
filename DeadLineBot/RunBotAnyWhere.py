import telebot
import config
import datetime
import random

bot = telebot.TeleBot(config.TokenBot)
chat_id = 565567440


def get_day():
    dl = config.DeadLineDate.split('-')
    day = datetime.date(int(dl[0]), int(dl[1]), int(dl[2])) - datetime.date.today()
    return int(day.days)


def send_message():
    deadlineday = get_day()
    if deadlineday > 0:
        bot.send_message(chat_id, f"{config.DayMessage} <b>{str(deadlineday)}</b>", parse_mode="html")
    elif deadlineday == 0:
        bot.send_message(chat_id, config.DeadLineZerro)
    else:
        bot.send_message(chat_id, config.DeadLineMinus + str(abs(deadlineday)))
    nmess = random.randrange(0, len(config.RandomMessage))
    bot.send_message(chat_id, f"<i>{config.RandomMessage[nmess]}</i>", parse_mode="html")


send_message()
