import cv2;         
import pyfirmata;    

cap = cv2.VideoCapture(0);
cap.set(3, 640);
cap.set(4, 420);

board=pyfirmata.Arduino('COM4');

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml");

while True:
    success, img = cap.read();
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);

    faces = faceCascade.detectMultiScale(imgGray, 1.3, 5);

    if(len(faces) >0):
        for (x, y, w, h) in faces:
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0,0, 255), 3);
            board.digital[13].write(1);
    else:
        board.digital[13].write(0);

    cv2.imshow('face_detect', img);
    if cv2.waitKey(1) == ord('q'):
        break

board.digital[13].write(0);
cap.release();

