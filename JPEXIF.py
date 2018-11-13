#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module requires libraries:
Use "pip install piexif"
Written for Python 3.6
Software Provided with no licence and entirely in good faith.
"""
import os, csv, piexif
from fractions import Fraction

def dms_conv(val, loc):
    if val < 0:
        locValue = loc[0]
    elif val > 0:
        locValue = loc[1]
    else:
        locValue = ""
    absv = abs(val)
    deg =  int(absv)
    t1 = (absv-deg)*60
    mins = int(t1)
    sec = round((t1 - mins)* 60, 5)
    return (deg, mins, sec, locValue)

def numberFix(number):
    f = Fraction(str(number))
    return (f.numerator, f.denominator)


def set_EXIF(jpeg, lat, lng, alt):

    latDMS = dms_conv(lat, ["S", "N"])
    lngDMS = dms_conv(lng, ["W", "E"])

    final_lat = (numberFix(latDMS[0]), numberFix(latDMS[1]), numberFix(latDMS[2]))
    final_lng = (numberFix(lngDMS[0]), numberFix(lngDMS[1]), numberFix(lngDMS[2]))

    gps_ifd = {
        piexif.GPSIFD.GPSVersionID: (2, 0, 0, 0),
        piexif.GPSIFD.GPSAltitudeRef: 1,
        piexif.GPSIFD.GPSAltitude: numberFix(round(alt)),
        piexif.GPSIFD.GPSLatitudeRef: latDMS[3],
        piexif.GPSIFD.GPSLatitude: final_lat,
        piexif.GPSIFD.GPSLongitudeRef: lngDMS[3],
        piexif.GPSIFD.GPSLongitude: final_lng,
    }

    exif_dict = {"GPS": gps_ifd}
    exif_bytes = piexif.dump(exif_dict)
    piexif.insert(exif_bytes, jpeg)

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

## messy but it flows nicely down here

jpegArray = filelistIntoMemory()
llaArray = csvIntoMemory()

try:
    for k in range(len(llaArray)):
        set_EXIF(jpegArray[k],float(llaArray[k][0]),float(llaArray[k][1]),float(llaArray[k][2]))
    input("Seems Complete... press Return")
             
except:
    print("Something broke, sorry. Try checking your input data?")
    input("...press Return")
