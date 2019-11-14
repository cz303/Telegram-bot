#!/usr/bin/python3
import config
import telebot
import requests
from keyboard_bot import menu
from bot_mess_controller import *
from bot_function import *

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, string_hello())
	create_account(message)

@bot.message_handler(commands=['menu'])
def send_menu(message):
	bot.send_message(message.chat.id,"Меню🏠", reply_markup = menu())

@bot.message_handler(commands=['help'])
def send_help(message):
	bot.send_message(message.chat.id,string_help(), reply_markup = menu(),parse_mode='HTML')

@bot.message_handler(content_types=['text'])
def send_message(message):
	bot_st = return_user(message)
	if bot_st['state_controller'] == 'menu':
		menu_mess_controller(message)
	elif bot_st['state_controller'] == 'menu_conv':
		menu_conv_mess_controller(message)
	elif bot_st['state_controller'] == 'menu_wallet':
		menu_wallet_mess_controller(message)
	elif bot_st['state_controller'] == 'menu_poloniex':
		menu_poloniex_mess_controller(message)
	elif bot_st['state_controller'] == 'menu_game_reg':
		menu_game_reg_mess_controller(message)
	elif bot_st['state_controller'] == 'menu_game':
		menu_game_mess_controller(message)
	elif bot_st['state_controller'] == 'cansel':
		cansel_mess_controller(message)
	elif bot_st['state_controller'] == 'menu_buy':
		buy_mess_controller(message)
	elif bot_st['state_controller'] == 'edit_menu':
		edit_mess_controller(message)

if __name__ == "__main__":
	bot.polling()