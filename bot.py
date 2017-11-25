""" Telegramm BOT """
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem
import datetime
import logging
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
    # EllipticalBody
    # HyperbolicBody
    # Jupiter
    # Mars
    # Mercury
    # Moon
    # Neptune
    # ParabolicBody
    # Pluto
    # Saturn
    # Sun
    # Uranus
    # Venus
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
    logging.info(user_text)
    update.message.reply_text(user_text)

def main():
    """ Updater """
    updater = Updater('375235291:AAE0bk2KG8p7FEFOw0WUY92Su-DRsJOIKcE')

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_ephem, pass_args=True))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    updater.start_polling()
    updater.idle()

main()
