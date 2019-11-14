#! ./venv/bin/python3
import telebot

def menu():
	markup = telebot.types.ReplyKeyboardMarkup(True,False)
	m_btn_get_btc = telebot.types.KeyboardButton('Курс↗️')
	m_btn_graf = telebot.types.KeyboardButton('График📊')
	m_btn_birj = telebot.types.KeyboardButton('Биржа Poloniex🏦')
	m_btn_get_wallet = telebot.types.KeyboardButton('Кошелек💰')
	m_btn_convert = telebot.types.KeyboardButton('Конвертер💱')
	m_btn_game = telebot.types.KeyboardButton('Игра🎮')
	markup.add(m_btn_get_btc,m_btn_convert,m_btn_graf)
	markup.add(m_btn_birj,m_btn_get_wallet)
	markup.add(m_btn_game)
	return markup

def menu_poloniex():
	markup = telebot.types.ReplyKeyboardMarkup(True,False)
	m_btn_get_course = telebot.types.KeyboardButton('Курс биржи↗️')
	m_btn_get_volume = telebot.types.KeyboardButton('Объем за 24 часа🕜')
	m_btn_exit = telebot.types.KeyboardButton('Меню🏠')
	markup.add(m_btn_get_course)
	markup.add(m_btn_get_volume)
	markup.add(m_btn_exit)
	return markup

def menu_wallet():
	markup = telebot.types.ReplyKeyboardMarkup(True,False)
	m_btn_get_balance = telebot.types.KeyboardButton('Баланс💳')
	m_btn_exit = telebot.types.KeyboardButton('Меню🏠')
	markup.add(m_btn_get_balance)
	markup.add(m_btn_exit)
	return markup

def menu_conv():
	markup = telebot.types.ReplyKeyboardMarkup(True,False)
	m_btn_get_convert = telebot.types.KeyboardButton('Список сайтов▶')
	m_btn_exit = telebot.types.KeyboardButton('Меню🏠')
	markup.add(m_btn_get_convert)
	markup.add(m_btn_exit)
	return markup

def menu_game_reg():
	markup = telebot.types.ReplyKeyboardMarkup(True,False)
	m_btn_registration = telebot.types.KeyboardButton('Регистрация📝')
	m_btn_exit = telebot.types.KeyboardButton('Меню🏠')
	markup.add(m_btn_registration)
	markup.add(m_btn_exit)
	return markup

def inline_calc():
    markup = telebot.types.InlineKeyboardMarkup()
    m_btn_btc_usd = telebot.types.InlineKeyboardButton('cryptonator.com',url='https://ru.cryptonator.com/converter?utm_referrer=https%3a%2f%2fwww.google.com%2f')
    m_btn_usd_btc = telebot.types.InlineKeyboardButton('myfin.by',url='https://myfin.by/crypto-rates/calculator')    
    markup.add(m_btn_btc_usd)
    markup.add(m_btn_usd_btc)
    return markup

def menu_game():
	markup = telebot.types.ReplyKeyboardMarkup(True,False)
	m_btn_stat = telebot.types.KeyboardButton('Моя компания🏢')
	m_btn_exchanger = telebot.types.KeyboardButton('ТОП-5 игроков🔝')
	m_btn_oil = telebot.types.KeyboardButton('Нефтяные вышки⛽')
	m_btn_buy = telebot.types.KeyboardButton('Купить вышки💲')
	m_btn_edite = telebot.types.KeyboardButton('Настройки⚙')
	m_btn_exit = telebot.types.KeyboardButton('Меню🏠')
	markup.add(m_btn_stat,m_btn_exchanger)
	markup.add(m_btn_buy,m_btn_oil)
	markup.add(m_btn_exit,m_btn_edite)
	return markup

def menu_buy_tower():
	markup = telebot.types.ReplyKeyboardMarkup(True,False)
	m_btn_buy_1 = telebot.types.KeyboardButton('Купить №1💲')
	m_btn_buy_2 = telebot.types.KeyboardButton('Купить №2💲')
	m_btn_buy_3 = telebot.types.KeyboardButton('Купить №3💲')
	m_btn_cansel = telebot.types.KeyboardButton('Отмена✖️')
	markup.add(m_btn_buy_1,m_btn_buy_2)
	markup.add(m_btn_buy_3)
	markup.add(m_btn_cansel)
	return markup

def cansel():
	markup = telebot.types.ReplyKeyboardMarkup(True,False)
	m_btn_cansel = telebot.types.KeyboardButton('Отмена✖️')
	markup.add(m_btn_cansel)
	return markup

def menu_collect():
	markup = telebot.types.ReplyKeyboardMarkup(True,False)
	m_btn_collect = telebot.types.KeyboardButton('Собрать⛽')
	m_btn_cansel = telebot.types.KeyboardButton('Отмена✖️')
	markup.add(m_btn_collect)
	markup.add(m_btn_cansel)
	return markup