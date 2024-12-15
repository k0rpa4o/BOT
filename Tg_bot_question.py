import telebot
from telebot import TeleBot
from telegraph import Telegraph
import sqlite3
from telebot import types

API_TOKEN = '7531692531:AAGbqnlrnX9QANmepfbfUAwWJHaflDRRLc8'
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, start_text())


def start_text():

    text = ("Привет! Что тебя интерисует? \n"
            "1. Руководство Оператора\n"
            "2. У тебя какой то вопрос?\n"
            "Выбери предложеное из меню")
    return text


telegraph = Telegraph()

# Шаг 1: Создание аккаунта Telegraph (выполняется один раз)
telegraph.create_account(short_name='MyBot')


@bot.message_handler(commands=['operators_manual'])
def send_article(message):
    try:
        with open('html/Operators_Manual.html', 'r', encoding='utf-8') as file:
            html_content = file.read()

        response = telegraph.create_page(
            title="Руководство оператора",  # Заголовок статьи
            html_content=html_content  # Содержимое статьи
        )

        # Получаем ссылку на статью
        article_url = f"https://telegra.ph/{response['path']}"

        # Шаг 3: Отправляем ссылку пользователю
        bot.send_message(message.chat.id, f"Руководство оператора, краткая инструкция! Читайте её по ссылке: {article_url}")

    except FileNotFoundError:
        bot.send_message(message.chat.id, "Ошибка: Файл article.html не найден!")
    except Exception as e:
        bot.send_message(message.chat.id, f"Произошла ошибка: {e}")


@bot.message_handler(commands=['questions'])
def questions(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Как купить выбранный автомобиль?", callback_data="bay_car")
    btn2 = types.InlineKeyboardButton("Что мы за компания?", callback_data="company")
    btn3 = types.InlineKeyboardButton("Нету интерисующего вопроса.", callback_data="no_questions")
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)

    bot.send_message(message.chat.id, text="Какой вопрос вас беспокоит?", reply_markup=markup)


bot.polling(none_stop=True)