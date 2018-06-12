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
    samplingRate = 1000
    nSamples = 50
    digitalOutput = [1,1]

    # Connect to BITalino
    device = BITalino(macAddress)
    
    # Set battery threshold
    device.battery(batteryThreshold)

    # Read BITalino version
    os.system(clearCmd)
    print "Device Version:", device.version()
    
    print("\n\n\n\n\n\n")
    response = raw_input("Are you ready for the game? Type 'No' to exit".center(int(columns)," "))
    if response == "No":
        sys.exit()

    # Start Acquisition
    device.start(samplingRate, acqChannels)

    gameRunning = True

    player1Progress = 16

    while gameRunning:
        # While not reaching runningTime, read samples
        rawData = device.read(nSamples)
        portA1 = rawData[:,5]
        #print "Port A1: ", portA1
        valueA1 = numpy.mean(abs(portA1 - numpy.mean(portA1)))
        #print "Value A1: ", valueA1
        #print ""
        portA2 = rawData[:,6]
        #print "Port A2: ", portA2
        valueA2 = numpy.mean(abs(portA2 - numpy.mean(portA2)))
        #print "Value A2: ", valueA2
        #print "\n"
        if valueA1 < valueA2:
            player1Progress-=1
        print "\n\n\n\n"
        print "Player 1 Reading:\t\t\t\tPlayer 2 Reading:".center(int(columns)," ")
        print "\n"
        print "%16d\t\t\t\t%16d".center(int(columns)," ") % (valueA1, valueA2)
        print "\n\n\n"
        print "*****************I*****************".center(int(columns)," ")
        progress = "*" + ' '*player1Progress + 'O' + ' '*(32-player1Progress) + '*'
        print progress.center(int(columns)," ")
        print "*****************I*****************".center(int(columns)," ")
        time.sleep(0.05)
        os.system(clearCmd)
        if player1Progress == 0:
            print "\n\n\n\n\n"
            print "Player 1 has won".center(int(columns)," ")
            gameRunning = False
        elif player1Progress == 32:
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
