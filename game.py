"""
License
-------
GNU GENERAL PUBLIC LICENSE v3
2018

Author
------
Sifan Ye
"""

import sys
import os
import platform

import numpy

import time

from bitalino import BITalino

def main():
    
    # OS Specific Initializations
    clearCmd = "cls||clear"

    if platform.system() == 'Windows':
        clearCmd = "cls"
        print "Using Windows default console size 80x24"
        columns = 80
        rows = 24
    else:
        clearCmd = "clear"
        rows, columns = os.popen('stty size', 'r').read().split()

    print "Connecting to BITalino..."

    # Set MAC Address with argument
    defaultMACAddress = "20:16:12:21:98:56"

    if len(sys.argv) == 2:
        macAddress = sys.argv[1]
        print "Using address:", macAddress
    elif len(sys.argv) > 1:
        print "Please input only 1 argument, which is the address of the BITalino device."
        print "Running without argument will use default MAC Address =", defaultMACAddress
        print "Exiting..."
        exit()
    else:
        macAddress = defaultMACAddress
        print "Using default MAC address:", macAddress

    # Setting other attributes
    batteryThreshold = 30
    acqChannels = [0,1]
    samplingRate = 100
    nSamples = 20
    digitalOutput = [1,1]

    # Connect to BITalino
    device = BITalino(macAddress)
    
    # Set battery threshold
    device.battery(batteryThreshold)

    # Read BITalino version
    os.system(clearCmd)
    print "Device Version:", device.version()

    # Start Acquisition
    device.start(samplingRate, acqChannels)

    # Take baseline measurement
    p1Base = []
    p2Base = []

    start = time.time()
    end = time.time()

    samplingTime = 15

    print "Sampling for baseline..."

    while (end - start) < samplingTime:
        # Sampling for baseline
        baseSample = device.read(nSamples)
        p1Base.append(numpy.mean(baseSample[:,5]))
        p2Base.append(numpy.mean(baseSample[:,6]))
        end = time.time()

    p1B = numpy.mean(p1Base)
    p2B = numpy.mean(p2Base)

    print "\n"
    p1P = "Player 1 Baseline: " + str(p1B)
    print p1P
    p2P = "Player 2 Baseline: " + str(p2B)
    print p2P


    print("\n\n\n\n\n\n")
    print("Are you ready for the game? Type 'No' to exit".center(int(columns)," "))
    response = sys.stdin.readline().rstrip()
    if response == "No":
        sys.exit()

    print "\n"
    print "Starting Game...".center(int(columns)," ")

    time.sleep(5)


    # Start Game

    os.system(clearCmd)

    gameRunning = True

    player1Progress = 28

    while gameRunning:
        # While not reaching runningTime, read samples
        rawData = device.read(nSamples)
        portA1 = rawData[:,5]
        #print "Port A1: ", portA1
        valueA1 = numpy.mean(portA1 - p1B)
        #print "Value A1: ", valueA1
        #print ""
        portA2 = rawData[:,6]
        #print "Port A2: ", portA2
        valueA2 = numpy.mean(portA2 - p2B)
        #print "Value A2: ", valueA2
        #print "\n"
        if (valueA2 - valueA1) > 10:
            player1Progress-=1
        elif (valueA2 - valueA1) > 20:
            plater1Progress-=2
        elif (valueA1 - valueA2) > 10:
            player1Progress+=1
        elif (valueA1 - valueA2) > 20:
            player1Progress+=2

        print "\n\n"
        print "Player 1 Reading:".center(int(columns)," ")
        print "\n"
        print str(valueA1).center(int(columns)," ")
        print "\n\n\n"

        print "*****************************I*****************************".center(int(columns)," ")
        progress = "P1 *" + ' '*player1Progress + 'O' + ' '*(56-player1Progress) + '* P2'
        print progress.center(int(columns)," ")
        print "*****************************I*****************************".center(int(columns)," ")
        print "\n\n\n"

        print "Player 2 Reading:".center(int(columns)," ")
        print "\n"
        print str(valueA2).center(int(columns)," ")

        time.sleep(0.2)

        os.system(clearCmd)

        if player1Progress == 0:
            print "\n\n\n\n\n"
            print "Player 1 has won".center(int(columns)," ")
            gameRunning = False
        elif player1Progress == 56:
            print "\n\n\n\n\n"
            print "Player 2 has won".center(int(columns)," ")
            gameRunning = False

    # Turn BITalino LED on
    device.trigger(digitalOutput)

    # Stop acquisition
    device.stop()

    # Close connection
    device.close()


if __name__ == "__main__":
    main()
