
<h1> <align="center">Music Recommendation System</h1>

## Developer: 

<a href="https://https://github.com/MousumiAria"> Mousumi Sen</a>

## Level: 
* Junior Data Scientist

## Organization:
* Becode Company (Ghent)

## The timeline of the project: 
**16/06/2022 - 30/06/2022  4:30**

## Duration: 
* 2 weeks

## Dataset details:
* This dataset contains audio statistics of the top 2000 tracks on Spotify from 2000-2019. The data contains about 18 columns each 	 describing the track and it's qualities. Colums are: artist, song, duration_ms, explicit, year, popularity, danceability, energy, key, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo, genre.


## Description:

The Music Recommendation System recommend users top 10 songs based on their prefered one. User have to give one song by their own and the system return top 10 similar songs based on comparing there features similarity.To create this app following steps were done:

# Data downloading and cleaning:
* Data downloaded from Spotify.
* Cleaned data and saved in a Final_csv file.


# Data Visualizing:
* In this part first analized the data by obserbing relation between the features of songs, like songs by genre, 
  year, artist, popularity.
* In next step visualized above observation of datas.

# Data Vectorization:

* To vectorization, selected ipmortant features and used cosine similarity to create a score or vector for each  song. 
* Compared the score factor of all songs with the user given song, the app return top 10 most similar songs to user.


## Used Language and Libraries:

* Python
* Numpy
* Pandas 
* Matplotlib
* Seaborn
* Flask
* Sklearn

## Link of the app:https://music-recommendationapp.herokuapp.com/User_Song/



