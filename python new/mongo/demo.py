
from pymongo.mongo_client import MongoClient
import datetime
uri = "mongodb+srv://tajraffick:Irfaan123@cluster0.k8usdmm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# print(client.list_database_names())
# db=client.test
# print(db.list_collection_names())

# #create one data
# data1={"name":"Nisha","course":"MongoDb","grade":10,"subjects":["python","DB"],"date":str(datetime.datetime.utcnow())}

# test1=db.newtest
# #result=test1.insert_one(data1)

# data2={"name":"John","course":"MongoDb","grade":11,"subjects":["python","DB"],"date":str(datetime.datetime.utcnow())},{"name":"John","course":"SQL","grade":12,"subjects":["python","DB"],"date":str(datetime.datetime(2024,2,1,10,45))}

# result=test1.insert_many(data2)

# #retrieve items

# result=test1.find_one()#retrieve first item
# print("the datas are",result)



# #retrieve items based on key

# # result=test1.find_one({"name":"John","grade":11})#retrieve based on bson
# # print(result)

# # result=test1.find_one({"subjects":"python"})#retrieve based on bson
# # print(result)

# #to retrieve based on id
# # from bson.objectid import ObjectId
# # result=test1.find_one({"_id":ObjectId("65d9bd08e1cd3522ea754d81")})#retrieve based on bson
# # print(result)


# #to retrive results through loop
# # results=test1.find({"name":"John"})
# # print(list(results))
# # print(results)

# # for result in results:
# #     print(result)
    
# # print(test1.count_documents({"grade":10}))

# #range function
# # date1=datetime.datetime(2020,2,1)
# # results=test1.find({"date":{"$gt":date1}}).sort('name')

# # for result in results:
# #     print(result)

# #remove datas
# from bson.objectid import ObjectId
# remdata=test1.delete_one({"name":"Nisha"})


# #remdata=test1.delete_one({"_id":ObjectId('65d9bd08e1cd3522ea754d81')})
# #remdata=test1.delete_many({"name":"John"})

# #update
# result=test1.update_one({'name':'John'},{'$set':{"name":"Jack"}})
# # result=test1.update_one({'name':'Jack'},{'$unset':{"name":"John"}})



