<H1># JPEXIF
  
Python Script to Insert GPS Location into JPEG EXIF Header</h1>

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
          
* The script will assing information from the 1st line of the CSV to the 1st image in the list:

        image_001.jpeg ---> row 1
        image_002.jpeg ---> row 2
        image_258.jpeg ---> row 258

* If there are only 500 rows and 600 images, only the first 500 images will be allocated GPS EXIF data.
* The file extensions are important. ONLY .jpeg and .csv are accepted.

