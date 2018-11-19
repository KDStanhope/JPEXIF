#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
standard libs used
Phil Harvey's EXIF Tool does all the heavy lifting
"""
import os, csv, subprocess


def csvIntoMemory():
    llaArray = []
    for files in os.listdir():
        if files.endswith(".csv"):
            csvFile = (os.path.join(files))
    inFile = open(csvFile)
    delim = csv.reader(inFile)
    
    
    for i in delim:
        llaArray.append(i)
        
    inFile.close()
    return llaArray

def filelistIntoMemory():
    jpegArray = []
    for files in os.listdir():
        if files.endswith(".jpeg"):
            jpegArray.append(os.path.join(files))
    return jpegArray

jpegArray = filelistIntoMemory()
llaArray = csvIntoMemory()
thisDir = os.path.dirname(os.path.realpath(__file__))

for i in range(len(llaArray)):
    try:
        alpha = llaArray[i+1][0]
        bravo = llaArray[i+1][1]
        charlie = llaArray[i+1][2]
        delta = llaArray[i+1][3]
        echo = llaArray[i+1][4]
        foxtrot = llaArray[i+1][5]
        golf = llaArray[i+1][6]
        hotel = llaArray[i+1][7]
    except:
        print("array +1 error not an error... carry on")
    try:
        file = jpegArray[i]
    except:
        print("More entries than images... check your data")
        break
    print("RUNNING: " + 'exiftool.exe -"GPSLatitudeRef"='+alpha+' -"GPSLongitudeRef"='+bravo+' -"GPSAltitude"='+hotel+' -"GPSAltitudeRef"='+'A'+' -"CameraSerialNumber"='+delta+' -"GPSLatitude"='+foxtrot+' -"GPSLongitude"='+golf+' '+file)
    os.system('exiftool.exe -"GPSLatitudeRef"='+alpha+' -"GPSLongitudeRef"='+bravo+' -"GPSAltitude"='+hotel+' -"GPSAltitudeRef"='+'A'+' -"CameraSerialNumber"='+delta+' -"GPSLatitude"='+foxtrot+' -"GPSLongitude"='+golf+' -overwrite_original '+file)
