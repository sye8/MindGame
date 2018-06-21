# MindGame
### A strange game. You win by not thinking about it.
*Note that this game does not work on macOS*

Using a BITalino device, this game compares the EEG readings of the two players. Like the rules of a tug-of-war, the player who gives a lower EEG reading than the opponent for a long enough time wins the game.


*Note that this is a TTY game, please don't expect any graphics*

***Note that apparently the BitalinoAPI is written in Python 2 syntax. So if you only have Python 3, please install Python 2***


## Dependencies
* [Python >2.7](https://www.python.org/downloads/) or [Anaconda](https://www.continuum.io/downloads)
* [NumPy](https://pypi.python.org/pypi/numpy)
* [pySerial](https://pypi.python.org/pypi/pyserial)
* [pyBluez](https://pypi.python.org/pypi/PyBluez/)
* [BitalinoAPI](https://github.com/BITalinoWorld/revolution-python-api)

### To install Dependencies:
**For Python 2.7**

```sh
sudo apt-get install python python-dev python-pip bluez libbluetooth-dev
sudo pip install numpy pyserial pybluez bitalino
git clone https://github.com/BITalinoWorld/revolution-python-api.git
cd revolution-python-api
sudo python setup.py install
```
*(For pip2.7) Note that if your pip complains about `no module named _internal` or `no module named internal`:*

```sh
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
sudo python get-pip.py --force-reinstall
```

**For Python 3**
```sh
sudo apt-get install python3 python3-dev python3-pip bluez libbluetooth-dev
sudo pip3 install numpy pyserial pybluez bitalino
```

**Note here we are not cloning the official BITalino git repo since we are using their old API for Python 3 support, which I have included in this repo. (Thanks to [Gautam Sawala](https://github.com/gautamsawala) for this suggestion)**


## Device Required:

A BITalino with bluetooth enabled and two EEG sensors connecting to channel A1 and A2. The terminal should have bluetooth capabilities


## Compatibility Note
**This python script has only been tested on Ubuntu MATE on Raspberry Pi 3 Model B**
