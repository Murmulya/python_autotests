# подключить библиотеку requests
import requests
# подключить библиотеку pytest
import pytest

HOST = 'https://api.pokemonbattle.ru/v2' # переменная имя хоста
END2 = '/trainers' # переменная эндпойнт - тренеры
TOKEN = 'd67f5a2ac77cab781989e4fb34d43f3e' # токен тренера
QUERY = {'trainer_id' : '12514'} # переменная QUERY тренер ID
HEAD={'Content-Type' : 'application/json','trainer_token' : TOKEN} # переменная заголовок - контент и токен
def test_status_code():
    # запрос на получение полного списка тренеров, ответ в переменную resp_get
    resp_get = requests.get(url = f'{HOST}{END2}',headers = HEAD)
    # утверждаем что статус-код ответа равен 200
    assert resp_get.status_code == 200
def test_trainer_id(): 
    # запрос на данные своего тренера по квери trainer_id, ответ в переменную resp_get1
    resp_get1 = requests.get(url = f'{HOST}{END2}',headers = HEAD, params = QUERY)
    # утверждаем что ответ содержит поле id значение 12514
    assert resp_get1.json()['data'][0]['trainer_name'] == 'Murmulya'