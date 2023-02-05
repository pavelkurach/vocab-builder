# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QSizePolicy,
                               QStatusBar, QWidget, QStackedWidget, QRadioButton)

from main_window import Ui_MainWindow
from add_word_dialog import Ui_add_word_dialog
from dict_scrapers import *


class AddWordDialog(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_add_word_dialog()
        self.ui.setupUi(self)
        self.ui.def_options = []
        self.ui.search_def_btn.clicked.connect(self.search_defs_btn_clicked)

    def search_defs_btn_clicked(self):
        word = self.ui.word.text()
        defs = scrape_oxford_learners_dictionary(word=word)
        for option in self.ui.def_options:
            option.setParent(None)
            del option
        self.ui.def_options = [QRadioButton(text=text) for text in defs]
        for option in self.ui.def_options:
            option.setStyleSheet('color: black')
            self.ui.defs_layout.addWidget(option)


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.stacked_widget = QStackedWidget()
        self.ui.add_word_dialog = AddWordDialog()
        self.ui.stacked_widget.addWidget(self.ui.add_word_dialog)
        self.ui.main_layout.addWidget(self.ui.stacked_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
