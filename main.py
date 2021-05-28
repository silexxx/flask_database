from flask import Flask,request
from flask_restful import  Api,Resource,reqparse,abort

from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'
api=Api(app)

db=SQLAlchemy(app)


class VideoModel(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    views=db.Column(db.Integer,nullable=False)
    likes=db.Column(db.Integer,nullable=False)


    def __repr__(self):
        return f"(Video(name= {name}, views= {views}, likes= {likes})"

# db.create_all()


video_put_args=reqparse.RequestParser()
video_put_args.add_argument("name",type=str,help="Name of  the video",required=True)
video_put_args.add_argument("views",type=str,help="views of  the video",required=True)
video_put_args.add_argument("likes",type=str,help="likes on  the video",required=True)

videos={}

def abort_if_video_id_doesnot_exist(video_id):
    if video_id not in videos:
        abort(404,message="Could not find video....")
def abort_if_video_exists(video_id):
    if video_id in videos:
        abort(409,message="video already exist with that ID...")

class Video(Resource):
    def get(self,video_id):
        abort_if_video_id_doesnot_exist(video_id)
        return videos[video_id]

    def put(self,video_id):
        abort_if_video_exists(video_id)
        args=video_put_args.parse_args()
        videos[video_id]=args
        return videos[video_id],201

    def delete(self,video_id):
        abort_if_video_id_doesnot_exist(video_id)
        del videos[video_id]
        return '',204

api.add_resource(Video,"/video/<int:video_id>")


if __name__ == '__main__':
    app.run(debug=True)