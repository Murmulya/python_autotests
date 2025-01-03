import requests # подключить библиотеку requests

HOST = 'https://api.pokemonbattle.ru/v2' # переменная имя хоста

END1 = '/pokemons' # переменная эндпойнт - покемоны

END2 = '/trainers/add_pokeball' # переменная эндпойнт - поймать в покебол

TOKEN = 'd67f5a2ac77cab781989e4fb34d43f3e' # переменная токен тренера

QUERY = {'trainer_id' : '12514'} # переменная QUERY для переименования

HEAD={'Content-Type' : 'application/json','trainer_token' : TOKEN}
# переменная заголовок - контент и токен

body_create={
    "name": "generate", "photo_id": -1
    }
# переменная body_create - создать покемона, имя авто, фото авто

r_create = requests.post(url = f'{HOST}{END1}', headers = HEAD, json=body_create)
# переменная r_create = ответ на запрос создания покемона

new_id = r_create.json()['id']
# переменная new_id - id созданного покемона из ответа, понадобится дальше

mess1 = r_create.json()['message'] # переменная mess1 - сообщение из ответа

print(r_create.status_code, mess1, new_id) # вывод статус-кода ответа,mess1, new_id

new_name = 'Пупсик'# переменная new_name - новое имя для созданного покемона

body_rename = { # переменная body_rename - переименовать покемона new_id в new_name
    "pokemon_id": new_id,
    "name": new_name,
    "photo_id": 2
}

r_rename = requests.put(url = f'{HOST}{END1}', headers = HEAD, json=body_rename)
# переменная r_rename = ответ на запрос переименования покемона

mess2 = r_rename.json()['message'] # переменная mess2 - сообщение из ответа

ren_id = r_rename.json()['id'] # переменная ren_id - id переименованного

if new_id == ren_id:
# если id созданного и переименованного совпали -
# вывод статус-кода ответа,mess2, ren_id, new_name
    print(r_rename.status_code, mess2, ren_id, new_name)
else:
    print(r_rename.status_code,'переименован другой покемон(')

body_add = { # переменная body_add - поймать покемона ren_id в покебол
    "pokemon_id": ren_id
}

r_add = requests.post(url = f'{HOST}{END2}', headers = HEAD, json=body_add)
# переменная r_add = ответ на запрос поймать в покебол

mess3 = r_add.json()['message'] # переменная mess3 - сообщение из ответа

add_id = r_add.json()['id'] # переменная add_id - id пойманного

print(r_add.status_code, mess3, add_id) # вывод статус-кода ответа,mess3, add_id

# запрос всех покемонов у тренера
# r_poke = requests.get(url = f'{HOST}{END2}',headers = HEAD, params = QUERY)
# print(r_poke.status_code, r_poke.json())
