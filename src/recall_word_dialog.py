# -*- coding: utf-8 -*-

###############################################################################
# Form generated from reading UI file 'recall_word_dialog.ui'
#
# Created by: Qt User Interface Compiler version 6.4.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
###############################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
)

from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
)


class Ui_recall_word_dialog(object):
    def setupUi(self, recall_word_dialog):
        if not recall_word_dialog.objectName():
            recall_word_dialog.setObjectName("recall_word_dialog")
        recall_word_dialog.resize(704, 522)
        self.verticalLayout = QVBoxLayout(recall_word_dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.word = QLabel(recall_word_dialog)
        self.word.setObjectName("word")

        self.horizontalLayout.addWidget(self.word)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.show_def_btn = QPushButton(recall_word_dialog)
        self.show_def_btn.setObjectName("show_def_btn")
        self.show_def_btn.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.show_def_btn)

        self.horizontalSpacer_4 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.definition = QLabel(recall_word_dialog)
        self.definition.setObjectName("definition")

        self.horizontalLayout_3.addWidget(self.definition)

        self.horizontalSpacer_6 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.forgot_btn = QPushButton(recall_word_dialog)
        self.forgot_btn.setObjectName("forgot_btn")
        self.forgot_btn.setEnabled(False)

        self.horizontalLayout_4.addWidget(self.forgot_btn)

        self.ok_btn = QPushButton(recall_word_dialog)
        self.ok_btn.setObjectName("ok_btn")
        self.ok_btn.setEnabled(False)

        self.horizontalLayout_4.addWidget(self.ok_btn)

        self.recalled_btn = QPushButton(recall_word_dialog)
        self.recalled_btn.setObjectName("recalled_btn")
        self.recalled_btn.setEnabled(False)

        self.horizontalLayout_4.addWidget(self.recalled_btn)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(recall_word_dialog)

        QMetaObject.connectSlotsByName(recall_word_dialog)

    # setupUi

    def retranslateUi(self, recall_word_dialog):
        recall_word_dialog.setWindowTitle(
            QCoreApplication.translate("recall_word_dialog", "Form", None)
        )
        self.word.setText(
            QCoreApplication.translate(
                "recall_word_dialog", "No words to revise.", None
            )
        )
        self.show_def_btn.setText(
            QCoreApplication.translate(
                "recall_word_dialog", "Show definition", None
            )
        )
        self.definition.setText("")
        self.forgot_btn.setText(
            QCoreApplication.translate("recall_word_dialog", "Forgot", None)
        )
        self.ok_btn.setText(
            QCoreApplication.translate("recall_word_dialog", "OK", None)
        )
        self.recalled_btn.setText(
            QCoreApplication.translate(
                "recall_word_dialog", "Recalled easily", None
            )
        )

    # retranslateUi
