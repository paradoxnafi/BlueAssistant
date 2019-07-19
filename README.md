# BlueAssistant
A assistant bot. Can play music from YouTube.
You will need to give it a query. Bot will search it on YouTube and grab the first result. Then it will download it as mp3 using youtube-dl and store it under \_Music folder.The music will be played using mpg123. If you get the same result again, it will play from local download.

# Install
To install the requirments, copy paste the command in a terminal.
```
sudo apt install python3 python3-dev python3-pip git wget mpg123 ffmpeg -y
```
Now install two python module
```
sudo pip3 install beautifulsoup4
sudo pip3 install youtube-dl
```
Finally, clone this repository
```
git clone https://github.com/paradoxnafi/BlueAssistant.git
cd BlueAssistant 
chmod +x play_from_youtube.py
```
# Run
```
./play_from_youtube.py
```
# Stop
Press CTRL+C to stop a currently playing music. Type '/exit' to stop the program.
