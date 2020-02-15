import re

import requests

SCHEMA = 'http'
HOST = '127.0.0.1'
PORT = '8012'

BASE_URL = f'{SCHEMA}://{HOST}:{PORT}/'
# CSRF_TOKEN = None


#  Как оказалось, тот токен который находится в куках и называется csrftoken и есть нужный нам токен,
#  не заметил я этого, когда они это дело внедрили.
#  по этому авторизацию можно изменить до такого вида
def get_session():
    url_login = BASE_URL + 'user/login/'
    session = requests.session()
    # requests.get()
    response = session.get(url_login, verify=False)
    session.headers['X-CSRFToken'] = response.cookies['csrftoken']
    login_data = {
        'username': 'admin',
        'password': 'zaq1@WSX',
        'next': '#'
    }
    response = session.post(url_login, data=login_data)
    #  а вот тут и кроется проблема, почему не был валидным токен в последующих запросах,
    #  после успешной авторизации, csrf token изменяется, по этому нужно еще раз изменить его в headers
    session.headers['X-CSRFToken'] = response.cookies['csrftoken']
    # print(response.content)
    return session


SESSION = get_session()

print('\n')
print(SESSION.cookies)
print(SESSION.headers)

item_list_response = SESSION.get(BASE_URL + 'api/item/')

if item_list_response.status_code == 200:
    print(item_list_response.json())

print('\n')
print(SESSION.cookies)
print(SESSION.headers)

new_item = {
    'name': 'Megaproduct',
    'description': 'MegaproductMegaproduct',
    'price': '100500',
    'image': None,
    'department': 1
}

create_item_response = SESSION.post(
    BASE_URL + 'api/item/',
    json=new_item,
)

print(create_item_response.content.decode())


print('\n')
print(SESSION.cookies)
print(SESSION.headers)
get_one_item = SESSION.get(BASE_URL + 'api/item/6/')
if get_one_item.status_code == 200:
    print(get_one_item.json())
else:
    print(get_one_item.text)





