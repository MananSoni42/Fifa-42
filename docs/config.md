This game is written in Python 3.7.0  
***

To set up a local copy, follow the steps given below:

- Install python (3+) and pip  
**Debian**: apt-get install python python3-pip  
**Arch**: pacman -S python python-pip  
**Windows**: Download [Python](https://www.python.org/downloads/windows/) (this [tutorial](https://github.com/BurntSushi/nfldb/wiki/Python-&-pip-Windows-installation) may be helpful)

- Clone this repository  
If you have git, execute:
```  
git clone https://github.com/MananSoni42/Fifa-42.git
```  
otherwise:
Download the [ZIP](https://github.com/MananSoni42/Fifa-42/archive/master.zip) file

- Install the required dependancies
> Ensure that you are inside the Fifa-42 directory
```
pip install -r requirements.txt
```

- Play the game with Python
> Ensure that you are inside the Fifa-42/src directory
```
python3 play.py
```
Done! Now you can make your own changes to the game.

- Various command line arguements are available, see them using
```
python3 play.py --help
```
