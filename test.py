# num1 = input("type first number ")
# num2 = input("type second number ")
# sim = input("type operator ")
# if sim == "pluss": print(int(num1) + int(num2))
# if sim == "minus": print(int(num1) - int(num2))
# if sim == "divide": print(int(num1) / int(num2))
# if sim == "multiply": print(int(num1) * int(num2))	
# if sim == "+": print(int(num1) + int(num2))
# if sim == "-": print(int(num1) - int(num2))
# if sim == "/": print(int(num1) / int(num2))
# if sim == "*": print(int(num1) * int(num2))	
# import pyowm

# owm = pyowm.OWM('ef16c91feb6e48f02903e6769e2a1ebc', language = "ru")
 
# plase = input("vor qaxaqum/erkrum es mnum ? ")

# observation = owm.weather_at_place(plase)
# w = observation.get_weather()
# temp = w.get_temperature('celsius') 
# print(plase + " goradum " + "hmi " + w.get_detailed_status())  
# print("jermastichan@ motavorapes" + str(temp))
import pyowm
import telebot
import math


owm = pyowm.OWM('ef16c91feb6e48f02903e6769e2a1ebc', language = "ru")
bot = telebot.TeleBot("845338292:AAHk3_Fkyqpn4v-g28zoINnYmaSrX_WOblw")

@bot.message_handler(content_types=['text'])
def send_welcome(message):
	observation = owm.weather_at_place( message.text )
	w = observation.get_weather()
	temp = w.get_temperature('celsius')["temp"]

	answer = message.text + " Գոռըդում " + "հմի " + w.get_detailed_status() + "\n"
	lome = "ջերմաստիճանը մոտ " + str(round(temp)) + " աստիճան է" + "\n\n"
	if temp < 10:
		lome += "շատ ա ցուրտ տաք կ հագնվես"
	elif temp < 15 and temp > 10:
		lome += "ըտենց շատ չի ցուրտ բայց տաք կ հագնվես"
	elif temp >15 and temp < 20:
		lome += "նորմալ ա, կարաս թեթև հագնվես"
	elif temp > 20 and temp < 30:
		lome += "ահավոր շոգ ա հետդ զոնտիկ կվերցնես"
		
	bot.send_message(message.chat.id, answer + str(lome))

bot.polling( none_stop = True)	