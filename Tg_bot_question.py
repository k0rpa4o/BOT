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


@bot.callback_query_handler(func=lambda call: call.data in ["bay_car", "company", "no_questions"])
def callback_query_handler(call):
    if call.data == "bay_car":
        text = ("Для того чтобы купить у нас автомобиль, во-первых вы должны быть зарегестрированы у нас в боте!"
                "Далее выбранный автомобиль добавьте в избранное, после зайдите в сови избранное и там под автомобилем будет кнопка"
                "Купить, нажимаете на эту кнопку и после в течении часа вам придет уведомление о том в какое время автомобидь будет доставлен на ваш адрес "
                "который был указан  при регистрации.\n"
                "Далее после осмотра автомобиля вы можете совершить оплату нашему сотруднику который доставит вам ваш автомобиль!")
        bot.send_message(call.message.chat.id, text=text)

    elif call.data == "company":
        text =( "**Основание автосалона 'Хуябаса' (意味: Быстрый порыв, стремительный рывок)**"
                "Компания 'Хуябаса' была основана с целью воплощения японского подхода к скорости, качеству и надежности в автомобильной сфере. "
                "Название автосалона переводится как стремительный порыв, что отражает нашу философию — помогать каждому клиенту сделать уверенный шаг к своей мечте."
                "Наша история началась с вдохновения японской культурой, которая сочетает в себе технологии, уважение к традициям и внимание к мельчайшим деталям."
                "Мы не просто продаем автомобили, а создаем пространство, где каждый клиент может почувствовать заботу, профессионализм и комфорт."
                " Наша миссия — ускорить ваш путь к свободе и новым горизонтам."  
                "Добро пожаловать в автосалон 'Хуябаса' — там, где скорость и совершенство встречаются с вашей мечтой!")
        bot.send_message(call.message.chat.id, text=text)

    elif call.data == "no_questions":
        text = ("Обратитесь к нашему администратору\n"
                "Егор Олегович\n"
                "@idhxjsnd")
        bot.send_message(call.message.chat.id, text=text)


bot.polling(none_stop=True)