from flask import Flask,jsonify,request
import csv

all_movies = []

with open("movies.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]

liked = []
unliked = []
did_not_watch = []

api = Flask(__name__)

@api.route("/get-movies")

def get_movies():
    return jsonify({
        "data":all_movies[0]
    })
    
@api.route("/liked-movies",methods=['POST'])

def liked_movies():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    liked.append(movie)
    return jsonify({
        "status":'succcessful'
    })
    
@api.route("/unliked-movies",methods=['POST'])

def unliked_movies():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    unliked.append(movie)
    return jsonify({
        "status":'succcessful'
    })
    
@api.route("/did-not-watch-movies",methods=['POST'])

def did_not_watch_movies():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    did_not_watch.append(movie)
    return jsonify({
        "status":'succcessful'
    })
    
api.run()