# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editor.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import os
from PIL import Image, ImageFilter, ImageDraw
workdir = ''
filename = ''
class Ui_MainWindow(object):
    def inverse(self):
        global workdir, filename
        with Image.open(f"{workdir}/{filename}") as img:
            draw = ImageDraw.Draw(img)
            width = img.size[0]
            height = img.size[1]
            pix = img.load()
            for x in range(width):
                for y in range(height):
                    r = pix[x,y][0]
                    g = pix[x,y][1]
                    b = pix[x,y][2]
                    draw.point((x,y), (255-r, 255-g, 255-b))
            img.save("newImage/inverse.png")
            self.label.setPixmap(QtGui.QPixmap("newImage/inverse.png"))
    def blackwhite(self):
        global workdir, filename
        with Image.open(f"{workdir}/{filename}") as img:
            t = img.convert("L")
            t.save("newImage/blackwhite.png")
            self.label.setPixmap(QtGui.QPixmap("newImage/blackwhite.png"))
    def blurred(self):
        global workdir, filename
        with Image.open(f"{workdir}/{filename}") as img:
            r = img.filter(ImageFilter.BLUR)
            r.save("newImage/blur.png")
            self.label.setPixmap(QtGui.QPixmap("newImage/blur.png"))
    def leftside(self):
        global workdir, filename
        with Image.open(f"{workdir}/{filename}") as img:
            q = img.transpose(Image.ROTATE_90)
            q.save("newImage/r90.png")
            self.label.setPixmap(QtGui.QPixmap("newImage/r90.png"))
    def rightside(self):
        global workdir, filename
        with Image.open(f"{workdir}/{filename}") as img:
            w = img.transpose(Image.ROTATE_270)
            w.save("newImage/r270.png")
            self.label.setPixmap(QtGui.QPixmap("newImage/r270.png"))
    def mirrored(self):
        global workdir, filename
        with Image.open(f"{workdir}/{filename}") as img:
            e = img.transpose(Image.ROTATE_180)
            e.save("newImage/r180.png")
            self.label.setPixmap(QtGui.QPixmap("newImage/r180.png"))
    def open_image(self):
        global workdir, filename
        filename = self.listWidget.selectedItems()[0].text()
        self.label.setPixmap(QtGui.QPixmap(f"{workdir}/{filename}"))
    def papka(self):
        global workdir, filename
        workdir = QFileDialog.getExistingDirectory()
        with os.scandir(workdir) as dir:
            for i in dir:
                self.listWidget.addItem(i.name)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1123, 693)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 60, 261, 571))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.clicked.connect(self.open_image)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 20, 261, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.papka)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 600, 131, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.leftside)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(420, 600, 131, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.rightside)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(560, 600, 131, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.mirrored)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(700, 600, 131, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.blurred)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(840, 600, 131, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.blackwhite)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(980, 600, 131, 28))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.inverse)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 70, 801, 521))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("original/photo_2022-12-11_16-41-11.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 10, 421, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1123, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Папка"))
        self.pushButton_2.setText(_translate("MainWindow", "Вліво"))
        self.pushButton_3.setText(_translate("MainWindow", "Вправо"))
        self.pushButton_4.setText(_translate("MainWindow", "Дзеркало"))
        self.pushButton_5.setText(_translate("MainWindow", "Різкість"))
        self.pushButton_6.setText(_translate("MainWindow", "Ч/Б"))
        self.pushButton_7.setText(_translate("MainWindow", "Інверсія"))
        self.label_2.setText(_translate("MainWindow", "Easy Editor"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
