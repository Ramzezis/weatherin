import telebot
from pyowm import OWM

owm = OWM('585f8699d7815174354185af5788aa33')
bot = telebot.TeleBot("1161445202:AAHR5DewQrTDeupDia6vfQFP9_TD5LGLpI8")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, where do you want to know the weather?")
    # tb.send_message(chat_id, text)

@bot.message_handler(content_types=['text'])
def send_message(message):
	mgr = owm.weather_manager()
	observation = mgr.weather_at_place(message.text)
	w = observation.weather
	temp =w.temperature('celsius')["temp"]

	answer = "In the town " + message.text + " now " + w.detailed_status + "\n\n"
	answer +=  "The temperature is in the area " + str(temp) + " celsius " + "\n\n"
	
	if temp < -30:
		answer += "Buried grandfather"

	elif temp < -10:
		answer += "do you want to live, do not leave home"

	elif temp < -5:
		answer += "Don't forget the scarf"

	elif temp < 0:
		answer += "Cold kapets, dress like a tank !!!"

	elif temp < 5:
		answer += "The jacket will not hurt"

	elif temp < 10:
		answer += "Cold, put on your panties !!!"
	
	elif temp <  15:
		answer += "Ivleeva does't approve"

	elif temp < 20:
		answer += "It's cold outside, dress warmly."

	elif temp < 25:
		answer += "On the street heat, even in shorts go"
		
	elif temp  < 30:
		answer += "Heat, even though fried eggs on the body"

	else:
		answer += "On the street, hellish hell, dress whatever you want, you’ll burn anyway."

	bot.send_message(message.chat.id, answer)

bot.polling( none_stop = True, interval=0 )