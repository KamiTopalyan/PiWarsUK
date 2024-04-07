import cv2
import numpy as np
import RPi.GPIO as GPIO

# Camera setup
cap = cv2.VideoCapture(0)
cap.set(3, 160)
cap.set(4, 120)

# GPIO pins to be set
in1 = 4
in2 = 17
in3 = 27
in4 = 22
en1 = 23
en2 = 24

# Change board depending on what pin format
# you will use refer to https://pinout.xyz/
GPIO.setmode(GPIO.BCM)

# Set up GPIO pins
GPIO.setup(en1, GPIO.OUT)
GPIO.setup(en2, GPIO.OUT)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
p1 = GPIO.PWM(en1, 100)
p2 = GPIO.PWM(en2, 100)
p1.start(50)
p2.start(50)
GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
GPIO.output(in3, GPIO.LOW)
GPIO.output(in4, GPIO.LOW)

while True:
    #read camera feed
    ret, frame = cap.read()
    
    #Tweak thresholds to allow a different shade of black
    # Tweak especially if the line is not being detected
    low_b = (80,80,80)
    high_b = (0,0,0)
    
    mask = cv2.inRange(frame, high_b, low_b)
    contours, hierarchy = cv2.findContours(mask, 1, cv2.CHAIN_APPROX_NONE)
    if len(contours) > 0 :
        c = max(contours, key=cv2.contourArea)
        M = cv2.moments(c)
        if M["m00"] !=0 :
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            print("CX : "+str(cx)+"  CY : "+str(cy))
            if cx >= 120 :
                print("Turn Left")
                GPIO.output(in1, GPIO.HIGH)
                GPIO.output(in2, GPIO.LOW)
                GPIO.output(in3, GPIO.LOW)
                GPIO.output(in4, GPIO.HIGH)
            if cx < 120 and cx > 40 :
                print("On Track")
                GPIO.output(in1, GPIO.HIGH)
                GPIO.output(in2, GPIO.LOW)
                GPIO.output(in3, GPIO.HIGH)
                GPIO.output(in4, GPIO.LOW)
            if cx <=40 :
                print("Turn Right")
                GPIO.output(in1, GPIO.LOW)
                GPIO.output(in2, GPIO.HIGH)
                GPIO.output(in3, GPIO.HIGH)
                GPIO.output(in4, GPIO.LOW)
            cv2.circle(frame, (cx,cy), 5, (255,255,255), -1)
    else :
        print("No Line")
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.LOW)
        GPIO.output(in3, GPIO.LOW)
        GPIO.output(in4, GPIO.LOW)
    cv2.drawContours(frame, c, -1, (0,255,0), 1)
    
    #Comment out to disbale windows popping up
    cv2.imshow("Mask",mask)
    cv2.imshow("Frame",frame)
    
    #Exit sequence
    if cv2.waitKey(1) & 0xff == ord('q'):
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.LOW)
        GPIO.output(in3, GPIO.LOW)
        GPIO.output(in4, GPIO.LOW)
        break
    
#Stop Camera Feed
cap.release()
cv2.destroyAllWindows()

