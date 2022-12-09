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
