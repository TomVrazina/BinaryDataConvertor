# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainCzHvzf.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(900, 600))
        MainWindow.setMaximumSize(QSize(900, 600))
        self.actionLoadKFG = QAction(MainWindow)
        self.actionLoadKFG.setObjectName(u"actionLoadKFG")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionAboutQt = QAction(MainWindow)
        self.actionAboutQt.setObjectName(u"actionAboutQt")
        self.actionLoad = QAction(MainWindow)
        self.actionLoad.setObjectName(u"actionLoad")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 350))
        self.frame.setStyleSheet(u"background-color: rgb(45, 45,45);")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 20, -1, 20)
        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(16)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_2.addWidget(self.label_11)

        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setPointSize(12)
        self.label_10.setFont(font1)
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_2.addWidget(self.label_10)


        self.verticalLayout.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setMaximumSize(QSize(16777215, 400))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_3)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setVerticalSpacing(25)
        self.formLayout.setContentsMargins(20, 10, 0, 20)
        self.label_12 = QLabel(self.frame_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)
        self.label_12.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_12)

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_3)

        self.LoadEditKFG = QLineEdit(self.frame_3)
        self.LoadEditKFG.setObjectName(u"LoadEditKFG")
        self.LoadEditKFG.setMinimumSize(QSize(600, 30))
        self.LoadEditKFG.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(32, 36, 42);\n"
"	border-radius: 5px;\n"
"	color: rgb(255, 170, 0);\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.LoadEditKFG)

        self.btn_load_KFG = QPushButton(self.frame_3)
        self.btn_load_KFG.setObjectName(u"btn_load_KFG")
        self.btn_load_KFG.setMinimumSize(QSize(100, 30))
        self.btn_load_KFG.setMaximumSize(QSize(200, 30))
        self.btn_load_KFG.setSizeIncrement(QSize(0, 0))
        self.btn_load_KFG.setBaseSize(QSize(0, 0))
        font2 = QFont()
        font2.setFamily(u"Arial Black")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setWeight(75)
        font2.setStrikeOut(False)
        font2.setKerning(False)
        self.btn_load_KFG.setFont(font2)
        self.btn_load_KFG.setStyleSheet(u"QPushButton {\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius: 10px;\n"
"	border:10px rgb(177, 177, 177)\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(85, 170, 255);\n"
"	\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"	\n"
"	;\n"
"	background-color: rgb(175, 217, 255);\n"
"	\n"
"	border-radius: 10px;\n"
"}")
        self.btn_load_KFG.setFlat(False)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.btn_load_KFG)

        self.label_14 = QLabel(self.frame_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)
        self.label_14.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_14.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_14)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.label_2)

        self.LoadData = QLineEdit(self.frame_3)
        self.LoadData.setObjectName(u"LoadData")
        self.LoadData.setMinimumSize(QSize(600, 30))
        self.LoadData.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(32, 36, 42);\n"
"	border-radius: 5px;\n"
"	color: rgb(255, 170, 0);\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.LoadData)

        self.btn_Load_data = QPushButton(self.frame_3)
        self.btn_Load_data.setObjectName(u"btn_Load_data")
        self.btn_Load_data.setMinimumSize(QSize(100, 30))
        self.btn_Load_data.setMaximumSize(QSize(200, 30))
        self.btn_Load_data.setSizeIncrement(QSize(0, 0))
        self.btn_Load_data.setBaseSize(QSize(0, 0))
        self.btn_Load_data.setFont(font2)
        self.btn_Load_data.setStyleSheet(u"QPushButton {\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius: 10px;\n"
"	border:10px rgb(177, 177, 177)\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(85, 170, 255);\n"
"	\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"	\n"
"	;\n"
"	background-color: rgb(175, 217, 255);\n"
"	\n"
"	border-radius: 10px;\n"
"}")
        self.btn_Load_data.setFlat(False)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.btn_Load_data)

        self.label_13 = QLabel(self.frame_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)
        self.label_13.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_13)

        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.label)

        self.SaveData = QLineEdit(self.frame_3)
        self.SaveData.setObjectName(u"SaveData")
        self.SaveData.setMinimumSize(QSize(600, 30))
        self.SaveData.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(32, 36, 42);\n"
"	border-radius: 5px;\n"
"	color: rgb(255, 170, 0);\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.SaveData)

        self.btn_Save = QPushButton(self.frame_3)
        self.btn_Save.setObjectName(u"btn_Save")
        self.btn_Save.setMinimumSize(QSize(100, 30))
        self.btn_Save.setMaximumSize(QSize(200, 30))
        self.btn_Save.setSizeIncrement(QSize(0, 0))
        self.btn_Save.setBaseSize(QSize(0, 0))
        self.btn_Save.setFont(font2)
        self.btn_Save.setStyleSheet(u"QPushButton {\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius: 10px;\n"
"	border:10px rgb(177, 177, 177)\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(85, 170, 255);\n"
"	\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"	\n"
"	;\n"
"	background-color: rgb(175, 217, 255);\n"
"	\n"
"	border-radius: 10px;\n"
"}")
        self.btn_Save.setFlat(False)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.btn_Save)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 16777215))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(300, 16777215))
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(10, 10, 0, -1)
        self.label_15 = QLabel(self.frame_5)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)
        self.label_15.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_15.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_15, 0, 0, 1, 1)

        self.CycleTime = QLineEdit(self.frame_5)
        self.CycleTime.setObjectName(u"CycleTime")
        self.CycleTime.setMinimumSize(QSize(100, 30))
        self.CycleTime.setMaximumSize(QSize(100, 16777215))
        self.CycleTime.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(222, 222, 222);\n"
"	border-radius: 5px;\n"
"	color: rgb(0, 0, 0);\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"")

        self.gridLayout_2.addWidget(self.CycleTime, 0, 1, 1, 1)

        self.label_16 = QLabel(self.frame_5)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)
        self.label_16.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_16.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_16, 1, 0, 1, 1)

        self.Sel_Cycle = QLineEdit(self.frame_5)
        self.Sel_Cycle.setObjectName(u"Sel_Cycle")
        self.Sel_Cycle.setMinimumSize(QSize(100, 30))
        self.Sel_Cycle.setMaximumSize(QSize(100, 16777215))
        self.Sel_Cycle.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(222, 222, 222);\n"
"	border-radius: 5px;\n"
"	color: rgb(0, 0, 0);\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"")

        self.gridLayout_2.addWidget(self.Sel_Cycle, 1, 1, 1, 1)


        self.horizontalLayout.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(200, 0))
        self.frame_6.setMaximumSize(QSize(1677215, 16777215))
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_6)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(410, 30, 0, 0)
        self.Process_data_btn = QPushButton(self.frame_6)
        self.Process_data_btn.setObjectName(u"Process_data_btn")
        self.Process_data_btn.setMinimumSize(QSize(200, 50))
        self.Process_data_btn.setSizeIncrement(QSize(0, 0))
        self.Process_data_btn.setBaseSize(QSize(0, 0))
        self.Process_data_btn.setFont(font2)
        self.Process_data_btn.setStyleSheet(u"  QPushButton:enabled {\n"
"               \n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius: 10px;\n"
"	border:10px rgb(177, 177, 177)\n"
"}\n"
"   \n"
" QPushButton:disabled {\n"
"	background-color: #ccc; /* Gray for disabled */\n"
"	color: black;\n"
"}\n"
"\n"
"QPushButton {\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius: 10px;\n"
"	border:10px rgb(177, 177, 177)\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(85, 170, 255);\n"
"	\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"	\n"
"	;\n"
"	background-color: rgb(175, 217, 255);\n"
"	\n"
"	border-radius: 10px;\n"
"}")
        self.Process_data_btn.setFlat(False)

        self.verticalLayout_3.addWidget(self.Process_data_btn)


        self.horizontalLayout.addWidget(self.frame_6)


        self.verticalLayout.addWidget(self.frame_4, 0, Qt.AlignLeft)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 900, 22))
        self.menubar.setStyleSheet(u"QMenuBar {\n"
"background-color: rgb(25, 25, 35);\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"color : white;\n"
"margin-top:4px;\n"
"spacing: 3px;\n"
"padding: 1px 10px;\n"
"background: transparent;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QMenuBar::item:selected { /* when selected using mouse or keyboard */\n"
"background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"QMenuBar::item:pressed {\n"
"background-color: rgb(85, 170, 255);\n"
"}")
        self.menubar.setDefaultUp(False)
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuFile.setStyleSheet(u"QMenu {\n"
"background-color: rgb(25, 25, 35);\n"
"}\n"
"\n"
"QMenu::item {\n"
"color : white;\n"
"margin-top:4px;\n"
"spacing: 3px;\n"
"padding: 2px 20px;\n"
"background: transparent;\n"
"border-radius: 1px;\n"
"}\n"
"\n"
"QMenu::item:selected { /* when selected using mouse or keyboard */\n"
"background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"QMenu::item:pressed {\n"
"background-color: rgb(85, 170, 255);\n"
"}")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuAbout.setStyleSheet(u"QMenu {\n"
"background-color: rgb(25, 25, 35);\n"
"}\n"
"\n"
"QMenu::item {\n"
"color : white;\n"
"margin-top:4px;\n"
"spacing: 3px;\n"
"padding: 2px 20px;\n"
"background: transparent;\n"
"border-radius: 1px;\n"
"}\n"
"\n"
"QMenu::item:selected { /* when selected using mouse or keyboard */\n"
"background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"QMenu::item:pressed {\n"
"background-color: rgb(85, 170, 255);\n"
"}")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuFile.addAction(self.actionLoadKFG)
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionSave)
        self.menuAbout.addAction(self.actionAboutQt)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionLoadKFG.setText(QCoreApplication.translate("MainWindow", u"Load KFG", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionAboutQt.setText(QCoreApplication.translate("MainWindow", u"AboutQt", None))
        self.actionLoad.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"DATA CONVERTOR", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Program for conversion of binary data to int and floats", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"KFG File directory", None))
        self.label_3.setText("")
        self.btn_load_KFG.setText(QCoreApplication.translate("MainWindow", u"Load KFG", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Data Folder directory", None))
        self.label_2.setText("")
        self.btn_Load_data.setText(QCoreApplication.translate("MainWindow", u"Load Data", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Save directory", None))
        self.label.setText("")
        self.btn_Save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Time of Cycle", None))
        self.CycleTime.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Selected Cycle", None))
        self.Process_data_btn.setText(QCoreApplication.translate("MainWindow", u"Process Data", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

