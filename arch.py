from config import TOKEN
import telebot
from logic import varian_game
import psycopg2

conn = psycopg2.connect(dbname='guest_results', user='new_guest', password='my', host='localhost', port=5432)
cursor = conn.cursor()
conn.autocommit = True

bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def start_game(message):
    game = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = telebot.types.KeyboardButton("Камень")
    b2 = telebot.types.KeyboardButton("Ножницы")
    b3 = telebot.types.KeyboardButton("Бумага")
    game.add(b1, b2, b3)
    bot.send_message(message.chat.id, f"Привет {message.from_user.first_name}.\nДавай поиграем в камень-ножницы-бумага!",reply_markup=game)

@bot.message_handler(content_types=['text'])
def game(message):
    if message.chat.type == 'private':
        if message.text == 'Камень':
            result = varian_game(1)
            bot.send_message(message.chat.id, result)
            cursor.execute(f"insert into results(result) values('{result}')")
        elif message.text == 'Ножницы':
            result = varian_game(2)
            bot.send_message(message.chat.id, result)
            cursor.execute(f"insert into results(result) values('{result}')")
        elif message.text == 'Бумага':
            result = varian_game(3)
            bot.send_message(message.chat.id, result)
            cursor.execute(f"insert into results(result) values('{result}')")
        else:
            bot.send_message(message.chat.id, "Ошибка")

bot.polling(non_stop=True)