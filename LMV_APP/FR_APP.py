# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FR_APP.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os
import subprocess

e_lab = 'Erick_Negrete'

class Ui_Form(object):
    def runFR(self):
        mytext = self.text_name.toPlainText()
        result = subprocess.check_output([sys.executable, '/home/erickpc/LMV_FR/recognition_face_BS.py'])
        resul = result.decode()
        result = resul.rstrip()
        if result  == e_lab:
            print('si salio')
    
    def showText(self):
         print(self.text_name.toPlainText() + 'todo bien')

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1362, 836)
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
        self.label_picu.setText(_translate("Form", "<html><head/><body><p><img src=T4oligo.jpeg></p></body></html>"))
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
