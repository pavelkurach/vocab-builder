# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_word_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_add_word_dialog(object):
    def setupUi(self, add_word_dialog):
        if not add_word_dialog.objectName():
            add_word_dialog.setObjectName(u"add_word_dialog")
        add_word_dialog.resize(792, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(add_word_dialog.sizePolicy().hasHeightForWidth())
        add_word_dialog.setSizePolicy(sizePolicy)
        add_word_dialog.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"\n"
"\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(add_word_dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(add_word_dialog)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetNoConstraint)
        self.word = QLineEdit(add_word_dialog)
        self.word.setObjectName(u"word")
        self.word.setStyleSheet(u"background-color: rgb(40, 40, 40);")

        self.horizontalLayout_2.addWidget(self.word)

        self.search_def_btn = QPushButton(add_word_dialog)
        self.search_def_btn.setObjectName(u"search_def_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.search_def_btn.sizePolicy().hasHeightForWidth())
        self.search_def_btn.setSizePolicy(sizePolicy2)
        self.search_def_btn.setMinimumSize(QSize(150, 0))
        self.search_def_btn.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.search_def_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label_2 = QLabel(add_word_dialog)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.label_2)

        self.widget = QWidget(add_word_dialog)
        self.widget.setObjectName(u"widget")
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.defs_layout = QVBoxLayout()
        self.defs_layout.setObjectName(u"defs_layout")
        self.defs_layout.setSizeConstraint(QLayout.SetNoConstraint)
        self.custom_def_btn = QRadioButton(self.widget)
        self.custom_def_btn.setObjectName(u"custom_def_btn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.custom_def_btn.sizePolicy().hasHeightForWidth())
        self.custom_def_btn.setSizePolicy(sizePolicy3)
        self.custom_def_btn.setStyleSheet(u"")

        self.defs_layout.addWidget(self.custom_def_btn)

        self.textEdit = QTextEdit(self.widget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"background-color: rgb(40, 40, 40);")

        self.defs_layout.addWidget(self.textEdit)


        self.verticalLayout_3.addLayout(self.defs_layout)


        self.verticalLayout.addWidget(self.widget)

        self.status_label = QLabel(add_word_dialog)
        self.status_label.setObjectName(u"status_label")
        sizePolicy1.setHeightForWidth(self.status_label.sizePolicy().hasHeightForWidth())
        self.status_label.setSizePolicy(sizePolicy1)
        self.status_label.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.status_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.add_word_button = QPushButton(add_word_dialog)
        self.add_word_button.setObjectName(u"add_word_button")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.add_word_button.sizePolicy().hasHeightForWidth())
        self.add_word_button.setSizePolicy(sizePolicy4)
        self.add_word_button.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.add_word_button)

        self.clear_button = QPushButton(add_word_dialog)
        self.clear_button.setObjectName(u"clear_button")
        self.clear_button.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.clear_button)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(add_word_dialog)

        QMetaObject.connectSlotsByName(add_word_dialog)
    # setupUi

    def retranslateUi(self, add_word_dialog):
        add_word_dialog.setWindowTitle(QCoreApplication.translate("add_word_dialog", u"Form", None))
        self.label.setText(QCoreApplication.translate("add_word_dialog", u"Word:", None))
        self.search_def_btn.setText(QCoreApplication.translate("add_word_dialog", u"Search definitions", None))
        self.label_2.setText(QCoreApplication.translate("add_word_dialog", u"Definition:", None))
        self.custom_def_btn.setText(QCoreApplication.translate("add_word_dialog", u"Custom definition ", None))
        self.status_label.setText("")
        self.add_word_button.setText(QCoreApplication.translate("add_word_dialog", u"Add ", None))
        self.clear_button.setText(QCoreApplication.translate("add_word_dialog", u"Clear", None))
    # retranslateUi

