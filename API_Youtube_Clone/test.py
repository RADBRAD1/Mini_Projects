import requests

#location of the api, server that it runs on
BASE =  "http://127.0.0.1:5000"

data = [ 
    { "likes": 78, "name": "Joe", "views": 100000},
    { "likes": 10000, "name": "How to make REST API", "views": 80000},
    { "likes": 35, "name": "Tim", "views": 2000}
]

for i in range(len(data)):
    response = requests.put(BASE+"video/" +str(i), data[i])
    print(response.json())

input()
response = requests.delete(BASE + "video/0")
print(response) #not print(response.json()), because in the .delete method defined we do not return any json serializable object.
input()
response = requests.get(BASE+"video/2")
print(response.json())



#sends a get request to the specified url which is base +helloworld.

#response = requests.put(BASE+"helloworld/tim", { "data": "information"}) # this action makes it so that not only is the url put, but the data that is passed into
# the put funciton call also is

