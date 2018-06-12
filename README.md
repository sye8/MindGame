# MindGame (Work In Progress)
### A strange game. You win by not thinking about it.
*Note that this game does not work on macOS*

Using a BITalino device, this game compares the EEG readings of the two players. Like the rules of a tug-of-war, the player who gives a lower EEG reading than the opponent for a long enough time wins the game.


*Note that this is a TTY game, please don't expect any graphics*


## Dependencies
* [Python >2.7](https://www.python.org/downloads/) or [Anaconda](https://www.continuum.io/downloads)
* [NumPy](https://pypi.python.org/pypi/numpy)
* [pySerial](https://pypi.python.org/pypi/pyserial)
* [pyBluez](https://pypi.python.org/pypi/PyBluez/)
* [BitalinoAPI](https://github.com/BITalinoWorld/revolution-python-api) (When running, please place into the same folder as game.py)

## Device Required:

A BITalino with bluetooth enabled and two EEG sensors connecting to channel A1 and A2. The terminal should have bluetooth capabilities


**The python script has been tested on Ubuntu MATE on Raspberry Pi 3 Model B**


*The game is so far only tested with two ACC sensors. EEG testing pending*
