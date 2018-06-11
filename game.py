import sys
import platform
import math
import numpy
import re
import socket
import serial
import struct
import time
import select

from bitalino import BITalino

def main():
    
    defaultMACAddress = "20:16:12:21:98:56"

    # Set MAC Address with argument
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

    runningTime = 5

    # Setting other attributes
    batteryThreshold = 30
    acqChannels = [0,1]
    samplingRate = 1000
    nSamples = 10
    digitalOutput = [1,1]

    # Connect to BITalino
    device = BITalino(macAddress)
    
    # Set battery threshold
    device.battery(batteryThreshold)

    # Read BITalino version
    print "Device Version:", device.version()

    # Start Acquisition
    device.start(samplingRate, acqChannels)

    startTime = time.time()
    endTime = time.time()
    
    while (endTime - startTime) < runningTime:
        # While not reaching runningTime, read samples
        rawData = device.read(nSamples)
        portA1 = rawData[:,5]
        print "Port A1: ", portA1
        valueA1 = numpy.mean(abs(portA1 - numpy.mean(portA1)))
        print "Value A1: ", valueA1
        print ""
        portA2 = rawData[:,6]
        print "Port A2: ", portA2
        valueA2 = numpy.mean(abs(portA2 - numpy.mean(portA2)))
        print "Value A2: ", valueA2
        print "\n"
        endTime = time.time()

    # Turn BITalino LED on
    device.trigger(digitalOutput)

    # Stop acquisition
    device.stop()

    # Close connection
    device.close()


if __name__ == "__main__":
    main()
