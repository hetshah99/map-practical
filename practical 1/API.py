# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 23:06:48 2020

@author: HETSHAH
"""


from flask import Flask, jsonify,request

app = Flask(__name__)

movies = [
    {
        "name": "The Shawshank Redemption"
      
    }
]

@app.route('/movies')
def hello():
    return jsonify(movies)


@app.route('/movies/<int:index>', methods=['GET'])
def get1(index):
    movie = request.get_json()
    return jsonify(movies[index-1]), 200


@app.route('/movies', methods=['POST'])
def add_movie():
    movie = request.get_json()
    movies.append(movie)
    return {'id': len(movies)}, 200

@app.route('/movies/<int:index>', methods=['PUT'])
def update_movie(index):
    movie = request.get_json()
    movies[index] = movie
    return jsonify(movies[index]), 200

@app.route('/movies/<int:index>', methods=['DELETE'])
def delete_movie(index):
    movies.pop(index)
    return 'None', 200

app.run()