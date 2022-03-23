from asyncio.windows_events import NULL
import csv
from email.policy import default
from logging import root
from unittest import result
from exif import Image
from tkinter import Tk, filedialog
from os import listdir
from os.path import isfile, join

#select folder path
root = Tk()
root.withdraw()
folder_path = filedialog.askdirectory()

#create filePathName list
imagePaths = [join(folder_path,f) for f in listdir(folder_path) if isfile(join(folder_path,f))]

#open and wtite data in the same folder as code
imagesGeoTags = open('geoTagCsv.csv','w+')
imagesGeoTags.truncate()
writer = csv.writer(imagesGeoTags)
writer.writerow(["ImagePathName","Latitude","Longitude"])

for imagePath in imagePaths:
    with open(imagePath, 'rb') as img_file:
        img = Image(img_file)
    
    writer.writerow([img_file.name,img.get("gps_latitude",default="NULL"),img.get("gps_longitude",default="NULL")])

imagesGeoTags.close()