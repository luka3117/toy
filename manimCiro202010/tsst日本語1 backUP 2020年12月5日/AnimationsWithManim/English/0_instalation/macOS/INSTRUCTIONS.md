# Installation on MacOS

Link to [video tutorial](https://www.youtube.com/watch?v=uZj_GQc6pN4).

## Install dependencies.

### Open a terminal 
Search "terminal" on Spotlight

<p align="center"><img src ="/English/0_instalation/macOS/gifs/terminal.png" /></p>

### Install Homebrew
Copy the code from [Homebrew](https://brew.sh) and paste it in the terminal

<p align="center"><img src ="/English/0_instalation/macOS/gifs/MacP1.gif" /></p>

### Install LaTeX (versión completa)
Go to [MacTeX](http://www.tug.org/mactex/), download the .pkg file and install it ([help](https://www.youtube.com/watch?v=5CNmIaRxS20)).

<p align="center"><img src ="/English/0_instalation/macOS/gifs/MacP2.gif" /></p>

### Install Python 3
Go to the official website of [Python](https://www.python.org/), and download the 3.7 version ([help](https://www.youtube.com/watch?v=0hGzGdRQeak)).

<p align="center"><img src ="/English/0_instalation/macOS/gifs/MacP3.gif" /></p>

### Install PIP
Run the follow commands:

```sh
brew install curl
mkdir ManimInstall
cd ManimInstall
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
```

### Install FFmpeg, SoX and Cairo.
Run the follow commands:

#### FFmpeg
```sh
brew install ffmpeg
```
#### Sox
```sh
brew install sox
```
#### More packages
```sh
brew install cairo
```

If that does not works use:

```sh
brew install cairo --use-clang
```

```sh
brew install py2cairo
```

```sh
brew install pkg-config
```

<p align="center"><img src ="/English/0_instalation/macOS/gifs/MacP5.gif" /></p>

### Download Manim from [actual version](https://github.com/3b1b/manim), or [3/Feb/2019 version](https://github.com/3b1b/manim/tree/3b088b12843b7a4459fe71eba96b70edafb7aa78).

<p align="center"><img src ="/English/0_instalation/macOS/gifs/DescargarManim.gif" /></p>

### Unzip the file into a directory that does not have spaces

<p align="center"><img src ="/English/0_instalation/macOS/gifs/pd.png" /></p>

### Install list requirements.txt
Move the terminal to manim-master folder and run this:

```sh
python3 -m pip install pyreadline
python3 -m pip install pydub
```

#### Download the rest
Open `requirements.txt` and replace the content with [this](https://github.com/3b1b/manim/blob/master/requirements.txt) and use:

```
python3 -m pip install -r requirements.txt
```

<p align="center"><img src ="/English/0_instalation/macOS/gifs/MacP6.gif" /></p>

# Run Manim

With the terminal in manim-master directory run this:

```sh
python3 -m manim example_scenes.py WriteStuff -pl
```

That command have to build the follow video:

<p align="center"><img src ="/English/0_instalation/macOS/gifs/MacP8.gif" /></p>

