#%% Imports

import eyed3
import os

#%% Getting file names and new song names

# Both, names of file, of whicht the songnames should be chang

songspath = "C:\\Users\\ralph\\Music\\songs"


file_names = [file for file in os.listdir(songspath) if ".mp3" in file]

with open(os.path.join(songspath, 'new_song_names.txt'), "r") as file:
    new_song_names = file.readlines()

with open(os.path.join(songspath, 'new_file_names.txt'), "r") as file:
    new_file_names = file.readlines()

song_numbers = [n+1 for n in list(range(len(file_names)))]


#%% Saving new tags

# Loop to save new info
for i in range(len(file_names)):

    # Loading files
    audiofile = eyed3.load(os.path.join(songspath, file_names[i]))
    # Setting tags
    audiofile.tag.title = new_song_names[i][:-1]
    audiofile.tag.track_num = song_numbers[i]
    audiofile.tag.album = "Demon Slayer the Movie - Mugen Train OST"
    audiofile.tag.genre = "Original Score"
    audiofile.tag.artist = "Go Shiina"
    audiofile.tag.album_artist = "Go Shiina"
    audiofile.tag.original_release_date = 2020
    audiofile.tag.release_date = 2020
    audiofile.tag.save()