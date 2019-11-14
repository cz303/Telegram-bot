from poloniex_API import *
from bitcoincharts import *
from mongodb import *

cripto_list = ['USDT_BTC','USDT_DASH','USDT_LTC','USDT_XMR','USDT_ETH']
crypto_total = ['totalBTC', 'totalETH', 'totalUSDC', 'totalUSDT', 'totalXMR']

def get_balanses_wallet():
    data = api_query('returnBalances')
    answer = '<b>Ваш баланс</b>\n\n'

    for i in data.keys():
        for j in range(len(cripto_list)):
            if i == cripto_list[j][5:]:
                answer += "<b>{0}</b> - {1:.3f}$\n".format(i,float(data[cripto_list[j][5:]]))
    return answer

def get_poloniex_course():
    data = get_course()
    answer = '<b>Курс биржи Poloniex</b>\n\n'

    for i in data.keys():
        if (float(data[i]['last']) > 1.0) and i[3] == 'T':
            answer += "<b>{0}</b> - {1:.3f}$ ({2:.3f}%)\n".format(i[5:],float(data[i]['last']),float(data[i]['percentChange']))
    return answer

def get_course_top5():
    data = get_course()
    answer = ''

    for i in data.keys():
        for j in range(len(cripto_list)):
            if i == cripto_list[j]:
                answer += "<b>{0}</b> - {1:.3f}$ ({2:.3f}%)\n".format(cripto_list[j][5:],float(data[cripto_list[j]]['last']),float(data[cripto_list[j]]['percentChange']))
    return answer

def get_plot_btc():
    load_image()
    return open('bitcoincharts.jpg', 'rb')

def autorization_user(message):
    user = search_in_db(message)
    if user['name_comp'] == None:
        return True
    else:
        return False

def create_account(message):
    user = search_in_db(message)
    if user == None:
        data = {'id':message.chat.id,'name_comp':None,'byb_coin':100,'tower_1':0,'tower_2':0,'tower_3':0,'poloniex_key':None,'poloniex_sign':None,'state_controller':'menu','oil_1':0,'oil_2':0,'oil_3':0}
        insert_user(data)
    
def info_of_comp(message):
    data = search_in_db(message)
    return "🏢<b>{0}</b> - компания\n⚫️<b>{1}</b> - Bcoin\n⛽<b>{2}</b> - кол-во вышек №1\n⛽<b>{3}</b> - кол-во вышек №2\n⛽<b>{4}</b> - кол-во вышек №3".format(data['name_comp'],data['byb_coin'],data['tower_1'],data['tower_2'],data['tower_3'])

def string_hello():
    return "Привет, я CryptoTowerBot!\nНажми /menu, чтобы продолжить."

def string_help():
    return "HELP:\n/start - start bot\n/menu - base menu\n/help - help\nCreator bot - <a href='https://vk.com/zay_chek'>Vlad Bubeniuk</a>"

def oil_tower(message):
    data = search_in_db(message)
    return '''
                ⛽Нефтяные вышки\nЗдесь Вы можете купить различные нефтяные вышки. Нефтяные вышки добывают 🛢 баррели нефти, которые Вы впоследствии можете продать на рынке за ⚫️ Bcoin и впоследствии можете вывести как реальные деньги!
                \nВаши нефтяные вышки:
                \n⛽ Деревянная ручная вышка
                \nКоличество: {0}
                \nДобыто: {1} 🛢 баррелей нефти
                \n⛽ Металлическая вышка
                \nКоличество: {2}
                \nДобыто: {3} 🛢 баррелей нефти
                \n⛽ Фабричная вышка
                \nКоличество: {4}
                \nДобыто: {5} 🛢 баррелей нефти
            '''.format(data['tower_1'],data['oil_1'],data['tower_2'],data['oil_2'],data['tower_3'],data['oil_3'])

def buy_oil_tower_string():
    return  '⛽️№1 Деревянная ручная вышка\nДобывает 16 🛢 баррелей нефти в час\nЦена: 100 ⚫️ Bcoin\n⛽️№2 Металлическая вышка\nДобывает 184 🛢 баррелей нефти в час\nЦена: 1000 ⚫️ Bcoin\n⛽️№3 Фабричная вышка\nДобывает 1249 🛢 баррелей нефти в час\nЦена: 6000 ⚫️ Bcoin\n'

def buy_oil_tower_1(message):
    if update_user_info_1(message) == True:
        return "Успешно!✅"
    else:
        return "Недостаточно средств!✖️"

def buy_oil_tower_2(message):
    if update_user_info_2(message) == True:
        return "Успешно!✅"
    else:
        return "Недостаточно средств!✖️"

def buy_oil_tower_3(message):
    if update_user_info_3(message) == True:
        return "Успешно!✅"
    else:
        return "Недостаточно средств!✖️"

def return_user(message):
    return search_in_db(message)

def update_state_menu(message,menu):
    update_state(message,menu)

def update_comp_name_users(message,name):
    update_comp_name(message,name)

def collect(message):
    collect_update_coin(message)

def top_5():
    users = top_5_in_db()
    answer = "<b>ТОП-5 игроков🔝</b>\n"
    for i in range(5):
        answer += "🏢<b>{0}</b> - компания\n⚫️<b>{1}</b> - Bcoin\n".format(users[i]['name_comp'],users[i]['byb_coin'])
    return answer

def return_24_volume():
    data = get_history()
    answer = "<b>Объем криптовалюты за 24 часа🕜</b>\n\n"
    for i in crypto_total:
        answer += "<b>{0}</b> - {1:.3f}\n".format(i[5:],float(data[i]))
    return answer

