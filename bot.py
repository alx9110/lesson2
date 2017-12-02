""" Telegramm BOT """
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem
import datetime
import logging
import re
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                   )


def greet_user(bot, update):
    """ Cmd """
    logging.info('Hello /start')
    update.message.reply_text('Hello')

def planet_ephem(bot, update, args):
    """ Planet """
    date = datetime.datetime.now()
    now = date.strftime('%d/%m/%Y')
    user_text = args[0]
    planets = {'Марс': ephem.Mars(now),
               'Венера': ephem.Venus(now),
               'Юпитер': ephem.Jupiter(now),
               'Солнце': ephem.Sun(now),
               'Юпитер': ephem.Jupiter(now),
              }
    msg = ephem.constellation(planets[user_text.capitalize()])
    update.message.reply_text('{} в созвездии: '.format(user_text.capitalize()) + ' '.join(msg))

def talk_to_me(bot, update):
    """ Talk """
    user_text = update.message.text
    if user_text.endswith('='):
        operands = re.findall(r'\d+', user_text)
        operator = re.findall(r'[+,\-,*,/]', user_text)
        if len(operands) != 2:
            update.message.reply_text('Вы ввели не два числа!')
        result = 0
        if operator[0] == '+':
            result = float(operands[0]) + float(operands[-1])
        elif operator[0] == '-':
            result = float(operands[0]) - float(operands[-1])
        elif operator[0] == '*':
            result = float(operands[0]) * float(operands[-1])
        elif operator[0] == '/':
            try:
                result = float(operands[0]) / float(operands[-1])
            except ZeroDivisionError:
                result = 'На ноль делить нельзя!!!'
        update.message.reply_text('{0}'.format(str(result)))

    # Калькулятор со словами
    elif user_text.lower().startswith('сколько будет '):
        if len(user_text.split()) != 5:
            update.message.reply_text('Вы пропустили число или оператор')
        digit_binds = {'ноль': 0,
                       'один': 1,
                       'два': 2,
                       'три': 3,
                       'четыре': 4,
                       'пять': 5,
                       'шесть': 6,
                       'семь': 7,
                       'восемь': 8,
                       'девять': 9,
                      }
        cmd = user_text.split()
        operands = [digit_binds[cmd[2]], digit_binds[cmd[4]]]
        operator = cmd[3]
        if operator == 'минус':
            result = int(operands[0]) - int(operands[1])
            update.message.reply_text(str(result))
        elif operator == 'плюс':
            result = int(operands[0]) + int(operands[1])
            update.message.reply_text(str(result))
    else:
        logging.info(user_text)
        update.message.reply_text(user_text)

def word_count(bot, update, args):
    """ Word count """
    user_text = ' '.join(args)
    logging.info(user_text)
    if user_text.startswith('«') and user_text.endswith('»'):
        if user_text and user_text != '«»':
            update.message.reply_text('В предложении {} слова!'.format(len(args)))
    else:
        update.message.reply_text('Тест должен быть в кавычках')


def main():
    """ Updater """
    updater = Updater('375235291:AAE0bk2KG8p7FEFOw0WUY92Su-DRsJOIKcE')

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_ephem, pass_args=True))
    dp.add_handler(CommandHandler("words", word_count, pass_args=True))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    updater.start_polling()
    updater.idle()

main()
