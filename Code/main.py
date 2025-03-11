import cv2
import face_recognition
import numpy as np
import os
from playsound import playsound
import threading


KNOWN_FACES_DIR = "known_faces"  
ALARM_SOUND = "alarm.mp3"  

known_face_encodings = []
known_face_names = []

print("Loading known faces...")

for filename in os.listdir(KNOWN_FACES_DIR):
    image_path = os.path.join(KNOWN_FACES_DIR, filename)
    image = face_recognition.load_image_file(image_path)
    encoding = face_recognition.face_encodings(image)[0]  
    known_face_encodings.append(encoding)
    known_face_names.append(os.path.splitext(filename)[0])  
print(f"Loaded {len(known_face_encodings)} known faces.")


def trigger_alarm():
    playsound(ALARM_SOUND)


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Camera not found!")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture image from the camera. Please check the connection.")
        break

    
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.5)
        name = "Unknown"

        if True in matches:
            match_index = matches.index(True)
            name = known_face_names[match_index]  
        else:
            print("⚠ ALERT! Unknown person detected! ⚠")
            threading.Thread(target=trigger_alarm, daemon=True).start()  

        
        top, right, bottom, left = face_location
        color = (0, 255, 0) if name != "Unknown" else (0, 0, 255)  
        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

    cv2.imshow("Face Recognition Alarm", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):  
        break

cap.release()
cv2.destroyAllWindows()
