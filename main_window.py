# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setKerning(True)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QPushButton:checked {\n"
"	background-color: rgb(28, 28, 28);\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.menu_layout = QHBoxLayout()
        self.menu_layout.setObjectName(u"menu_layout")
        self.menu_layout.setSizeConstraint(QLayout.SetNoConstraint)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setStyleSheet(u"")

        self.menu_layout.addWidget(self.label_2)


        self.verticalLayout.addLayout(self.menu_layout)

        self.main_layout = QHBoxLayout()
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setSizeConstraint(QLayout.SetNoConstraint)
        self.languages_menu = QWidget(self.centralwidget)
        self.languages_menu.setObjectName(u"languages_menu")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.languages_menu.sizePolicy().hasHeightForWidth())
        self.languages_menu.setSizePolicy(sizePolicy2)
        self.languages_menu.setMaximumSize(QSize(100, 16777215))
        self.languages_menu.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.languages_menu)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.english_button = QPushButton(self.languages_menu)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.english_button)
        self.english_button.setObjectName(u"english_button")
        self.english_button.setStyleSheet(u"")
        self.english_button.setCheckable(True)
        self.english_button.setChecked(True)
        self.english_button.setAutoExclusive(True)
        self.english_button.setFlat(False)

        self.verticalLayout_2.addWidget(self.english_button)

        self.french_button = QPushButton(self.languages_menu)
        self.buttonGroup.addButton(self.french_button)
        self.french_button.setObjectName(u"french_button")
        self.french_button.setStyleSheet(u"")
        self.french_button.setCheckable(True)
        self.french_button.setAutoExclusive(True)
        self.french_button.setFlat(False)

        self.verticalLayout_2.addWidget(self.french_button)

        self.russian_button = QPushButton(self.languages_menu)
        self.buttonGroup.addButton(self.russian_button)
        self.russian_button.setObjectName(u"russian_button")
        self.russian_button.setStyleSheet(u"")
        self.russian_button.setCheckable(True)
        self.russian_button.setAutoExclusive(True)
        self.russian_button.setFlat(False)

        self.verticalLayout_2.addWidget(self.russian_button)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.main_layout.addWidget(self.languages_menu)


        self.verticalLayout.addLayout(self.main_layout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Menu window", None))
        self.english_button.setText(QCoreApplication.translate("MainWindow", u"English", None))
        self.french_button.setText(QCoreApplication.translate("MainWindow", u"French", None))
        self.russian_button.setText(QCoreApplication.translate("MainWindow", u"Russian", None))
    # retranslateUi

