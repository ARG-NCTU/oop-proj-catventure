# 貓險王 - Catventure
# Description 
In the game, you become a little black cat and your goal is to gather as many cans of cat food as you can. The more cans you collect, the higher your score will be. Along the way, you'll come across traps that make it harder to score, and their number will grow as you play. But don't worry, you'll also find power-up items that boost your abilities and make you even better.

<img src="./oop-proj-catventure.gif"/>

## Getting started
### Ubuntu
Download and run the game
```
$ cd ~
$ git clone git@github.com:ARG-NCTU/oop-proj-17.git
```
Run docker
```
$ cd oop-proj-catventure
$ source docker_run.sh
```
Start the game
```
$ python3 Catventure.py
```
### Windows
Install Anaconda from following site.
https://docs.anaconda.com/free/anaconda/install/windows/
#### Download oop-proj-catventure
Download oop-proj-catventure as a zip, and unzip.
#### activate base env, and start the game
You can change "oop_env" to what ever the name you like.
```
$ conda create --name oop_env python=3.8.10
$ conda activate oop_env
$ pip3 install pygame
$ pip3 install numpy
```
cd to your oop-proj-proj-catventure dir location, and run the game.
```
$ cd oop-proj-proj-catventure
$ python Catventure.py
```
## Controls
1. A - Move left
2. S - Move right
3. D - Drop down
4. Space - Jump
5. Left mouse button - Shoot bullets
## Traps
1. Arrows - Randomly fall from the sky
2. Saws - Randomly spawn on the ground when the score is greater than 5
3. Darts - Randomly generate and bounce around the screen when the score is greater than 10
4. Ghost 1 - Appears when stars are collected and chases the player
5. Ghost 2 - Appears when stars are collected and bounces around the screen
## Items
1. Shield - Grants 3 seconds of invincibility
2. Potion - Increases life by 1, but not exceeding the original life value.
3. Fire - Bullets scatter within 4 seconds
## Records
You can find your score & play time in the Records.txt 
## Additional Information
Hope you enjoy this game!

## Developer

連哲寬/LIEN,CHE-KUAN  
lian.ee11@nycu.edu.tw
