from time import time
import datetime
from picamera import PiCamera
from fractions import Fraction
from time import sleep
from PIL import Image

camera = PiCamera()
camera.iso=800
#camera.shutter_speed = 6000000
#camera.abw_gains = g
print(camera.exposure_speed)

sleep(2)

logFile = open('data.log', 'w')
logFile.write("Time,Counter\n")

camera.shutter_speed = 6000000#camera.exposure_speed 
camera.awb_mode = 'off'
while(True):

    v = 0
    for u in range(30):
        camera.capture('./image.png')

        im = Image.open('./image.png')

        (a, b) = im.size

        for i in range(a):
            for j in range (b):
                (r, g, b, t) =  im.getpixel((i, j)) 
                v +=  (r+g+b)
    print(v)
    now = datetime.datetime.now()	
    logFile.write("{0},{1}\n".format(now, v))
    logFile.flush()
