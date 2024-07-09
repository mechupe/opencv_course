import os
import cv2
import sys

s = 0

net = cv2.dnn.readNetFromCaffe('../data/models/deploy.prototxt', '../data/models/15aa726b4d46d9f023526d85537db81cbc8dd566/opencv_face_detector.caffemodel')

cap = cv2.VideoCapture(s)
win_name = "Camera Preview"
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
alive = True
if not cap.isOpened():
    print('Capture isn"t opened')
    sys.exit(0)

while alive :
    key = cv2.waitKey(1)
    ret, frame = cap.read()
    frame_width = frame.shape[0]
    frame_height = frame.shape[1]

    if not ret or key in (ord('q'), ord('Q'), 27):
        alive = False

    blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300), [104, 117, 123], False, False)
    net.setInput(blob)
    detections = net.forward()[0, 0, 0, :]
    confidence = detections[2]
    if confidence >= 0.7:
        x_left_up = int(detections[3] * frame_height)
        y_left_up = int(detections[4] * frame_width)
        x_right_down = int(detections[5] * frame_height)
        y_right_down = int(detections[6] * frame_width)

    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 0.5
    thickness = 1

    text = "What a handsome Man"
    size, baseline = cv2.getTextSize(text, font, fontScale, thickness)

    width, height = size

    # break
    cv2.rectangle(frame, pt1=(x_left_up, y_left_up), pt2=(x_left_up + width, y_left_up + height), color=(255, 255 ,255), thickness=cv2.FILLED)
    cv2.putText(frame, text, (x_left_up, y_left_up + height), font, fontScale, color= (0, 0 , 0), thickness=thickness)
    cv2.rectangle(frame, pt1=(x_left_up, y_left_up), pt2=(x_right_down, y_right_down), color=(255, 0 ,0), thickness=3)
    cv2.imshow(win_name, frame)
cap.release()
cv2.destroyAllWindows(win_name)
    