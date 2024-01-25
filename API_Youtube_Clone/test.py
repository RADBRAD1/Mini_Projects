import requests

#location of the api, server that it runs on
BASE =  "http://127.0.0.1:5000"

#sends a get request to the specified url which is base +helloworld.

response = requests.put(BASE+"helloworld/tim", { "data": "information"}) # this action makes it so that not only is the url put, but the data that is passed into
# the put funciton call also is

