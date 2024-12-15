import telebot
import sqlite3

API_TOKEN = '7073988924:AAGlr3M6iIkFkZdFp-s3KN-NUh-781_a9MQ'
bot = telebot.TeleBot(API_TOKEN)

conn = sqlite3.connect('db/AUTO.db', check_same_thread=False)
cursor = conn.cursor()


def db_table_val_car(marka: str, model: str, year: int, power: int, liter: int, transmission: str, drive: str, color: str, country: str, price: int, link: str):
    cursor.execute('INSERT INTO CAR (marka, model, year, power, liter, transmission, drive, color, country, price, link) VALUES (?,?,?,?,?,?,?,?,?,?,?)', (marka, model, year, power, liter, transmission, drive, color, country, price, link,))
    conn.commit()


def db_table_val_bmw(marka: str, model: str, year: int, power: int, liter: int, transmission: str, drive: str, color: str, country: str, price: int, link: str):
    cursor.execute('INSERT INTO BMW (marka, model, year, power, liter, transmission, drive, color, country, price, link) VALUES (?,?,?,?,?,?,?,?,?,?,?)', (marka, model, year, power, liter, transmission, drive, color, country, price, link,))
    conn.commit()


def db_table_val_mercedes(marka: str, model: str, year: int, power: int, liter: int, transmission: str, drive: str, color: str, country: str, price: int, link: str):
    cursor.execute('INSERT INTO MERCEDES (marka, model, year, power, liter, transmission, drive, color, country, price, link) VALUES (?,?,?,?,?,?,?,?,?,?,?)', (marka, model, year, power, liter, transmission, drive, color, country, price, link,))
    conn.commit()


def db_table_val_porsche(marka: str, model: str, year: int, power: int, liter: int, transmission: str, drive: str, color: str, country: str, price: int, link: str):
    cursor.execute('INSERT INTO PORSCHE (marka, model, year, power, liter, transmission, drive, color, country, price, link) VALUES (?,?,?,?,?,?,?,?,?,?,?)', (marka, model, year, power, liter, transmission, drive, color, country, price, link,))
    conn.commit()


def db_table_val_ford(marka: str, model: str, year: int, power: int, liter: int, transmission: str, drive: str, color: str, country: str, price: int, link: str):
    cursor.execute('INSERT INTO FORD (marka, model, year, power, liter, transmission, drive, color, country, price, link) VALUES (?,?,?,?,?,?,?,?,?,?,?)', (marka, model, year, power, liter, transmission, drive, color, country, price, link,))
    conn.commit()


def db_table_val_dodge(marka: str, model: str, year: int, power: int, liter: int, transmission: str, drive: str, color: str, country: str, price: int, link: str):
    cursor.execute('INSERT INTO DODGE (marka, model, year, power, liter, transmission, drive, color, country, price, link) VALUES (?,?,?,?,?,?,?,?,?,?,?)', (marka, model, year, power, liter, transmission, drive, color, country, price, link,))
    conn.commit()


def db_table_val_chevrolet(marka: str, model: str, year: int, power: int, liter: int, transmission: str, drive: str, color: str, country: str, price: int, link: str):
    cursor.execute('INSERT INTO CHEVROLET (marka, model, year, power, liter, transmission, drive, color, country, price, link) VALUES (?,?,?,?,?,?,?,?,?,?,?)', (marka, model, year, power, liter, transmission, drive, color, country, price, link,))
    conn.commit()


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, start_text())


def start_text():

    text = ("Привет вот что я могу: \n"
            "/admin_add_car - Добавить машину в БД")
    return text


def admin_add_car_text():
    text = ("Что бы добавить автомобиль в БД вам надо отправить сообщение по типу:\n"
            "Марка машины\n"
            "Модель машины\n"
            "Ее год\n"
            "Лошадиные силы\n"
            "Литры в моторе\n"
            "Привод\n"
            "Цвет\n"
            "Страна производства\n"
            "Цена в рублях\n"
            "Ссылка на фото\n\n"
            "пример:\n"
            "Ford\n"
            "Mustang GT 500\n"
            "2024\n"
            "487\n"
            "5\n"
            "Автомат\n"
            "Задний\n"
            "Серый\n"
            "Америка\n"
            "13000000\n"
            "https://i.pinimg.com/736x/84/de/8416de3461896d837db1287859a69479.jpg\n")
    return text


@bot.message_handler(commands=['admin_add_car'])
def admin_add_car(message):
    bot.send_message(message.chat.id, admin_add_car_text())


@bot.message_handler(content_types=['text'])
def add_car(message):
    all_text = message.text
    file = open(r'txt\add_car.txt', 'w')
    file.write(all_text)
    file.close()

    with open(r'txt\add_car.txt', "r") as file:
        lines = file.readlines()
        marka_text = lines[0]
        model_text = lines[1]
        year_text = lines[2]
        power_text = lines[3]
        liter_text = lines[4]
        transmission_text = lines[5]
        drive_text = lines[6]
        color_text = lines[7]
        country_text = lines[8]
        price_text = lines[9]
        link_text = lines[10]
    bot.send_message(message.from_user.id, 'Вы добавили машину в БД')
    if marka_text == "BMW\n":
        db_table_val_car(marka=marka_text, model=model_text, year=year_text, power=power_text, liter=liter_text,
                         transmission=transmission_text, drive=drive_text, color=color_text, country=country_text,
                         price=price_text, link=link_text)
        db_table_val_bmw(marka=marka_text, model=model_text, year=year_text, power=power_text, liter=liter_text,
                         transmission=transmission_text, drive=drive_text, color=color_text, country=country_text,
                         price=price_text, link=link_text)

    elif marka_text == "Mercedes\n":
        db_table_val_car(marka=marka_text, model=model_text, year=year_text, power=power_text, liter=liter_text,
                         transmission=transmission_text, drive=drive_text, color=color_text, country=country_text,
                         price=price_text, link=link_text)
        db_table_val_mercedes(marka=marka_text, model=model_text, year=year_text, power=power_text, liter=liter_text,
                         transmission=transmission_text, drive=drive_text, color=color_text, country=country_text,
                         price=price_text, link=link_text)

    elif marka_text == "Porsche\n":
        db_table_val_car(marka=marka_text, model=model_text, year=year_text, power=power_text, liter=liter_text,
                         transmission=transmission_text, drive=drive_text, color=color_text, country=country_text,
                         price=price_text, link=link_text)
        db_table_val_porsche(marka=marka_text, model=model_text, year=year_text, power=power_text, liter=liter_text,
                         transmission=transmission_text, drive=drive_text, color=color_text, country=country_text,
                         price=price_text, link=link_text)

    elif marka_text == "Ford\n":
        db_table_val_car(marka=marka_text, model=model_text, year=year_text, power=power_text, liter=liter_text,
                         transmission=transmission_text, drive=drive_text, color=color_text, country=country_text,
                         price=price_text, link=link_text)
        db_table_val_ford(marka=marka_text, model=model_text, year=year_text, power=power_text, liter=liter_text,
                         transmission=transmission_text, drive=drive_text, color=color_text, country=country_text,
                         price=price_text, link=link_text)

    elif marka_text == "Dodge\n":
        db_table_val_car(marka=marka_text, model=model_text, year=year_text, power=power_text, liter=liter_text,
                         transmission=transmission_text, drive=drive_text, color=color_text, country=country_text,
                         price=price_text, link=link_text)
        db_table_val_dodge(marka=marka_text, model=model_text, year=year_text, power=power_text, liter=liter_text,
                         transmission=transmission_text, drive=drive_text, color=color_text, country=country_text,
                         price=price_text, link=link_text)

    elif marka_text == "Chevrolet\n":
        db_table_val_car(marka=marka_text, model=model_text, year=year_text, power=power_text, liter=liter_text,
                         transmission=transmission_text, drive=drive_text, color=color_text, country=country_text,
                         price=price_text, link=link_text)
        db_table_val_chevrolet(marka=marka_text, model=model_text, year=year_text, power=power_text, liter=liter_text,
                         transmission=transmission_text, drive=drive_text, color=color_text, country=country_text,
                         price=price_text, link=link_text)


bot.polling(none_stop=True)