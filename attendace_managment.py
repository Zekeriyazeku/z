import kivy
import face_recognition
import cv2
import numpy as np
import os
from datetime import datatime

video_capture = cv2.videocapture(0)

zekeriya_image = face_recognition.load_image_file("photo/zekeriya.jpg")
zekeriya_camera = face_recognition.face_encoding(zekeriya_image)[0]

muhammed_image = face_recognition.load_image_file("photo/muhammed.jpg")
muhamed_camera = face_recognition.face_encoding(muhammed_image)[0]

ruman_image = face_recognition.load_image_file("photo/ruman.jpg")
ruman_camera = face_recognition.face_encoding(ruman_image)[0]
know_faces_names =[
"zekeriya",
"muhammed",
"ruman"
]
student = know_face_names.copy()
# use for the faces comes from the video captured
face_location = []
face_encoding = []
face_name = []
s=True
time= datetime.now()
current_date = now.strftime("%Y-%m-%d")


f =open(current_date='.csv','w+',newline= '')
lnwriter =csvwriter(f)
while True:
    frame =video_capture.read()
    small_frame =csv.resize(frame,(0,0),fx=0.25,fy=0.25)
    rgb_small_frame = small_frame[:,:,::-1]
    if s:
        face_location =face_recognition.face_location(rgb_small_frame)
        face_encoding = face_recognition.face_encoding(rgb_small_frame,face_location)
        face_name = []
        for face_encoding in face_encoding:
            matches = face_recogniyion.compare_face(known_face_encoding,face_encoding)
            name =""
            face_distance face_recognition.face_distance(known_face_encoding,face_encoding)
            best_match_index =np.argmin(face_distance)
            if matches
            name = known face_name[best_match_index]

            face_names.append(name)
            if name in known_faces_names:
                if name in student:
                    student.remove(name)
                    print(student)
                    current_time = now.strftime("%H-%m-%s")
                    inwriter.writerrow([name,current_time])
    cv2.imshow("zeki's attendance system",frame)
    if cv2.waitkey(1) &0xFF ==ord('q'):
        break
video_capture.release()
cv2.ddestroyaiwindiws()



