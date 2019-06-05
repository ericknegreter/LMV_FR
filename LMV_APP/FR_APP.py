# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FR_APP.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import os
import subprocess
from gtts import gTTS
import paramiko
import sys
import mysql.connector

class Ui_Form(object):
    def showmessage(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Question)
        msgBox.setWindowTitle(title)
        msgBox.setGeometry(1000, 500, 1400, 600)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        resp = msgBox.exec_()
        if resp == QtWidgets.QMessageBox.Yes:
            return 1
        else:
            return 0

    def runFR(self):
        texto = self.text_name.toPlainText()
        result = subprocess.check_output([sys.executable, '/home/erickpc/LMV_FR/recognition_face_BS.py'])
        resul = result.decode()
        result = resul.rstrip()
        print(result)
        name_corr = texto.split()
        name_corr = "_".join(name_corr)
        print(name_corr)
        if result  == name_corr:
            mytext = ('Bienvenido ' + texto)
            language = 'es'
            myobj = gTTS(text=mytext, lang=language, slow=False)
            myobj.save("welcome.mp3")
            os.system("mpg321 welcome.mp3")
            #proxy = None
            #client = paramiko.SSHClient()
            #client.load_system_host_keys()
            #client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            #client.connect(hostname='10.0.5.122', username='pi', password='t4oligo', proxy=proxy)
            #ssh_stdin, ssh_stdout, ssh_stderr = client.exec_command('python3 /home/pi/Documents/entrada_lab/open_door1.py')
            sys.exit(app.exec_())
        else:
            m = self.showmessage('Invalid user', 'Would you like try again?')
            if m == 0:
                sys.exit(app.exec_())

    
    def showText(self):
         print(self.text_name.toPlainText() + 'todo bien')

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1362, 836)
        #Form.resize(2000,1000)
        self.label_picu = QtWidgets.QLabel(Form)
        self.label_picu.setGeometry(QtCore.QRect(386, 9, 501, 441))
        self.label_picu.setObjectName("label_picu")
        self.text_name = QtWidgets.QTextEdit(Form)
        self.text_name.setGeometry(QtCore.QRect(386, 548, 501, 51))
        self.text_name.setObjectName("text_name")
        self.label_name = QtWidgets.QLabel(Form)
        self.label_name.setGeometry(QtCore.QRect(387, 523, 501, 21))
        self.label_name.setTextFormat(QtCore.Qt.AutoText)
        self.label_name.setObjectName("label_name")
        ########################pushButton_cancel#####################
        self.pushButton_cancel = QtWidgets.QPushButton(Form)
        self.pushButton_cancel.setGeometry(QtCore.QRect(640, 610, 251, 25))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.pushButton_cancel.clicked.connect(QtCore.QCoreApplication.instance().quit)
        ##############################################################
        #
        ########################pushButton_continue###################
        self.pushButton_continue = QtWidgets.QPushButton(Form)
        self.pushButton_continue.setGeometry(QtCore.QRect(386, 610, 241, 25))
        self.pushButton_continue.setObjectName("pushButton_continue")
        self.pushButton_continue.clicked.connect(self.runFR)
        #############################################################
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_picu.setText(_translate("Form", "<html><head/><body><p><img src=blackstar.png></p></body></html>"))
        self.label_name.setText(_translate("Form", "Ingresa tu nombre"))
        self.pushButton_cancel.setText(_translate("Form", "Cancelar"))
        self.pushButton_continue.setText(_translate("Form", "Continuar"))


#import t4oligo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
