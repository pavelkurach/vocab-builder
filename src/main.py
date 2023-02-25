import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QSizePolicy,
    QWidget,
    QRadioButton,
    QTabWidget,
    QLabel,
)

from main_window import Ui_MainWindow
from add_word_dialog import Ui_add_word_dialog
from recall_word_dialog import Ui_recall_word_dialog

from dict_scrapers import scrape_oxford_learners_dictionary


class AddWordDialog(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_add_word_dialog()
        self.ui.setupUi(self)
        self.ui.def_options = []
        self.ui.search_def_btn.clicked.connect(self._search_defs_btn_clicked)

    def _search_defs_btn_clicked(self):
        word = self.ui.word.text()
        defs = scrape_oxford_learners_dictionary(word=word.lower())
        for option in self.ui.def_options:
            option.deleteLater()
        self.ui.def_options = [
            QRadioButton(text=text.replace(". ", ".\n")) for text in defs
        ]
        for option in self.ui.def_options:
            self.ui.defs_layout.addWidget(option)


class RecallWordDialog(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_recall_word_dialog()
        self.ui.setupUi(self)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tab_widget = QTabWidget()
        self.ui.tab_widget.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding
        )
        self.ui.add_word_dialog = AddWordDialog()
        self.ui.recall_word_dialog = RecallWordDialog()
        self.ui.tab_widget.addTab(self.ui.add_word_dialog, "Add new words")
        self.ui.tab_widget.addTab(self.ui.recall_word_dialog, "Revise")
        self.ui.main_layout.addWidget(self.ui.tab_widget)
        #self.ui.tab_widget.currentChanged.connect()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
