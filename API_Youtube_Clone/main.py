from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app) #just says that we are going to wrap our application in an API

videos= {

}


#first resource in the API, this video inherits from Resource class
class Video(Resource):
    def get(self, video_id): #allows us to perform get requests. 
        return videos[video_id]
    def put(self, video_id):
        return 



#from the /helloworld url, the HelloWorld resource is accessible. 
api.add_resource(Video, "/video/<int:video_id>") #the <> dictates that the user has to pass in a string, and it can be accessed with the title "name" 
#can add multiple parameters, not necessarily just <string :name>, can add <int:age> 


if __name__ == "__main__":
    app.run(debug = True) #debug = true is only run in a dev, not production environment. 