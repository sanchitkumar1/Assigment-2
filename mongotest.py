import pymongo
client = pymongo.MongoClient("mongodb+srv://test:TEST@atlascluster.npkvi.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

#creating a dictionary
d = {
	"name":"Sanchit",
	"email":"snk324@stern.nyu.edu",
	"surname":"Kumar"
}

#inserting the dictionary into mongodb
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)

