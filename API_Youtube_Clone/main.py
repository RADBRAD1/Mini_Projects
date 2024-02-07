from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class VideoModel(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	views = db.Column(db.Integer, nullable=False)
	likes = db.Column(db.Integer, nullable=False)

	def __repr__(self):
		return f"Video(name = {name}, views = {views}, likes = {likes})"
	

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video", required=True)
video_put_args.add_argument("likes", type=int, help="Likes on the video", required=True)

video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="Name of the video is required")
video_update_args.add_argument("views", type=int, help="Views of the video")
video_update_args.add_argument("likes", type=int, help="Likes on the video")

resource_fields = {
	'id': fields.Integer,
	'name': fields.String,
	'views': fields.Integer,
	'likes': fields.Integer
} 

#defines how an object should be serialized.  

class Video(Resource):
	@marshal_with(resource_fields)
	def get(self, video_id):
		result = VideoModel.query.filter_by(id=video_id).first()
		if not result:
			abort(404, message="Could not find video with that id")
		return result

	@marshal_with(resource_fields)
	def put(self, video_id):
		args = video_put_args.parse_args()
		result = VideoModel.query.filter_by(id=video_id).first()
		if result:
			abort(409, message="Video id taken...")

		video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
		db.session.add(video)
		db.session.commit()
		return video, 201

	@marshal_with(resource_fields)
	def patch(self, video_id):
		args = video_update_args.parse_args()
		result = VideoModel.query.filter_by(id=video_id).first()
		if not result:
			abort(404, message="Video doesn't exist, cannot update")

		if args['name']:
			result.name = args['name']
		if args['views']:
			result.views = args['views']
		if args['likes']:
			result.likes = args['likes']

		db.session.commit()

		return result


	def delete(self, video_id):
		abort_if_video_id_doesnt_exist(video_id)
		del videos[video_id]
		return '', 204


api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
	app.run(debug=True)


"""
from flask import Flask,request
from flask_restful import Api, Resource, reqparse, abort

#flask-sql alchemy allows us to have an itnerface to work with DBs
from flask_sqlalchemy import SQLAlchemy

#reqparser makes sure when we pass a request, we pass the required information with the request
app = Flask(__name__)
api = Api(app) #just says that we are going to wrap our application in an API
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db" #define where we want our database to be, relative path.
db = SQLAlchemy(app)#wrapping sqlalchemy in our app. 

class VideoModel(db.Model):
    #define fields we want in our video model
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False) #nullable=False means we have to have this information. 
    views = db.Column(db.Integer, nullable = False)
    likes = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return f"Video(name ={name}, views = {views}, likes = {likes})"

db.create_all() #creates the database, only done once. do not re-initialize after first run


video_put_args = reqparse.requestParser() #makes sure it fits the specified guidelines below
#validates data we want to request and process first. 
video_put_args.add_argument("name", type = str, help = "Name of the Video is required", required = True) #help argument tells python what to display if user doesnt give us the name argument.
video_put_args.add_argument("views", type = int, help = "Views of the Video is required",required= True) 
video_put_args.add_argument("likes", type = int, help = "Number of likes on the Video is required", required = True) #required= True makes sure that it crashes if not given this arg. 


videos= {

}
#can store data in memory. can do so with the request library within flask, and do  print(request.form)

def abort_if_video_id_not_exist(video_id):
    if video_id not in videos:
        abort(404, message = "Could not find the video") #abort sends an error message back, sending the included string. skips any following statements
        
def abort_if_video_exists(video_id):
    if video_id in videos:
         abort(409, message = "Video already exists with that ID")

#first resource in the API, this video inherits from Resource class
class Video(Resource):
    def get(self, video_id): #allows us to perform get requests. 
        abort_if_video_id_not_exist(video_id)
        return videos[video_id]
    def put(self, video_id):
        abort_if_video_exists(video_id)
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201 #return data plus a status code here
    def delete(self, video_id):
        abort_if_video_id_not_exist(video_id)
        del(videos[video_id])
        return '', 204



#from the /helloworld url, the HelloWorld resource is accessible. 
api.add_resource(Video, "/video/<int:video_id>") #the <> dictates that the user has to pass in a string, and it can be accessed with the title "name" 
#can add multiple parameters, not necessarily just <string :name>, can add <int:age> 


if __name__ == "__main__":
    app.run(debug = True) #debug = true is only run in a dev, not production environment. 
"""