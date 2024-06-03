import telebot
import sqlite3
import codecs
import io
from telebot import types


API_TOKEN = '6468230239:AAGsYFJLgppd62hDduN1WmtDSy2ELx9v2hg'
bot = telebot.TeleBot(API_TOKEN)

conn = sqlite3.connect('db/AUTO.db', check_same_thread=False)
cursor = conn.cursor()


def db_table_val_user(FIO: str, number: str, age: int, gmail: str, adress: str):
    cursor.execute('INSERT INTO USER (FIO, number, age, gmail, adress) VALUES (?,?,?,?,?)', (FIO, number, age, gmail, adress, ))
    conn.commit()


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, start_text())


def start_text():

    text = ("Привет вот что я могу: \n"
            "/technical_support - Техническая поддержка\n"
            "/car_catalog - Каталог автомобилей\n"
            "/registration - Регистрация")
    return text


def registration_text():
    text = ("Что бы зарегистрироваться вам надо отправить сообщение по типу:\n"
            "ФИО\n"
            "Номер телефона\n"
            "Возраст\n"
            "Почта\n"
            "Адресс проживания\n\n\n"
            "пример:\n"
            "Иванов Иван Иванович\n"
            "8 925 212 32 07\n"
            "31\n"
            "ivanov@gmail.com\n"
            "Россия, Мытищи, 1-ый Щелковский пр. д.11 к.1 кв 11\n")

    return text


def bmw():
    cursor.execute('SELECT * FROM BMW')
    data = cursor.fetchall()
    # Запись данных в файл
    with open('txt\BMW\BMW.txt', 'w', encoding='utf-8', newline='') as file:
        for row in data:
            file.write('\n'.join(map(str, row)) + '\n')
    file.close()

    with open('txt\BMW\BMW.txt') as f:
        lines = f.readlines()
        non_empty_lines = (line for line in lines if not line.isspace())
    with open('txt\BMW\BMW_new.txt', 'w') as n_f:
        n_f.writelines(non_empty_lines)

    with open('txt\BMW\BMW_new.txt', 'r', encoding='utf-8', newline='') as file:
        data = file.read()

    lines = data.strip().split("\n")

    new_data = ""
    for i in range(1, len(lines), 11):
        new_data += "Марка: " + lines[i] + ""
        new_data += "Модель: " + lines[i + 1] + ""
        new_data += "Год: " + lines[i + 2] + ""
        new_data += "Л.c: " + lines[i + 3] + ""
        new_data += "Литры: " + lines[i + 4] + ""
        new_data += "Коробка передач: " + lines[i + 5] + ""
        new_data += "Привод: " + lines[i + 6] + ""
        new_data += "Цвет: " + lines[i + 7] + ""
        new_data += "Страна производства: " + lines[i + 8] + ""
        new_data += "Цена: " + lines[i + 9] + "\n"

    #print(new_data)
    with open("txt\BMW\BMW_new_new.txt", "w") as file:
        file.write(new_data)

    file = open("txt\BMW\BMW_new_new.txt")
    return file.read()


def mercedes():
    cursor.execute('SELECT * FROM MERCEDES')
    data = cursor.fetchall()
    # Запись данных в файл
    with open('txt\Mercedes\Mercedes.txt', 'w', encoding='utf-8', newline='') as file:
        for row in data:
            file.write('\n'.join(map(str, row)) + '\n')
    file.close()

    with open('txt\Mercedes\Mercedes.txt') as f:
        lines = f.readlines()
        non_empty_lines = (line for line in lines if not line.isspace())
    with open('txt\Mercedes\Mercedes_new.txt', 'w') as n_f:
        n_f.writelines(non_empty_lines)

    with open('txt\Mercedes\Mercedes_new.txt', 'r', encoding='utf-8', newline='') as file:
        data = file.read()

    lines = data.strip().split("\n")

    new_data = ""
    for i in range(1, len(lines), 11):
        new_data += "Марка: " + lines[i] + ""
        new_data += "Модель: " + lines[i + 1] + ""
        new_data += "Год: " + lines[i + 2] + ""
        new_data += "Л.c: " + lines[i + 3] + ""
        new_data += "Литры: " + lines[i + 4] + ""
        new_data += "Коробка передач: " + lines[i + 5] + ""
        new_data += "Привод: " + lines[i + 6] + ""
        new_data += "Цвет: " + lines[i + 7] + ""
        new_data += "Страна производства: " + lines[i + 8] + ""
        new_data += "Цена: " + lines[i + 9] + "\n"

    #print(new_data)
    with open("txt\Mercedes\Mercedes_new_new.txt", "w") as file:
        file.write(new_data)

    file = open("txt\Mercedes\Mercedes_new_new.txt")
    return file.read()


def porsche():
    cursor.execute('SELECT * FROM PORSCHE')
    data = cursor.fetchall()
    # Запись данных в файл
    with open('txt\Porsche\Porsche.txt', 'w', encoding='utf-8', newline='', errors='ignore') as file:
        for row in data:
            file.write('\n'.join(map(str, row)) + '\n')
    file.close()

    with open('txt\Porsche\Porsche.txt', errors='ignore') as f:
        lines = f.readlines()
        non_empty_lines = (line for line in lines if not line.isspace())
    with open('txt\Porsche\Porsche_new.txt', 'w', errors='ignore') as n_f:
        n_f.writelines(non_empty_lines)

    with open('txt\Porsche\Porsche_new.txt', 'r', encoding='utf-8', newline='', errors='ignore') as file:
        data = file.read()

    lines = data.strip().split("\n")

    new_data = ""
    for i in range(1, len(lines), 11):
        new_data += "Марка: " + lines[i] + ""
        new_data += "Модель: " + lines[i + 1] + ""
        new_data += "Год: " + lines[i + 2] + ""
        new_data += "Л.c: " + lines[i + 3] + ""
        new_data += "Литры: " + lines[i + 4] + ""
        new_data += "Коробка передач: " + lines[i + 5] + ""
        new_data += "Привод: " + lines[i + 6] + ""
        new_data += "Цвет: " + lines[i + 7] + ""
        new_data += "Страна производства: " + lines[i + 8] + ""
        new_data += "Цена: " + lines[i + 9] + "\n"

    #print(new_data)
    with open("txt\Porsche\Porsche_new_new.txt", "w") as file:
        file.write(new_data)

    file = open("txt\Porsche\Porsche_new_new.txt")
    return file.read()


def ford():
    cursor.execute('SELECT * FROM FORD')
    data = cursor.fetchall()
    # Запись данных в файл
    with open('txt\Ford\Ford.txt', 'w', encoding='utf-8', newline='', errors='ignore') as file:
        for row in data:
            file.write('\n'.join(map(str, row)) + '\n')
    file.close()

    with open('txt\Ford\Ford.txt', errors='ignore') as f:
        lines = f.readlines()
        non_empty_lines = (line for line in lines if not line.isspace())
    with open('txt\Ford\Ford_new.txt', 'w', errors='ignore') as n_f:
        n_f.writelines(non_empty_lines)

    with open('txt\Ford\Ford_new.txt', 'r', encoding='utf-8', newline='', errors='ignore') as file:
        data = file.read()

    lines = data.strip().split("\n")

    new_data = ""
    for i in range(1, len(lines), 11):
        new_data += "Марка: " + lines[i] + ""
        new_data += "Модель: " + lines[i + 1] + ""
        new_data += "Год: " + lines[i + 2] + ""
        new_data += "Л.c: " + lines[i + 3] + ""
        new_data += "Литры: " + lines[i + 4] + ""
        new_data += "Коробка передач: " + lines[i + 5] + ""
        new_data += "Привод: " + lines[i + 6] + ""
        new_data += "Цвет: " + lines[i + 7] + ""
        new_data += "Страна производства: " + lines[i + 8] + ""
        new_data += "Цена: " + lines[i + 9] + "\n"

    #print(new_data)
    with open("txt\Ford\Ford_new_new.txt", "w") as file:
        file.write(new_data)

    file = open("txt\Ford\Ford_new_new.txt")
    return file.read()


def dodge():
    cursor.execute('SELECT * FROM DODGE')
    data = cursor.fetchall()
    # Запись данных в файл
    with open('txt\Dodge\Dodge.txt', 'w', encoding='utf-8', newline='', errors='ignore') as file:
        for row in data:
            file.write('\n'.join(map(str, row)) + '\n')
    file.close()

    with open('txt\Dodge\Dodge.txt', errors='ignore') as f:
        lines = f.readlines()
        non_empty_lines = (line for line in lines if not line.isspace())
    with open('txt\Dodge\Dodge_new.txt', 'w', errors='ignore') as n_f:
        n_f.writelines(non_empty_lines)

    with open('txt\Dodge\Dodge_new.txt', 'r', encoding='utf-8', newline='', errors='ignore') as file:
        data = file.read()

    lines = data.strip().split("\n")

    new_data = ""
    for i in range(1, len(lines), 11):
        new_data += "Марка: " + lines[i] + ""
        new_data += "Модель: " + lines[i + 1] + ""
        new_data += "Год: " + lines[i + 2] + ""
        new_data += "Л.c: " + lines[i + 3] + ""
        new_data += "Литры: " + lines[i + 4] + ""
        new_data += "Коробка передач: " + lines[i + 5] + ""
        new_data += "Привод: " + lines[i + 6] + ""
        new_data += "Цвет: " + lines[i + 7] + ""
        new_data += "Страна производства: " + lines[i + 8] + ""
        new_data += "Цена: " + lines[i + 9] + "\n"

    #print(new_data)
    with open("txt\Dodge\Dodge_new_new.txt", "w") as file:
        file.write(new_data)

    file = open("txt\Dodge\Dodge_new_new.txt")
    return file.read()


def chevrolet():
    cursor.execute('SELECT * FROM CHEVROLET')
    data = cursor.fetchall()
    # Запись данных в файл
    with open('txt\Chevrolet\Chevrolet.txt', 'w', encoding='utf-8', newline='', errors='ignore') as file:
        for row in data:
            file.write('\n'.join(map(str, row)) + '\n')
    file.close()

    with open('txt\Chevrolet\Chevrolet.txt', errors='ignore') as f:
        lines = f.readlines()
        non_empty_lines = (line for line in lines if not line.isspace())
    with open('txt\Chevrolet\Chevrolet_new.txt', 'w', errors='ignore') as n_f:
        n_f.writelines(non_empty_lines)

    with open('txt\Chevrolet\Chevrolet_new.txt', 'r', encoding='utf-8', newline='', errors='ignore') as file:
        data = file.read()

    lines = data.strip().split("\n")

    new_data = ""
    for i in range(1, len(lines), 11):
        new_data += "Марка: " + lines[i] + ""
        new_data += "Модель: " + lines[i + 1] + ""
        new_data += "Год: " + lines[i + 2] + ""
        new_data += "Л.c: " + lines[i + 3] + ""
        new_data += "Литры: " + lines[i + 4] + ""
        new_data += "Коробка передач: " + lines[i + 5] + ""
        new_data += "Привод: " + lines[i + 6] + ""
        new_data += "Цвет: " + lines[i + 7] + ""
        new_data += "Страна производства: " + lines[i + 8] + ""
        new_data += "Цена: " + lines[i + 9] + "\n"

    #print(new_data)
    with open("txt\Chevrolet\Chevrolet_new_new.txt", "w") as file:
        file.write(new_data)

    file = open("txt\Chevrolet\Chevrolet_new_new.txt")
    return file.read()


def car_text():
    cursor.execute('SELECT * FROM CAR')
    data = cursor.fetchall()
    # Запись данных в файл
    with open('txt\print_car.txt', 'w', encoding='utf-8', newline='') as file:
        for row in data:
            file.write('\n'.join(map(str, row)) + '\n')
    file.close()

    with open('txt\print_car.txt') as f:
        lines = f.readlines()
        non_empty_lines = (line for line in lines if not line.isspace())
    with open('txt\print_car_new.txt', 'w') as n_f:
        n_f.writelines(non_empty_lines)

    with open('txt\print_car_new.txt', 'r', encoding='utf-8', newline='') as file:
        data = file.read()

    lines = data.strip().split("\n")

    new_data = ""
    for i in range(1, len(lines), 11):
        new_data += "Марка: " + lines[i] + ""
        new_data += "Модель: " + lines[i + 1] + ""
        new_data += "Год: " + lines[i + 2] + ""
        new_data += "Л.c: " + lines[i + 3] + ""
        new_data += "Литры: " + lines[i + 4] + ""
        new_data += "Коробка передач: " + lines[i + 5] + ""
        new_data += "Привод: " + lines[i + 6] + ""
        new_data += "Цвет: " + lines[i + 7] + ""
        new_data += "Страна производства: " + lines[i + 8] + ""
        new_data += "Цена: " + lines[i + 9] + "\n"

    #print(new_data)
    with open(r"txt\new_new.txt", "w") as file:
        file.write(new_data)

    file = open(r"txt\new_new.txt")
    return file.read()


@bot.message_handler(commands=['car_catalog'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Америка")
    btn2 = types.KeyboardButton("Германия")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Из какой страны ты хочешь себе машину?\n"
                                           "Из Америки такие как Ford, Dodge, Chevrolet\n"
                                           "Из Германии такие как BMW, Mercedes, Porsche".format(message.from_user), reply_markup=markup)


@bot.message_handler(commands=['technical_support'])
def technical_support(message):
    bot.send_message(message.chat.id, "@idhxjsnd\n"
                                      "Егор олегович")


@bot.message_handler(commands=['registration'])
def registration(message):
    bot.send_message(message.chat.id, registration_text())


@bot.message_handler(content_types=['text'])
def nemec(message):
    if message.text == "Германия":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("BMW")
        btn2 = types.KeyboardButton("Mercedes")
        btn3 = types.KeyboardButton("Porsche")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(message.chat.id, text="Выбери марку машины ", reply_markup=markup)
    elif message.text == "BMW":
        bot.send_message(message.chat.id, bmw())
    elif message.text == "Mercedes":
        bot.send_message(message.chat.id, mercedes())
    elif message.text == "Porsche":
        bot.send_message(message.chat.id, porsche())
    elif message.text == "Вернуться в главное меню":
        bot.send_message(message.chat.id, start_text())
    if message.text == "Америка":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Ford")
        btn2 = types.KeyboardButton("Dodge")
        btn3 = types.KeyboardButton("Chevrolet")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(message.chat.id, text="Выбери марку машины ", reply_markup=markup)
    elif message.text == "Ford":
        bot.send_message(message.chat.id, ford())
    elif message.text == "Dodge":
        bot.send_message(message.chat.id, dodge())
    elif message.text == "Chevrolet":
        bot.send_message(message.chat.id, chevrolet())

        '''
        def fio_text(message):
            all_text = message.text
            file = open(r'txt\registration.txt', 'w')
            file.write(all_text)
            file.close()

            with open(r'txt\registration.txt', "r") as file:
                lines = file.readlines()
                FIO_text = lines[0]
                number_text = lines[1]
                age_text = lines[2]
                gmail_text = lines[3]
                adress_text = lines[4]

            bot.send_message(message.from_user.id, 'Вы зарегистрировались')
            db_table_val_user(FIO=FIO_text, number=number_text, age=age_text, gmail=gmail_text, adress=adress_text)
        '''


bot.polling(none_stop=True)




