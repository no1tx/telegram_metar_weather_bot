# -*- coding: utf-8 -*-
from metar import Metar
import re
import requests
import json
import config
import telebot

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
	bot.send_message(message.chat.id, 'Now simple send me ICAO code of desired airport to get human-readable data about weather.\nYou can find out code of your city airport here - http://www.rap.ucar.edu/weather/surface/stations.txt')

@bot.message_handler(commands=['stop'])
def handle_start_help(message):
	bot.send_message(message.chat.id, 'Good bye!')

@bot.message_handler(content_types=["text"])
def send_decoded(message): 
	try:
		buff = str(message.text)
		check = re.compile(r'^[A-Za-z\s]*$')
		if ( len(buff) == 4 and check.match(buff) ):
			code = buff
			fetch_and_decode_metar(code)
			bot.send_message(message.chat.id, 'city: ' + city + '\n' + decoded_data)
		else:
			bot.send_message(message.chat.id, "It's not an ICAO code. Try again.")
	except UnicodeEncodeError:
		bot.send_message(message.chat.id, "It's not an ICAO code. Try again.")

def fetch_and_decode_metar(code):
	global decoded_data
	global city
	city = 'None' # for error report message when got problems with response
	link = 'http://metartaf.ru/' + code + '.json'
	response = requests.get(link)
	try:
		parsed_response = json.loads(response.text)
		city = parsed_response["name"]
		metar_data = parsed_response["metar"]
		metar_data = metar_data.split('\n')
		metar_data = metar_data[1]
		decoded_data = Metar.Metar(metar_data)
		decoded_data = str(decoded_data)
	except ValueError as e:
		decoded_data = 'Catched an error when contacting METAR server (Got empty or wrong JSON response, or you provide a wrong ICAO code). Check your code or try again later.'

if __name__ == '__main__':
	 bot.polling(none_stop=True)
