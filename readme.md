<h1 align="center">Block Blaster 3000!</h1>

<p align="center">
  <a href="https://codeclimate.com/github/arbauman/Block-Blaster-3000"><img src="https://img.shields.io/codeclimate/github/arbauman/Block-Blaster-3000.svg?style=flat-square" alt="Code Climate" /></a>
  <a href="https://github.com/arbauman/Block-Blaster-3000/issues"><img src="https://img.shields.io/github/issues-raw/arbauman/Block-Blaster-3000.svg?style=flat-square" alt="" /></a>
  <a href="https://github.com/arbauman/Block-Blaster-3000/graphs/contributors"><img src="https://img.shields.io/github/contributors/arbauman/Block-Blaster-3000.svg?style=flat-square" alt="GitHub contributors" /></a>
  <a href="https://github.com/arbauman/Block-Blaster-3000/blob/master/license"><img src="https://img.shields.io/github/license/arbauman/Block-Blaster-3000.svg?style=flat-square" alt="license" /></a>
</p>

<p align="center">
  <img src="https://i.imgur.com/L1Cq6W0.gif" alt="" />
</p>

2D recreation of Blockout written in Python using Livewires.
Requires Python 2.6.6 32-bit, Pygame 1.9.1 32-bit, and Livewires 2.0.

###Installation
Python 2.6.6 can be downloaded from [here](https://www.python.org/download/releases/2.6.6/)

Pygame 1.9.1 can be downloaded from [here](http://www.pygame.org/download.shtml)  Be sure to download the version intended for Python 2.6

As Livewires 2.0 does not seem to be available anymore, I've bundled it with this program.  Livewires 2.1 seems to change a lot in games.py, so this seems to be a quicker solution.  To install, you just need to copy the "livewires" folder containing 
- "init.py"
- "beginners.py"
- "color.py"
- "games.py" 

into your Python26/Lib folder.  

###How to Run
- Rename "Block Blaster 3000.py" as "Block Blaster 3000.pyw"
- Simply double-click on "Block Blaster 3000.pyw"

###Instructions
Left Arrow Key - Move Paddle Left
Right Arrow Key - Move Paddle Right

###Objective
Destroy as many blocks as possible, while 
keeping the ball in play.  The ball will 
leave play if it falls below the Paddle.

Each block has a different "hardness".
- Blue = 1 hit
- Red = 2 hits
- Cyan = 3 hits

Once you destroy a set of blocks, new blocks
will automatically be generated!  How long 
can you survive?

Note: This repository does not include assets necessary to play the game.  

###MISSING ASSETS

-gameover.wav

-hit1.wav
