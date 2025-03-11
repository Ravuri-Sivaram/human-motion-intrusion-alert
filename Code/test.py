import cv2
import imutils
import numpy as np
import threading
from playsound import playsound
import mail

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Camera not found!")
    exit()

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

_, start_frame = cap.read()

# Check if the first frame is captured properly
if start_frame is None:
    print("Error: Failed to capture initial frame!")
    cap.release()
    exit()

start_frame = imutils.resize(start_frame, width=500)
start_frame = cv2.cvtColor(start_frame, cv2.COLOR_BGR2GRAY)
start_frame = cv2.GaussianBlur(start_frame, (21, 21), 0)

alarm = False
alarm_mode = False
alarm_counter = 0

def beep_alarm():
    global alarm
    while alarm_mode:
        print("ALARM")
        playsound('alarm.mp3')

while True:
    _, frame = cap.read()
    
    # If the frame is not captured successfully, break
    if frame is None:
        print("Error: Failed to capture image from camera.")
        break

    frame = imutils.resize(frame, width=500)

    if alarm_mode:
        frame_btw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame_btw = cv2.GaussianBlur(frame_btw, (5, 5), 0)

        difference = cv2.absdiff(start_frame, frame_btw)
        threshold = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)[1]
        start_frame = frame_btw

        if threshold.sum() > 10000:  
            alarm_counter += 1
            if alarm_counter > 20:
                if not alarm:
                    alarm = True
                    threading.Thread(target=beep_alarm).start()
                    threading.Thread(target=mail.send_email, args=(frame, frame, frame, frame, frame)).start()
        else:
            if alarm_counter > 0:
                alarm_counter -= 1
        cv2.imshow("Cam", threshold)
    elif not alarm_mode and alarm:
        black_frame = np.zeros_like(frame)
        cv2.imshow("Cam", black_frame)
    else:
        cv2.imshow("Cam", frame)

    key_pressed = cv2.waitKey(30)
    if key_pressed == ord('t'):
        print("You have activated/deactivated the alarm!")
        alarm_mode = not alarm_mode
        alarm_counter = 0
    elif key_pressed == ord('q'):
        print("Quitting the program!")
        alarm_mode = False
        break

cap.release()
cv2.destroyAllWindows()
