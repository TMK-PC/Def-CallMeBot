import requests

class CallMeBot:

    def __init__(self):
        self.__base_url = 'https://api.callmebot.com/whatsapp.php'
        
    def send_message(self, number, key, message):
        response = requests.get(
            url = f'{self.__base_url}?phone=+{number}&text={message}&apikey={key}'
        )
        
        return response.text

        
