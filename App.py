import json

import numpy as np
import pandas as pd
from flask import Flask, jsonify, redirect, render_template, request
# Using Conine similarity to calculate simirarity factor ofall songs
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
uploads_dir = "/home/becode/BeCode Projects/Music_RecommendationApp/Data/Final_Data.csv"
df1 = pd.read_csv(uploads_dir)
df1.drop(["Unnamed: 0"], axis=1, inplace=True)


def get_song(title, df1):
    # 1. Based on the title get the song data from the dataframe
    song_index = df1[df1['song'] == title].index.values
    song_data = df1.iloc[song_index, 4:]
    # 2. Compare the song data (vector) with all the dataframe
    cosine = cosine_similarity(song_data, df1.iloc[:, 4:])[0]
    # 3. Create a new coloumn with the cosine similarity
    df1["CosineSimilarity"] = cosine.tolist()
    # 4. Return top 10 songs based on cosine similarity
    score = df1.sort_values(by=["CosineSimilarity"], ascending=False)
    top10_songs = score["song"][1:11]
    top10_songs_list = top10_songs.values.tolist()
    return top10_songs_list


def get_top_songs():
    return df1.head(10)

# route to form to get house details from user


@app.route('/User_Song/', methods=['POST', 'GET'])
def inputdata():

    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':

        songslst = {}

        # get the song title from form
        song_title = request.form['search']

        # get the list
        top_songs = get_song(song_title, df1)

        # populate the song list
        songslst = json.dumps(top_songs)

        # create json object
        json_song = json.loads(songslst)

        return render_template('index.html', top_songs=render_template('SongTracks.html', songs=json_song))


app.run(host='localhost', port=5002)
#app.run()
