import cv2
import pyfirmata
from simple_facerec import SimpleFacerec

board = pyfirmata.Arduino('COM4')
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    face_locations, face_names = sfr.detect_known_faces(frame)

    if(len(face_names) > 0):
        for face_loc, name in zip(face_locations, face_names):
            y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
            cv2.putText(frame, name, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)
            if(name == "Kousik Roy"):
                board.digital[13].write(1)
            else:
                board.digital[13].write(0)
    else:
        board.digital[13].write(0)

    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) == ord('q'):
        break

board.digital[13].write(0)
cap.release()
cv2.destroyAllWindows()
