import telebot
import config
from keyboard_bot import *
from bot_function import *
import ai_bot

bot = telebot.TeleBot(config.token)

def menu_mess_controller(message):
    if message.text == 'Игра🎮':
        if autorization_user(message):
            bot.send_message(message.chat.id,"CryptoTower🎮", reply_markup = menu_game_reg())
            update_state_menu(message,'menu_game_reg')
        else:
            bot.send_message(message.chat.id,"CryptoTower🎮", reply_markup = menu_game())
            update_state_menu(message,'menu_game')
    elif message.text == 'Курс↗️':
        bot.send_message(message.chat.id,get_course_top5(),parse_mode='HTML')
    elif message.text == 'График📊':
        bot.send_photo(message.chat.id,photo=get_plot_btc())
    elif message.text == 'Биржа Poloniex🏦':
        bot.send_message(message.chat.id,"Биржа Poloniex🏦", reply_markup = menu_poloniex())
        update_state_menu(message,'menu_poloniex')
    elif message.text == 'Кошелек💰':
        bot.send_message(message.chat.id,"Кошелек💰", reply_markup = menu_wallet())
        update_state_menu(message,'menu_wallet')
    elif message.text == 'Конвертер💱':
        bot.send_message(message.chat.id,"Конвертер💱", reply_markup = menu_conv())
        update_state_menu(message,'menu_conv')
    else:
        bot.send_message(message.chat.id,ai_bot.ai_bot_answer(message.text))

def menu_conv_mess_controller(message):
    if message.text == 'Список сайтов▶':
        bot.send_message(message.chat.id, "Сайты▶",reply_markup=inline_calc())
    elif message.text == 'Меню🏠':
        bot.send_message(message.chat.id,"Меню🏠", reply_markup = menu())
        update_state_menu(message,'menu')
    else:
        bot.send_message(message.chat.id,ai_bot.ai_bot_answer(message.text))

def menu_poloniex_mess_controller(message):
    if message.text == 'Курс биржи↗️':
        bot.send_message(message.chat.id,get_poloniex_course(),parse_mode='HTML')
    elif message.text == 'Объем за 24 часа🕜':
        bot.send_message(message.chat.id,return_24_volume(),parse_mode='HTML')
    elif message.text == 'Меню🏠':
        bot.send_message(message.chat.id,"Меню🏠", reply_markup = menu())
        update_state_menu(message,'menu')
    else:
        bot.send_message(message.chat.id,ai_bot.ai_bot_answer(message.text))

def menu_wallet_mess_controller(message):
    if message.text == 'Баланс💳':
        bot.send_message(message.chat.id,get_balanses_wallet(),parse_mode='HTML')
    elif message.text == 'Меню🏠':
        bot.send_message(message.chat.id,"Меню🏠", reply_markup = menu())
        update_state_menu(message,'menu')
    else:
        bot.send_message(message.chat.id,ai_bot.ai_bot_answer(message.text))

def menu_game_mess_controller(message):
    if message.text == 'Моя компания🏢':
        bot.send_message(message.chat.id,info_of_comp(message),parse_mode='HTML')
    elif message.text == 'Нефтяные вышки⛽':
        bot.send_message(message.chat.id,oil_tower(message),reply_markup=menu_collect())
    elif message.text == 'Купить вышки💲':
        bot.send_message(message.chat.id,buy_oil_tower_string(),reply_markup=menu_buy_tower())
        update_state_menu(message,'menu_buy')
    elif message.text == 'Собрать⛽':
        collect(message)
        bot.send_message(message.chat.id,"Баррели переведены в BCoin успешно!",reply_markup=menu_game())
    elif message.text == 'ТОП-5 игроков🔝':
        bot.send_message(message.chat.id,top_5(),parse_mode='HTML')
    elif message.text == 'Отмена✖️':
        bot.send_message(message.chat.id,"Отмена✖️",reply_markup = menu_game())
    elif message.text == 'Меню🏠':
        bot.send_message(message.chat.id,"Меню🏠", reply_markup = menu())
        update_state_menu(message,'menu')
    elif message.text == 'Настройки⚙':
        bot.send_message(message.chat.id,"Изменить название комании?⚙", reply_markup = cansel())
        update_state_menu(message,'edit_menu')
    else:
        bot.send_message(message.chat.id,ai_bot.ai_bot_answer(message.text))

def buy_mess_controller(message):
    if message.text == 'Купить №1💲':
        bot.send_message(message.chat.id,buy_oil_tower_1(message))
    elif message.text == 'Купить №2💲':
        bot.send_message(message.chat.id,buy_oil_tower_2(message))
    elif message.text == 'Купить №3💲':
        bot.send_message(message.chat.id,buy_oil_tower_3(message))
    elif message.text == 'Отмена✖️':
        bot.send_message(message.chat.id,"Отмена✖️",reply_markup = menu_game())
        update_state_menu(message,'menu_game')
    else:
        bot.send_message(message.chat.id,ai_bot.ai_bot_answer(message.text))

def menu_game_reg_mess_controller(message):
    if message.text == 'Регистрация📝':
        bot.send_message(message.chat.id,'Введите название компании:',reply_markup=cansel())
        update_state_menu(message,'cansel')
    elif message.text == 'Меню🏠':
        bot.send_message(message.chat.id,"Меню🏠", reply_markup = menu())
        update_state_menu(message,'menu')
    else:
        bot.send_message(message.chat.id,ai_bot.ai_bot_answer(message.text))

def cansel_mess_controller(message):
    if message.text == 'Отмена✖️':
        bot.send_message(message.chat.id,"Отмена✖️",reply_markup = menu_game_reg())
        update_state_menu(message,'menu_game_reg')
    else:
        update_comp_name_users(message,message.text)
        bot.send_message(message.chat.id,"Регистрация прошла успешно!✅",reply_markup = menu_game())
        update_state_menu(message,'menu_game')

def edit_mess_controller(message):
    if message.text == 'Отмена✖️':
        bot.send_message(message.chat.id,"Отмена✖️",reply_markup = menu_game())
        update_state_menu(message,'menu_game')
    else:
        update_comp_name_users(message,message.text)
        bot.send_message(message.chat.id,"Редактирование прошло успешно!✅",reply_markup = menu_game())
        update_state_menu(message,'menu_game')