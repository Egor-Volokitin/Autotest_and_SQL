import configuration
import requests
import data


def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,  # запрос на создание заказа
                         json=body)


response = post_new_order(data.order_body)

print(response.status_code)  # просмотр кода ответа на запрос
print(response.json())  # просмотр тела ответа на запрос

track = response.json()['track']  # сохранение номера заказа в переменную
track = str(track)  # присвоение строчного типа данных номеру заказа
print(track)  # смотрим, что в переменную сохранен номер заказа из запроса


def find_order():
    return requests.get(configuration.URL_SERVICE + configuration.FIND_ORDER + track)  # запрос на поиск заказа по треку


response1 = find_order()

print(response1.status_code)  # просмотр кода ответа на запрос
print(response1.json())  # просмотр тела ответа на запрос
