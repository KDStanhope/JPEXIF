<H1>exiftool Batch</H1>

This is an add on and a little bit messy but it gets the job done. 

<H2><b>Preface:</b></H2>

The tags embedded in the jpeg files produced by FLIR cameras are not open. They still contain the standard jpeg exif tags but the header contains extra bytes in order to extend the number of tags available. A brief bit of reverse engineering shows that at byte 0x06 we have a file format indicator of sorts: 'JFIF'
Somewhere around 0x19 we have 'FLIR' 
etc etc

A lot of trial and error shows that at 0x002b we can find the GPS info and at 0x0020 we can find all the FLIR specific stuff

Implementing a python library that reads, decodes and identifies all the known and not known tags is a big job involving a lot of reverse engineering. 

Luckily Phil Harvey did a lot of the heavy lifting for us. 

EXIFtool allows us to write these FLIR specific tags so this script pulls information from a csv and an image list and compiles the correct command line argument and pipes it to windows command prompt. For every image. 

<H2><b>Usage:</b></H2>

It is VERY IMPORTANT that you place exiftools.exe in the same folder as your images, your csv and the exiftool_batch_parse.py
CSV needs to be in the format:

        GPSLatRef,GPSLongRef,GPSAltRef,CameraSerialNumber,FocusDistance,GPSLat,GPSLong,GPSAltitude,
        S,E,Above Sea Level,55002383,0.075m,27.0709564973753,-22.3959007370108,1788.437
        S,E,Above Sea Level,55002383,0.075m,27.0715361636981,-22.3959617750669,1788.121
        S,E,Above Sea Level,55002383,0.075m,27.0726994921811,-22.3960759447445,1788.297
        S,E,Above Sea Level,55002383,0.075m,27.073282123073 ,-22.3961302609259,1788.868
        S,E,Above Sea Level,55002383,0.075m,27.0738646642463,-22.3961867450806,1789.600
        
        
The header items and ordering are essential. 

The number of images and the number of entries in the CSV should match. 






<H1># JPEXIF</H1>

  
<h1>Python Script to Insert GPS Location into JPEG EXIF Header</h1>

<H4><b>Dirt Simple Tools.</b></H4>

<H2><b>Usage:</b></H2>

Copy JPEXIF.py to the folder that has your .jpeg files and your .csv and double click to run.

          --or--
          
Run from within IDLE/Arc/JetBrains interpreter.



<H2><b>Prerequisites:</b></H2>

* Python 3.6 
* pyexif (https://pypi.org/project/piexif/#files) or install from command line using pip install pyexif.
* one of more Jpeg file.
* a CSV list in the format lat, long, altitude. 


<H2><b>Conditions:</b></H2>

* The CSV MUST contain only lat, long, altitude in the format: 

          27.0738646642463,-22.3961867450806,1789.600
          27.073282123073 ,-22.3961302609259,1788.868
          ...
          
* The script will assign information from the 1st line of the CSV to the 1st image in the list:

        image_001.jpeg ---> row 1
        image_002.jpeg ---> row 2
        image_258.jpeg ---> row 258

* If there are only 500 rows and 600 images, only the first 500 images will be allocated GPS EXIF data.
* The file extensions are important. ONLY .jpeg and .csv are accepted.



<H2><b>Comments:</b></H2>

A <b>far more</b> robust solution would be to generate a CSV with an ID column that can tie the coordinates to the jpeg files. This will solve any issues relating to OS specific filename sorting. intergrating such a change to the script would be simple but as it stands it works just fine provided conditions are met.
