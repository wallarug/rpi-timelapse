#!/usr/bin/env python

from subprocess import call
from time import sleep
import os

image_count = 1
image_name = "Weather2-"  #set the file name here
#call (["cd /media/raspicam"], shell=True)

print "Program started!"

while True:
	f = open('logfile.txt', 'a')
        call (["raspistill -n -t 1000 -o " + str(image_name) + str(image_count) + ".jpg"], shell=True)
        current_image = str(image_name) + str(image_count) + ".jpg"
	if os.path.exists('/mnt/rpi-share'):
		call (["mv " + str(current_image) + " /mnt/rpi-share/"+str(image_name)+str(image_count)+".jpg"], shell=True)
        	f.write('SUCCEED to save: ' + str(current_image) + ' to /mnt/rpi-share \n')   # change /mnt/rpi-share to a different folder on the network or locally
		print "SUCESS"
	else:
		f.write('FAILED to save: ' +str(current_image)+ ' to /mnt/rpi-share \n') # change /mnt/rpi-share to a different folder on the network or locally
		print "FAIL"
	f.write('Picture taken with name: ' + str(current_image)+ '\n')
	f.close()
	image_count = image_count + 1
        print "Sleeping for 20 seconds... 20s to go"
	sleep(10)
	print "Sleeping for 20 seconds... 10s to go"
	sleep(5)
	print "Sleeping for 15 seconds... 5s to go"
	sleep(5)
	print "Finished Sleeping - taking a picture"
        # change the above for different time interval.



#call (["raspistill -o image.jpg"], shell=True)
#call (["raspivid -o video.h264"], shell=True)
#2592 x 1944.  

