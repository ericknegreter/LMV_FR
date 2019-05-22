import numpy as np
import dlib
import cv2
from imutils.video import VideoStream
from imutils import face_utils
import imutils
import os
import glob
import time
import tflearn
import math
import json

#For connection to the server
import mysql.connector
from mysql.connector import Error
import subprocess, datetime

hosts = ('google.com', 'kernel.org', 'yahoo.com')
localhost = ('10.0.5.246')
e_lab = ["Octavio_Garcia", "Roberto_x", "Mauricio_x", "Antony_Venancio", "Erick_Negrete"]

def ping(host):
    ret = subprocess.call(['ping', '-c', '3', '-W', '5', host],
            stdout=open('/dev/null', 'w'),
            stderr=open('/dev/null', 'w'))
    return ret == 0

def net_is_up():
    print("[%s] Checking if network is up..." % str(datetime.datetime.now()))

    xstatus = 1
    for h in hosts:
        if ping(h):
            if ping(localhost):
                print("[%s] Network is up..." % str(datetime.datetime.now()))
                xstatus = 0
                break

    if xstatus:
        time.sleep(10)
        print("[%s] Network is down..." % str(datetime.datetime.now()))
        time.sleep(25)

    return xstatus

def camera_recognition():
    faces=[]
    count_faces=0
    number_test=0
    with open('home/erickpc/LMV_FR/bd_FR/data.json', encoding='utf-8') as json_data:
        dict_user = json.load(json_data)

    net = tflearn.input_data(shape=[None, 47])
    net = tflearn.fully_connected(net, 32)
    net = tflearn.fully_connected(net, 64)
    net = tflearn.fully_connected(net, 128)
    net = tflearn.fully_connected(net, 256)
    net = tflearn.fully_connected(net, 17, activation='softmax')
    net = tflearn.regression(net)
    # Define model
    model = tflearn.DNN(net)
    # Start training (apply gradient descent algorithm)
    model.load("model_FR_BS.tflearn")


    print("[INFO] loading facial landmark predictor...")
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("land_mark/shape_predictor_68_face_landmarks.dat")

    print("[INFO] camera sensor warming up...")
    vs = VideoStream(src=1).start()
    # vs = VideoStream(usePiCamera=True).start() # Raspberry Pi
    time.sleep(2.0)
    video_capture = cv2.VideoCapture(0)
    flag_photo_taken=False
    count_photos=0
    count = 0
    while True:
        test_points = []
        ret, frame = video_capture.read()
        frame = imutils.resize(frame, width=400)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        rects = detector(gray, 0)
        if len(rects) ==1:

            for rect in rects:

                (bX, bY, bW, bH) = face_utils.rect_to_bb(rect)
                #print( bW)
                if ((bW) == 149):
                    shape = predictor(gray, rect)
                    shape = face_utils.shape_to_np(shape)

                    #OJO IZQUIERDO
                    x1, y1 = shape[36]
                    x2, y2 = shape[37]
                    x3, y3 = shape[38]
                    x4, y4 = shape[39]
                    x5, y5 = shape[40]
                    x6, y6 = shape[41]

                    #OJO DERECHO
                    x7, y7 = shape[42]
                    x8, y8 = shape[43]
                    x9, y9 = shape[44]
                    x10, y10 = shape[45]
                    x11, y11 = shape[46]
                    x12, y12 = shape[47]

                    #NARIZ
                    x13, y13 = shape[30]
                    x14, y14 = shape[31]
                    x15, y15 = shape[35]

                    #BOCA
                    x16, y16 = shape[48]
                    x17, y17 = shape[50]
                    x18, y18 = shape[52]
                    x19, y19 = shape[54]
                    x20, y20 = shape[56]
                    x21, y21 = shape[57]
                    x22, y22 = shape[58]

                    #MENTON
                    x23, y23 = shape[4]
                    x24, y24 = shape[7]
                    x25, y25 = shape[9]
                    x26, y26 = shape[12]

                    #CARA
                    x27, y27 = shape[0]
                    x28, y28 = shape[16]
                    x29, y29 = shape[2]
                    x30, y30 = shape[14]
                    x31, y31 = shape[5]
                    x32, y32 = shape[11]
                    x33, y33 = shape[27]
                    x34, y34 = shape[8]

                    #CEJA IZQUIERDA
                    x35, y35 = shape[17]
                    x36, y36 = shape[19]
                    x37, y37 = shape[21]

                    #CEJA DERECHA
                    x38, y38 = shape[22]
                    x39, y39 = shape[24]
                    x40, y40 = shape[26]

                    #TOTAL
                    x41, y41 = shape[1]
                    x42, y42 = shape[3]
                    x43, y43 = shape[6]
                    x44, y44 = shape[10]
                    x45, y45 = shape[13]
                    x46, y46 = shape[15]
                    x47, y47 = shape[18]
                    x48, y48 = shape[20]
                    x49, y49 = shape[23]
                    x50, y50 = shape[25]

                    #Distancia ojo izquido
                    distance_1 = math.sqrt(
                        (
                                (pow((x1 - x2), 2))
                                +
                                (pow((y1 - y2), 2))
                        )
                    )
                    distance_2 = math.sqrt(
                        (
                                (pow((x2 - x3), 2))
                                +
                                (pow((y2 - y3), 2))
                        )
                    )
                    distance_3 = math.sqrt(
                        (
                                (pow((x3 - x4), 2))
                                +
                                (pow((y3 - y4), 2))
                        )
                    )
                    distance_4 = math.sqrt(
                        (
                                (pow((x1 - x6), 2))
                                +
                                (pow((y1 - y6), 2))
                        )
                    )
                    distance_5 = math.sqrt(
                        (
                                (pow((x6 - x5), 2))
                                +
                                (pow((y6 - y5), 2))
                        )
                    )
                    distance_6 = math.sqrt(
                        (
                                (pow((x5 - x4), 2))
                                +
                                (pow((y5 - y4), 2))
                        )
                    )
                    distance_7 = math.sqrt(
                        (
                                (pow((x4 - x14), 2))
                                +
                                (pow((y4 - y14), 2))
                        )
                    )
                    #Distancias ojo derecho
                    distance_8 = math.sqrt(
                        (
                                (pow((x7 - x8), 2))
                                +
                                (pow((y7 - y8), 2))
                        )
                    )
                    distance_9 = math.sqrt(
                        (
                                (pow((x8 - x9), 2))
                                +
                                (pow((y8 - y9), 2))
                        )
                    )
                    distance_10 = math.sqrt(
                        (
                                (pow((x9 - x10), 2))
                                +
                                (pow((y9 - y10), 2))
                        )
                    )

                    distance_11 = math.sqrt(
                        (
                                (pow((x7 - x12), 2))
                                +
                                (pow((y7 - y12), 2))
                        )
                    )
                    distance_12 = math.sqrt(
                        (
                                (pow((x12 - x11), 2))
                                +
                                (pow((y12 - y11), 2))
                        )
                    )
                    distance_13 = math.sqrt(
                        (
                                (pow((x11 - x10), 2))
                                +
                                (pow((y11 - y10), 2))
                        )
                    )
                    distance_14 = math.sqrt(
                        (
                                (pow((x7 - x15), 2))
                                +
                                (pow((y7 - y15), 2))
                        )
                    )

                    #Distancia Nariz
                    distance_15 = math.sqrt(
                        (
                                (pow((x14 - x13), 2))
                                +
                                (pow((y14 - y13), 2))
                        )
                    )
                    distance_16 = math.sqrt(
                        (
                                (pow((x13 - x15), 2))
                                +
                                (pow((y13 - y15), 2))
                        )
                    )
                    distance_17 = math.sqrt(
                        (
                                (pow((x14 - x15), 2))
                                +
                                (pow((y14 - y15), 2))
                        )
                    )
                    distance_18 = math.sqrt(
                        (
                                (pow((x16 - x14), 2))
                                +
                                (pow((y16 - y14), 2))
                        )
                    )
                    distance_19 = math.sqrt(
                        (
                                (pow((x15 - x19), 2))
                                +
                                (pow((y15 - y19), 2))
                        )
                    )

                    #Distancia Boca
                    distance_20 = math.sqrt(
                        (
                                (pow((x16 - x17), 2))
                                +
                                (pow((y16 - y17), 2))
                        )
                    )
                    distance_21 = math.sqrt(
                        (
                                (pow((x17 - x18), 2))
                                +
                                (pow((y17 - y18), 2))
                        )
                    )
                    distance_22 = math.sqrt(
                        (
                                (pow((x18 - x19), 2))
                                +
                                (pow((y18 - y19), 2))
                        )
                    )
                    distance_23 = math.sqrt(
                        (
                                (pow((x16 - x22), 2))
                                +
                                (pow((y16 - y22), 2))
                        )
                    )
                    distance_24 = math.sqrt(
                        (
                                (pow((x22 - x20), 2))
                                +
                                (pow((y22 - y20), 2))
                        )
                    )
                    distance_25 = math.sqrt(
                        (
                                (pow((x20 - x19), 2))
                                +
                                (pow((y20 - y19), 2))
                        )
                    )
                    distance_26 = math.sqrt(
                        (
                                (pow((x23 - x16), 2))
                                +
                                (pow((y23 - y16), 2))
                        )
                    )
                    distance_27 = math.sqrt(
                        (
                                (pow((x19 - x26), 2))
                                +
                                (pow((y19 - y26), 2))
                        )
                    )
                    #Menton
                    distance_28 = math.sqrt(
                        (
                                (pow((x23 - x24), 2))
                                +
                                (pow((y23 - y24), 2))
                        )
                    )
                    distance_29 = math.sqrt(
                        (
                                (pow((x24 - x25), 2))
                                +
                                (pow((y24 - y25), 2))
                        )
                    )
                    distance_30 = math.sqrt(
                        (
                                (pow((x25 - x26), 2))
                                +
                                (pow((y25 - y26), 2))
                        )
                    )
                    distance_31 = math.sqrt(
                        (
                                (pow((x24 - x21), 2))
                                +
                                (pow((y24 - y21), 2))
                        )
                    )
                    distance_32 = math.sqrt(
                        (
                                (pow((x21 - x25), 2))
                                +
                                (pow((y21 - y25), 2))
                        )
                    )
                    distance_33 = math.sqrt(
                            (
                                (pow((x23 - x1), 2))
                                +
                                (pow((y23 - y1), 2))
                        )
                    )
                    distance_34 = math.sqrt(
                        (
                                (pow((x26 - x10), 2))
                                +
                                (pow((y26 - y10), 2))
                        )
                    )

                    #Distancia cara
                    distance_35 = math.sqrt(
                        (
                                (pow((x27 - x28), 2))
                                +
                                (pow((y27 - y28), 2))
                        )
                    )
                    distance_36 = math.sqrt(
                        (
                                (pow((x29 - x30), 2))
                                +
                                (pow((y29 - y30), 2))
                        )
                    )
                    distance_37 = math.sqrt(
                        (
                                (pow((x31 - x32), 2))
                                +
                                (pow((y31 - y32), 2))
                        )
                    )
                    distance_38 = math.sqrt(
                        (
                                (pow((x33 - x34), 2))
                                +
                                (pow((y33 - y34), 2))
                        )
                    )

                    #Distancia ceja izquierda
                    distance_39 = math.sqrt(
                        (
                                (pow((x35 - x36), 2))
                                +
                                (pow((y35 - y36), 2))
                        )
                    )
                    distance_40 = math.sqrt(
                        (
                                (pow((x35 - x37), 2))
                                +
                                (pow((y35 - y37), 2))
                        )
                    )
                    distance_41 = math.sqrt(
                        (
                                (pow((x36 - x37), 2))
                                +
                                (pow((y36 - y37), 2))
                        )
                    )
                    distance_42 = math.sqrt(
                        (
                                (pow((x37 - x33), 2))
                                +
                                (pow((y37 - y33), 2))
                        )
                    )

                    #Distancia ceja derecha
                    distance_43 = math.sqrt(
                        (
                                (pow((x33 - x38), 2))
                                +
                                (pow((y33 - y38), 2))
                        )
                    )
                    distance_44 = math.sqrt(
                        (
                                (pow((x38 - x39), 2))
                                +
                                (pow((y38 - y39), 2))
                        )
                    )
                    distance_45 = math.sqrt(
                        (
                                (pow((x39 - x40), 2))
                                +
                                (pow((y39 - y40), 2))
                        )
                    )
                    distance_46 = math.sqrt(
                        (
                                (pow((x38 - x40), 2))
                                +
                                (pow((y38 - y40), 2))
                        )
                    )

                    #Distancia total
                    distance_47 = math.sqrt(
                        (
                                (pow((x27 - x41), 2))
                                +
                                (pow((y27 - y41), 2))
                        )
                    ) + math.sqrt(
                        (
                                (pow((x41 - x29), 2))
                                +
                                (pow((y41 - y29), 2))
                        )
                    ) + math.sqrt(
                        (
                                (pow((x29 - x42), 2))
                                +
                                (pow((y29 - y42), 2))
                        )
                    ) + math.sqrt(
                        (
                                (pow((x42 - x23), 2))
                                +
                                (pow((y42 - y23), 2))
                        )
                    ) + math.sqrt(
                        (
                                (pow((x23 - x31), 2))
                                +
                                (pow((y23 - y31), 2))
                        )
                    ) + math.sqrt(
                        (
                                (pow((x31 - x43), 2))
                                +
                                (pow((y31 - y43), 2))
                        )
                    ) + math.sqrt(
                        (
                                (pow((x43 - x24), 2))
                                +
                                (pow((y43 - y24), 2))
                        )
                    ) + math.sqrt(
                        (
                                (pow((x24 - x34), 2))
                                +
                                (pow((y24 - y34), 2))
                        )
                    ) + math.sqrt(
                        (
                                (pow((x34 - x25), 2))
                                +
                                (pow((y34 - y25), 2))
                        )
                    ) + math.sqrt(
                        (
                                (pow((x25 - x44), 2))
                                +
                                (pow((y25 - y44), 2))
                        )
                    ) + math.sqrt(
                        (
                                (pow((x44 - x32), 2))
                                +
                                (pow((y44 - y32), 2))
                        )
                    ) + math.sqrt(
                        (
                                (pow((x32 - x26), 2))
                                +
                                (pow((y32 - y26), 2))
                        )
                    ) + math.sqrt(
                        (
                                (pow((x26 - x45), 2))
                                +
                                (pow((y26 - y45), 2))
                        )
                    ) + math.sqrt(
                        (
                                (pow((x45 - x30), 2))
                                +
                                (pow((y45 - y30), 2))
                        )
                    ) + math.sqrt(
                        (
                                (pow((x30 - x46), 2))
                                +
                                (pow((y30 - y46), 2))
                        )
                    ) + math.sqrt(
                        (
                                (pow((x46 - x28), 2))
                                +
                                (pow((y46 - y28), 2))
                        )
                    ) + math.sqrt(
                        (
                                (pow((x28 - x40), 2))
                                +
                                (pow((y28 - y40), 2))
                        )
                    ) + math.sqrt(
                        (
                                (pow((x40 - x50), 2))
                                +
                                (pow((y40 - y50), 2))
                        )
                    ) + math.sqrt(
                        (
                                (pow((x50 - x39), 2))
                                +
                                (pow((y50 - y39), 2))
                        )
                    ) + math.sqrt(
                        (
                                (pow((x39 - x49), 2))
                                +
                                (pow((y39 - y49), 2))
                        )
                    ) + math.sqrt(
                        (
                                (pow((x49 - x38), 2))
                                +
                                (pow((y49 - y38), 2))
                        )
                    ) + math.sqrt(
                        (
                                (pow((x38 - x37), 2))
                                +
                                (pow((y38 - y37), 2))
                        )
                    ) + math.sqrt(
                        (
                                (pow((x37 - x48), 2))
                                +
                                (pow((y37 - y48), 2))
                        )
                    ) + math.sqrt(
                        (
                                (pow((x48 - x36), 2))
                                +
                                (pow((y48 - y36), 2))
                        )
                    ) + math.sqrt(
                        (
                                (pow((x36 - x47), 2))
                                +
                                (pow((y36 - y47), 2))
                        )
                    ) + math.sqrt(
                        (
                                (pow((x47 - x35), 2))
                                +
                                (pow((y47 - y35), 2))
                        )
                    ) + math.sqrt(
                        (
                                (pow((x35 - x27), 2))
                                +
                                (pow((y35 - y27), 2))
                        )
                    )

                    test_points.append([distance_1,distance_2,distance_3,distance_4,distance_5,distance_6,distance_7,distance_8,distance_9,distance_10,distance_11,distance_12,distance_13,distance_14,distance_15,distance_16,distance_17,distance_18,distance_19,distance_20,distance_21,distance_22,distance_23,distance_24,distance_25,distance_26,distance_27,distance_28,distance_29,distance_30,distance_31,distance_32,distance_33,distance_34,distance_35,distance_36,distance_37,distance_38,distance_39,distance_40,distance_41,distance_42,distance_43,distance_44,distance_45,distance_46,distance_47])
                    test_points=np.asarray(test_points)
                    prediction=model.predict(test_points)

                    index_prediction=np.argmax(prediction)
                    #print(prediction)
                    if prediction[0][index_prediction]>0.99:
                        for name in e_lab:
                            if dict_user[str(index_prediction)] == name:
                                count+=1
                        print(dict_user[str(index_prediction)])
                        cv2.putText(frame, dict_user[str(index_prediction)], (bX - 10, bY - 10),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                        faces.append(dict_user[str(index_prediction)])
                        count_faces=count_faces+1
        else:
            cv2.putText(frame, "More than 1 face... ", (0 - 10, 0 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
        cv2.imshow("Frame", frame)
        count_photos=count_photos+1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if count == 50:
            while True:
                if(net_is_up() == 0):
                    mydb = mysql.connector.connect(host="10.0.5.246", user="LMV_ADMIN", passwd="LABORATORIOT4", database="LMV")
                    mycursor = mydb.cursor()
                    #Select to known if the laboratory door is open
                    sql = "SELECT estado FROM e_extraccion WHERE dispositivo='puerta'"
                    mycursor.execute(sql)
                    records = mycursor.fetchall()
                    print(mycursor.rowcount, "record selected")
                    for row in records:
                        estadolab = int(row[0])
                    if estadolab == 0:
                        os.system('gpio -g mode 22 out')
                        sql2 = "UPDATE r_muestras SET estado = 1 WHERE dispositivo='puerta'"
                        mycursor.execute(sql2)
                        mydb.commit()
                        print(mycursor.rowcount, "record affected")
                        time.sleep(1)
                        #END of mysql
                    elif estadolab == 1:
                        print("<p>close the laboratory door</p>")
                    break
            break
    cv2.destroyAllWindows()
    vs.stop()
    faces=np.asarray(faces)
    user_MAX=[]
    for user in dict_user:
        count_user=0
        for face in faces:
            if face==dict_user[user]:
                count_user=count_user+1
        user_MAX.append(count_user)
    user_MAX_index=np.argmax(user_MAX)
    response=""
    if user_MAX[user_MAX_index]<17:
        response=" "
    else:
        response=dict_user[str(user_MAX_index)]
    return response

while True:
    if(net_is_up() == 0):
        mydb = mysql.connector.connect(host="10.0.5.246", user="LMV_ADMIN", passwd="LABORATORIOT4", database="LMV")
        mycursor = mydb.cursor()
        #Select to known if the principal door is open
        sqlm = "SELECT estado FROM r_muestras WHERE dispositivo='puerta'"
        mycursor.execute(sqlm)
        recordsm = mycursor.fetchall()
        print(mycursor.rowcount, "record selected")
        for rowm in recordsm:
            estadopri = int(rowm[0])
        if estadopri == 1:
            print("<p>The principal door is open</p>")
        else:
            break

print(camera_recognition())
