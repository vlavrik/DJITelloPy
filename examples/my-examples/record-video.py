#from time import time
import time
from djitellopy import Tello
import cv2

tello = Tello()

tello.connect()
print(tello.get_battery())
tello.streamon()

resolution = (640, 480)

video = cv2.VideoWriter('video.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, resolution)

while True:
    img = tello.get_frame_read().frame
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # print(img.shape)
    img = cv2.resize(img, resolution)
    
    cv2.imshow('my-stream', img)
    video.write(img)
    cv2.waitKey(1)

    # print(img.shape)
    # time.sleep(1)

    

