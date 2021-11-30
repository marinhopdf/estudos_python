import requests

url = 'http://www.pudim.com.br'

try:
    msg = requests.get(url)
except requests.exceptions.ConnectionError:
        print('Site pudim está off.')
else:
        print('Site pudim está ON.')
