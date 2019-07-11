# This code plays music from youtube.
# It takes a query and serch it on youtube.
# Then plays the first result.
# It downloads the video in mp3 format using youtube-dl 
import os
import urllib.request
from bs4 import BeautifulSoup

# Create a directory to store all music
os.system('mkdir _Music')

print("Welcome, music bot at your service")
print("To exit, type /exit and hit enter")

while True:

	textToSearch = input('Enter your query: ')
	if textToSearch == '/exit':
		print('Good bye!!!')
		break
	query = urllib.parse.quote(textToSearch)
	url = "https://www.youtube.com/results?search_query=" + query
	response = urllib.request.urlopen(url)
	html = response.read()
	soup = BeautifulSoup(html, 'html.parser')
	for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
		link = ('https://youtu.be/' + vid['href'])
		break

	# List of all files in _Music directory
	musicList = os.listdir("_Music")

	# Video ID
	musicID = vid['href'][9:]

	if any(musicID in s for s in musicList):
		command = 'mpg123 _Music/*' + musicID + '.mp3' 
		os.system(command)
	else:
		command = 'youtube-dl -x --audio-format mp3 ' + link +  ' && mv *' + musicID + '.mp3 _Music' + ' && mpg123 _Music/*' + musicID + '.mp3' 
		os.system(command)
