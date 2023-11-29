# curator5_Genvver
import telebot
bot = telebot.TeleBot('6755123696:AAFfhfQNRZbjYIMCQZKmu5acYI0dxxfzUbU')


@bot.message_handler(commands=['start'])
def main(message):
	bot.send_message(message.chat.id, 'Обычное сообщение', parse_mode='Markdown')


@bot.message_handler(commands=['fat'])
def main(message):
	bot.send_message(message.chat.id, '*Жирный* \n тонкий', parse_mode='Markdown')


@bot.message_handler(commands=['italic'])
def main(message):
	bot.send_message(message.chat.id, '_Курсивный_ \n текст', parse_mode='Markdown')


bot.infinity_polling()
