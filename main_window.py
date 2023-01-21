# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(800, 551))
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.menu_layout = QHBoxLayout()
        self.menu_layout.setObjectName(u"menu_layout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.menu_layout.addWidget(self.label_2)


        self.verticalLayout.addLayout(self.menu_layout)

        self.main_layout = QHBoxLayout()
        self.main_layout.setObjectName(u"main_layout")
        self.languages_menu = QWidget(self.centralwidget)
        self.languages_menu.setObjectName(u"languages_menu")
        self.languages_menu.setMaximumSize(QSize(100, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.languages_menu)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.english_button = QPushButton(self.languages_menu)
        self.english_button.setObjectName(u"english_button")
        self.english_button.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_2.addWidget(self.english_button)

        self.french_button = QPushButton(self.languages_menu)
        self.french_button.setObjectName(u"french_button")
        self.french_button.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_2.addWidget(self.french_button)

        self.russian_button = QPushButton(self.languages_menu)
        self.russian_button.setObjectName(u"russian_button")
        self.russian_button.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_2.addWidget(self.russian_button)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.main_layout.addWidget(self.languages_menu)

        self.main_window = QWidget(self.centralwidget)
        self.main_window.setObjectName(u"main_window")
        self.label = QLabel(self.main_window)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(320, 70, 151, 16))
        self.label.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.main_layout.addWidget(self.main_window)


        self.verticalLayout.addLayout(self.main_layout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Menu window", None))
        self.english_button.setText(QCoreApplication.translate("MainWindow", u"English", None))
        self.french_button.setText(QCoreApplication.translate("MainWindow", u"French", None))
        self.russian_button.setText(QCoreApplication.translate("MainWindow", u"Russian", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Main window", None))
    # retranslateUi

