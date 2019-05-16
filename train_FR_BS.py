import numpy as np
import dlib
import cv2
from imutils import face_utils
import imutils
import os
import glob
import tflearn
import math
import json
##TRAINING-GETTING INPUTS FOR NEURALNETWORK
def train_model():
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("land_mark/shape_predictor_68_face_landmarks.dat")
    path_image_training="usuarios/"
    output_dir="trainning_usuarios/"
    dict_user={}
    index_label=0
    for image_dir in os.listdir(path_image_training):
        image_output_dir = os.path.join(output_dir, os.path.basename(os.path.basename(image_dir)))
        if not os.path.exists(image_output_dir):
            os.makedirs(image_output_dir)
        dict_user[index_label]=image_dir
        index_label=index_label+1

    image_paths = glob.glob(os.path.join(path_image_training, '**/*.jpg'))
    train_points=[]
    labels3=[]
    labels_toSave=[]
    for index_dic_users, users_name in enumerate(dict_user):
        labels_row=[]
        for value in range(0,len(dict_user)):
            if value==index_dic_users:
                labels_row.append(1)
            else:
                labels_row.append(0)
        labels_toSave.append(labels_row)
    labels_toSave=np.asarray(labels_toSave)

    for index, image_path in enumerate(image_paths):
        image_output_dir = os.path.join(output_dir, os.path.basename(os.path.dirname(image_path)))
        output_path = os.path.join(image_output_dir, os.path.basename(image_path))
        #path = os.path.join(output_path, output_path)
        img = cv2.imread(image_path)
        img = imutils.resize(img, width=400)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        rects = detector(gray, 0)
        if len(rects) ==1:

            for rect in rects:

                (bX, bY, bW, bH) = face_utils.rect_to_bb(rect)
                #print(bW)
                if ((bW) == 149):
                    shape = predictor(gray, rect)
                    shape = face_utils.shape_to_np(shape)

                    # loop over the (x, y)-coordinates for the facial landmarks
                    # and draw each of them
                    
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

                    #DISTANCIA CARA
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

                    #DISTANCIA CEJA IZQUIERDA
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

                    #DISTANCIA CEJA DERECHA
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

                    train_points.append([distance_1,distance_2,distance_3,distance_4,distance_5,distance_6,distance_7,distance_8,distance_9,distance_10,distance_11,distance_12,distance_13,distance_14,distance_15,distance_16,distance_17,distance_18,distance_19,distance_20,distance_21,distance_22,distance_23,distance_24,distance_25,distance_26,distance_27,distance_28,distance_29,distance_30,distance_31,distance_32,distance_33,distance_34,distance_35,distance_36,distance_37,distance_38,distance_39,distance_40,distance_41,distance_42,distance_43,distance_44,distance_45,distance_46])
                    name=str(image_path)
                    name=name.split("/")
                    #print name[0]

                    for index_dic_tr_users in range(0,len(dict_user)):
                        if dict_user[index_dic_tr_users]==name[1] :
                            labels3.append(labels_toSave[index_dic_tr_users])
                            break

                    print(image_path," \t imagen entrenada")



    train_points=np.asarray(train_points)
    labels3=np.asarray(labels3)
    
    print(len(train_points))
    print(len(labels3))

    net = tflearn.input_data(shape=[None, 46])
    net = tflearn.fully_connected(net, 32)
    net = tflearn.fully_connected(net, 120)
    net = tflearn.fully_connected(net, 180)
    net = tflearn.fully_connected(net, 10, activation='softmax')
    net = tflearn.regression(net)
    # Define model
    model = tflearn.DNN(net)
    # Start training (apply gradient descent algorithm)
    model.fit(train_points, labels3, n_epoch=10000, show_metric=True)

    with open('bd_FR/data.json', 'w') as fp:
        json.dump(dict_user, fp)
    model.save("model_FR_BS.tflearn")
    return "[INFO] MODEL SAVED"
train_model()
