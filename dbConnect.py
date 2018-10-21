from pymongo import MongoClient as mongodb

from pymongo import MongoClient as MongClient


# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string

actualClient = MongClient("mongodb://admin:Foodhacking!@hackingfood-shard-00-00-1vijt.azure.mongodb.net:27017,hackingfood-shard-00-01-1vijt.azure.mongodb.net:27017,hackingfood-shard-00-02-1vijt.azure.mongodb.net:27017/test?ssl=true&replicaSet=HackingFood-shard-0&authSource=admin&retryWrites=true")

db=actualClient.business
# Issue the serverStatus command and print the results
serverStatusResult=db.command("serverStatus")
#pprint(serverStatusResult)



client = MongClient("mongodb://admin:Foodhacking!@hackingfood-shard-00-00-1vijt.azure.mongodb.net:27017,hackingfood-shard-00-01-1vijt.azure.mongodb.net:27017,hackingfood-shard-00-02-1vijt.azure.mongodb.net:27017/test?ssl=true&replicaSet=HackingFood-shard-0&authSource=admin&retryWrites=true")
db=client.business





database = client['hackFood']
collection = database['testResults']

print (collection.insert({"restaurant":"im going home"}))
