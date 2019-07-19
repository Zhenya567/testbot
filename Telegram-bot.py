import telebot
import pyowm

owm = pyowm.OWM('22291e7d43eb6f9fbf30df8fddf07756',language="ru")
bot = telebot.TeleBot("769396375:AAGVe2UxorlIz31qq3aiWfaNf2aMnmYkAMk")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    #bot.reply_to(message, message.text)
    observation = owm.weather_at_place(message.text)
    w = observation.get_weather()
    temp = w.get_temperature('celsius')["temp"]

    answer="В городе/стране "+message.text+" сейчас "+w.get_detailed_status()+"\n"
    answer+= "Температура сейчас в районе "+str(temp)+"\n\n"
    if temp < 10:
        answer += "Сейчас очень холодно надень куртку :)"
    elif temp < 20:
        answer += "Сейчас холодно, оденься потеплее. :)"
    else:
        answer += "Одевай что хочешь :)"

    bot.send_message(message.chat.id,answer)


bot.polling(none_stop=True)