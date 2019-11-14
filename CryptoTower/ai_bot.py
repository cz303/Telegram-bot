#! ./venv/bin/python3
import json
import apiai

def ai_bot_answer(message):
    request = apiai.ApiAI('c6ffd3ebf9bb449b8a25b4266c69ce78').text_request()
    request.lang = 'ru'
    request.session_id = 'BatlabAIBot'
    request.query = message
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech']
    if response:
        return response
    else:
        return 'Я Вас не совсем понял...'