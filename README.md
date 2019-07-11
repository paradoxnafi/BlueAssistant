# BlueAssistant
A assistant bot. Can play music from YouTube.
You will need to give it a query. Bot will search it on YouTube and grab the first result. Then it will download it as mp3 using youtube-dl and store it under \_Music folder.The music will be played using mpg123. If you get the same result again, it will play from local download.
<<<<<<< HEAD

# Install
First you will need python3. To install it, copy paste the command in a terminal.
```
sudo apt install python3
```
Now you only need to run the setup file.
```
sudo python3 setup.py
```
You need root permisson hre. The setup file will first check for update. Then it will install "python3-dev python3-pip wget mpg123" packages and "youtube-dl" pip module.

# Stop
Press CTRL+C to stop a currently playing music. type '/exit' to stop the program.
=======
Press CTRL+C to stop a currently playing music. Type '/exit' to stop the program.
