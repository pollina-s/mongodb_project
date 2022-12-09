import pymongo

db_connection = pymongo.MongoClient("mongodb:\\localhost:27017")
current_db = db_connection["projectdb"]  # обращаемся к клиенту и указываем название бд

collection = current_db["creators"]

discovery_channel = {
    'title': 'Discovery Channel Россия',
    'url': 'https://www.youtube.com/@DiscoveryChannelRussia',
    'subscribers': '2470000',
    'views': '425382352'
}

#  ниже показан пример того, как добавлять в коллекцию по одной записи
result = collection.insert_one(discovery_channel)  # добавление записи в коллекцию
print(result.inserted_id)  # id добавленного объекта

more_creators = {  # на примере популярных каналов рассмотрим, как добавлять много записей сразу
    'title': 'selfedu', 'url': 'https://www.youtube.com/@selfedu_rus', 'subscribers': '88300', 'views': '10542737',
    'title': 'Python Hub Studio', 'url': 'https://www.youtube.com/@PythonHubStudio', 'subscribers': '132000', 'views': '6390498',
    'title': 'Sergey Nemchinskiy', 'url': 'https://www.youtube.com/@SergeyNemchinskiy', 'subscribers': '323000', 'views': '35203048'
}

result = collection.insert_many(more_creators)
print(result.inserted_ids)

#  рассмотрим простой запрос на нахождение документа с количеством подписчиков n
subs = 132000
print(collection.find_one('subscribers': subs))  # сам запрос
print(collection.count_documents('subscribers': subs))

for channel in collection.find():
    print(channel)

#  запрос сложнее с выборкой конкретных записей, подходящих под нужный запрос
print('Количество просмотров > 30000000')
print(collection.count_documents({'Views': {'$gt': 30000000}}))  # $gt - больше
print('Количество подписчиков < 10000')
print(collection.count_documents({'Subscribers': {'$lt': 10000}}))  # $lt - больше

#  запросы могут быть абсолютно разные, но принцип один и тот же, небольшие изменения в коде. MongoDB - достаточно простая бд