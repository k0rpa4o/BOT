import telebot
import sqlite3
from telebot import types

API_TOKEN = '6468230239:AAGsYFJLgppd62hDduN1WmtDSy2ELx9v2hg'
bot = telebot.TeleBot(API_TOKEN)

conn = sqlite3.connect('db/AUTO.db', check_same_thread=False)
cursor = conn.cursor()


def db_table_val_user(FIO: str, number: str, age: int, gmail: str, adress: str, tg_id: int):
    cursor.execute('INSERT INTO USER (FIO, number, age, gmail, adress, tg_id) VALUES (?, ?, ?, ?, ?, ?)',
                   (FIO, number, age, gmail, adress, tg_id))
    conn.commit()


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, start_text())


def start_text():
    text = ("Привет! Предлагаю тебе зарегестрироваться, инчаче если ты выберешь себе автомобиль наши сотрудник не смогут с тобой связаться!\n"
            "Ну а пока можешь выбрать то что тебя интерисуе из списка меню!\n")
    return text


def next():
    text = ("Привет вот что я могу: \n"
            "/technical_support - @SIR_help_cr24_bot\n"
            "/car_catalog - Каталог автомобилей\n"
            )
    return text


def registration_text():
    text = ("Чтобы зарегистрироваться, отправьте сообщение по типу:\n"
            "ФИО\n"
            "Номер телефона\n"
            "Возраст\n"
            "Почта\n"
            "Адрес проживания\n\n"
            "Пример:\n"
            "Иванов Иван Иванович\n"
            "8 925 212 32 07\n"
            "31\n"
            "ivanov@gmail.com\n"
            "Россия, Мытищи, 5-ый Щелковский пр. д.7 к.2 кв 218\n")
    return text


# Техническая поддержка
@bot.message_handler(commands=['technical_support'])
def technical_support(message):
    bot.send_message(message.chat.id, "@SIR_help_cr24_bot")


@bot.message_handler(commands=['car_catalog'])
def car_catalog_handler(message):
    cursor.execute("SELECT FIO FROM USER WHERE tg_id = ?", (message.from_user.id,))
    user_name = cursor.fetchone()

    if user_name:
        user_name = user_name[0]
    else:
        user_name = "Гость"

    # Создаём Inline клавиатуру
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Америка 🇺🇸", callback_data="america")
    btn2 = types.InlineKeyboardButton("Германия 🇩🇪", callback_data="germany")
    markup.add(btn1, btn2)

    # Отправляем сообщение
    bot.send_message(
        message.chat.id,
        text=f"Привет, {user_name}! Из какой страны ты хочешь себе машину?\n"
             "Из Америки такие как Ford, Dodge, Chevrolet\n"
             "Из Германии такие как BMW, Mercedes, Porsche",
        reply_markup=markup
    )


@bot.callback_query_handler(func=lambda call: call.data in ["america", "germany", "back_to_menu", "ford", "dodge", "chevrolet", "bmw", "mercedes", "porsche"])
def callback_query_handler(call):
    if call.data == "america":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("Ford", callback_data="ford")
        btn2 = types.InlineKeyboardButton("Dodge", callback_data="dodge")
        btn3 = types.InlineKeyboardButton("Chevrolet", callback_data="chevrolet")
        back = types.InlineKeyboardButton("Вернуться назад", callback_data="back_to_menu")
        markup.add(btn1, btn2, btn3)
        markup.add(back)
        bot.send_message(call.message.chat.id, text="Выберите марку машины:", reply_markup=markup)

    elif call.data == "germany":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("BMW", callback_data="bmw")
        btn2 = types.InlineKeyboardButton("Mercedes", callback_data="mercedes")
        btn3 = types.InlineKeyboardButton("Porsche", callback_data="porsche")
        back = types.InlineKeyboardButton("Вернуться назад", callback_data="back_to_menu")
        markup.add(btn1, btn2, btn3)
        markup.add(back)
        bot.send_message(call.message.chat.id, text="Выберите марку машины:", reply_markup=markup)

    elif call.data == "back_to_menu":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("Америка 🇺🇸", callback_data="america")
        btn2 = types.InlineKeyboardButton("Германия 🇩🇪", callback_data="germany")
        markup.add(btn1, btn2)
        bot.send_message(call.message.chat.id, text="Из какой страны вы хотите выбрать машину?", reply_markup=markup)

    elif call.data == "bmw":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("Добавить в избранное ❤", callback_data="like")
        btn2 = types.InlineKeyboardButton("Вернуться назад", callback_data="back_to_menu")
        markup.add(btn1)
        markup.add(btn2)
        cursor.execute('SELECT link FROM BMW')
        photos = cursor.fetchall()
        cursor.execute('SELECT * FROM BMW')
        rows = cursor.fetchall()
        if len(photos) != len(rows):
            bot.send_message(call.message.chat.id, "Ошибка: количество фотографий не совпадает с количеством строк данных.")
            return
        for row, photo in zip(rows, photos):
            caption = (
                f"id: {row[0]}\n"
                f"Марка: {row[1]}"
                f"Модель: {row[2]}"
                f"Год: {row[3]}\n"
                f"Л.с: {row[4]}\n"
                f"Литры: {row[5]}\n"
                f"Коробка: {row[6]}"
                f"Привод: {row[7]}"
                f"Цвет: {row[8]}"
                f"Страна: {row[9]}"
                f"Цена: {row[10]}"
            )
            photo_url = photo[0]
            bot.send_photo(chat_id=call.message.chat.id, photo=photo_url, caption=caption, reply_markup=markup)

    elif call.data == "mercedes":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("Добавить в избранное ❤", callback_data="like")
        btn2 = types.InlineKeyboardButton("Вернуться назад", callback_data="back_to_menu")
        markup.add(btn1)
        markup.add(btn2)
        cursor.execute('SELECT link FROM MERCEDES')
        photos = cursor.fetchall()
        cursor.execute('SELECT * FROM MERCEDES')
        rows = cursor.fetchall()
        if len(photos) != len(rows):
            bot.send_message(call.message.chat.id, "Ошибка: количество фотографий не совпадает с количеством строк данных.")
            return
        for row, photo in zip(rows, photos):
            caption = (
                f"id: {row[0]}\n"
                f"Марка: {row[1]}"
                f"Модель: {row[2]}"
                f"Год: {row[3]}\n"
                f"Л.с: {row[4]}\n"
                f"Литры: {row[5]}\n"
                f"Коробка: {row[6]}"
                f"Привод: {row[7]}"
                f"Цвет: {row[8]}"
                f"Страна: {row[9]}"
                f"Цена: {row[10]}"
            )
            photo_url = photo[0]
            bot.send_photo(chat_id=call.message.chat.id, photo=photo_url, caption=caption, reply_markup=markup)

    elif call.data == "porsche":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("Добавить в избранное ❤", callback_data="like")
        btn2 = types.InlineKeyboardButton("Вернуться назад", callback_data="back_to_menu")
        markup.add(btn1)
        markup.add(btn2)
        cursor.execute('SELECT link FROM PORSCHE')
        photos = cursor.fetchall()
        cursor.execute('SELECT * FROM PORSCHE')
        rows = cursor.fetchall()
        if len(photos) != len(rows):
            bot.send_message(call.message.chat.id, "Ошибка: количество фотографий не совпадает с количеством строк данных.")
            return
        for row, photo in zip(rows, photos):
            caption = (
                f"id: {row[0]}\n"
                f"Марка: {row[1]}"
                f"Модель: {row[2]}"
                f"Год: {row[3]}\n"
                f"Л.с: {row[4]}\n"
                f"Литры: {row[5]}\n"
                f"Коробка: {row[6]}"
                f"Привод: {row[7]}"
                f"Цвет: {row[8]}"
                f"Страна: {row[9]}"
                f"Цена: {row[10]}"
            )
            photo_url = photo[0]
            bot.send_photo(chat_id=call.message.chat.id, photo=photo_url, caption=caption, reply_markup=markup)

    elif call.data == "ford":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("Добавить в избранное ❤", callback_data="like")
        btn2 = types.InlineKeyboardButton("Вернуться назад", callback_data="back_to_menu")
        markup.add(btn1)
        markup.add(btn2)
        cursor.execute('SELECT link FROM FORD')
        photos = cursor.fetchall()
        cursor.execute('SELECT * FROM FORD')
        rows = cursor.fetchall()
        if len(photos) != len(rows):
            bot.send_message(call.message.chat.id, "Ошибка: количество фотографий не совпадает с количеством строк данных.")
            return
        for row, photo in zip(rows, photos):
            caption = (
                f"id: {row[0]}\n"
                f"Марка: {row[1]}"
                f"Модель: {row[2]}"
                f"Год: {row[3]}\n"
                f"Л.с: {row[4]}\n"
                f"Литры: {row[5]}\n"
                f"Коробка: {row[6]}"
                f"Привод: {row[7]}"
                f"Цвет: {row[8]}"
                f"Страна: {row[9]}"
                f"Цена: {row[10]}"
            )
            photo_url = photo[0]
            bot.send_photo(chat_id=call.message.chat.id, photo=photo_url, caption=caption, reply_markup=markup)

    elif call.data == "dodge":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("Добавить в избранное ❤", callback_data="like")
        btn2 = types.InlineKeyboardButton("Вернуться назад", callback_data="back_to_menu")
        markup.add(btn1)
        markup.add(btn2)
        cursor.execute('SELECT link FROM DODGE')
        photos = cursor.fetchall()
        cursor.execute('SELECT * FROM DODGE')
        rows = cursor.fetchall()
        if len(photos) != len(rows):
            bot.send_message(call.message.chat.id, "Ошибка: количество фотографий не совпадает с количеством строк данных.")
            return
        for row, photo in zip(rows, photos):
            caption = (
                f"id: {row[0]}\n"
                f"Марка: {row[1]}"
                f"Модель: {row[2]}"
                f"Год: {row[3]}\n"
                f"Л.с: {row[4]}\n"
                f"Литры: {row[5]}\n"
                f"Коробка: {row[6]}"
                f"Привод: {row[7]}"
                f"Цвет: {row[8]}"
                f"Страна: {row[9]}"
                f"Цена: {row[10]}"
            )
            photo_url = photo[0]
            bot.send_photo(chat_id=call.message.chat.id, photo=photo_url, caption=caption, reply_markup=markup)

    elif call.data == "chevrolet":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("Добавить в избранное ❤", callback_data="like")
        btn2 = types.InlineKeyboardButton("Вернуться назад", callback_data="back_to_menu")
        markup.add(btn1)
        markup.add(btn2)
        cursor.execute('SELECT link FROM CHEVROLET')
        photos = cursor.fetchall()
        cursor.execute('SELECT * FROM CHEVROLET')
        rows = cursor.fetchall()
        if len(photos) != len(rows):
            bot.send_message(call.message.chat.id, "Ошибка: количество фотографий не совпадает с количеством строк данных.")
            return
        for row, photo in zip(rows, photos):
            caption = (
                f"id: {row[0]}\n"
                f"Марка: {row[1]}"
                f"Модель: {row[2]}"
                f"Год: {row[3]}\n"
                f"Л.с: {row[4]}\n"
                f"Литры: {row[5]}\n"
                f"Коробка: {row[6]}"
                f"Привод: {row[7]}"
                f"Цвет: {row[8]}"
                f"Страна: {row[9]}"
                f"Цена: {row[10]}"
            )
            photo_url = photo[0]
            bot.send_photo(chat_id=call.message.chat.id, photo=photo_url, caption=caption, reply_markup=markup)


@bot.message_handler(commands=['registration'])
def registration_handler(message):
    bot.send_message(message.chat.id, registration_text())
    bot.register_next_step_handler(message, process_registration)


def process_registration(message):
    user_id = message.from_user.id
    try:
        lines = message.text.split('\n')
        if len(lines) < 5:
            bot.send_message(message.chat.id, "Ошибка! Проверьте формат данных.")
            return

        FIO_text = lines[0]
        number_text = lines[1]
        age_text = int(lines[2])
        gmail_text = lines[3]
        adress_text = lines[4]

        # Сохранение в БД
        db_table_val_user(FIO=FIO_text, number=number_text, age=age_text, gmail=gmail_text, adress=adress_text, tg_id=user_id)

        bot.send_message(message.chat.id, "Вы успешно зарегистрировались!\n"
                                          "/technical_support - Техническая поддержка\n"
                                          "/car_catalog - Каталог автомобилей")
    except Exception as e:
        bot.send_message(message.chat.id, f"Ошибка! Проверьте формат данных. Подробнее: {e}")


# Логика для выбора машин
#@bot.message_handler(content_types=['text'])
#pass


bot.polling(none_stop=True)
