import dlib
import cv2
from imutils.video import VideoStream
from imutils import face_utils
import imutils
import os
import time
def take_photo(Name_user):
    PATH = str(Name_user)
    PATH='/home/mauricio/Pictures/usuarios/'+Name_user
    if not os.path.exists(PATH):
        os.makedirs(PATH)
    ##TRAINING-GETTING INPUTS FOR NEURALNETWORK
    print("[INFO] loading facial landmark predictor...")
    detector = dlib.get_frontal_face_detector()
    print("[INFO] camera sensor warming up...")
    vs = VideoStream(src=1).start()
    # vs = VideoStream(usePiCamera=True).start() # Raspberry Pi
    time.sleep(2.0)
    video_capture = cv2.VideoCapture(0)
    flag_photo_taken=False
    count_photos=0
    while True:
        ret, frame = video_capture.read()
        frame = imutils.resize(frame, width=400)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rects = detector(gray, 0)
        if len(rects) > 0:
            for rect in rects:
                (bX, bY, bW, bH) = face_utils.rect_to_bb(rect)
                print( bW)
                if ((bW) == 149):
                    cv2.imwrite(PATH+"/"+Name_user+str(count_photos)+".jpg",frame)
                    count_photos=count_photos+1
                    if count_photos==5000:
                        flag_photo_taken=True
        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if flag_photo_taken:
            break
    cv2.destroyAllWindows()
    vs.stop()
take_photo("Octavio_Garcia")
