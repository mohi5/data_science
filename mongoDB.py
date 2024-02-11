# import pymongo
# client=pymongo.MongoClient("mongodb+srv://Mohit_tiwari:Mohit8989$@cluster0.kxhcjuw.mongodb.net/?retryWrites=true&w=majority")
# db = client.connect


from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://Mohit_tiwari:Mohit8989$@cluster0.kxhcjuw.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client['Mohit'] # This is my database name
data = {
    'name':'mohit',
    'course':'data science',
    'time':'flexi'
}
coll_pwskills = db['my record'] # This is my collection name
coll_pwskills.insert_one(data)

data1 = { #this is data name
    'mailid' : 'mohit@gmail.com',
    'phone no.':947150444,
    'addr':'hyderabad'
}
coll_pwskills.insert_one(data1)

data2 = [
  {
    "name": "Adeel Solangi",
    "language": "Sindhi",
    "id": "V59OF92YF627HFY0",
    "bio": "Donec lobortis eleifend condimentum. Cras dictum dolor lacinia lectus vehicula rutrum. Maecenas quis nisi nunc. Nam tristique feugiat est vitae mollis. Maecenas quis nisi nunc.",
    "version": 6.1
  },
  {
    "name": "Afzal Ghaffar",
    "language": "Sindhi",
    "id": "ENTOCR13RSCLZ6KU",
    "bio": "Aliquam sollicitudin ante ligula, eget malesuada nibh efficitur et. Pellentesque massa sem, scelerisque sit amet odio id, cursus tempor urna. Etiam congue dignissim volutpat. Vestibulum pharetra libero et velit gravida euismod.",
    "version": 1.88
  },
  {
    "name": "Aamir Solangi",
    "language": "Sindhi",
    "id": "IAKPO3R4761JDRVG",
    "bio": "Vestibulum pharetra libero et velit gravida euismod. Quisque mauris ligula, efficitur porttitor sodales ac, lacinia non ex. Fusce eu ultrices elit, vel posuere neque.",
    "version": 7.27
  },
  {
    "name": "Abla Dilmurat",
    "language": "Uyghur",
    "id": "5ZVOEPMJUI4MB4EN",
    "bio": "Donec lobortis eleifend condimentum. Morbi ac tellus erat.",
    "version": 2.53
  },
  {
    "name": "Adil Eli",
    "language": "Uyghur",
    "id": "6VTI8X6LL0MMPJCC",
    "bio": "Vivamus id faucibus velit, id posuere leo. Morbi vitae nisi lacinia, laoreet lorem nec, egestas orci. Suspendisse potenti.",
    "version": 6.49
  },
  {
    "name": "Adile Qadir",
    "language": "Uyghur",
    "id": "F2KEU5L7EHYSYFTT",
    "bio": "Duis commodo orci ut dolor iaculis facilisis. Morbi ultricies consequat ligula posuere eleifend. Aenean finibus in tortor vel aliquet. Fusce eu ultrices elit, vel posuere neque.",
    "version": 1.9
  }]

coll_pwskills.insert_many(data2)
print(coll_pwskills.find_one()) # For printing or finding one data

# for i in coll_pwskills.find(): # For finding all data
#     print(i)

for i in coll_pwskills.find({'name':'mohit'}): # for finding specific data
    print(i)

for i in coll_pwskills.find({'_id':{'$gte':'4'}}): # for finding greater then equal to or any filter based on compresion , we have reserved keyword for that($gte)
    print(i)

coll_pwskills.update_many({'name':'mohit'},{'$set':{'name':'Rohit'}}) #for updating the data that already exist and here ($set) is a reserved word
