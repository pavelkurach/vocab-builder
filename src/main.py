import sys
import logging

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QSizePolicy,
    QWidget,
    QRadioButton,
    QTabWidget,
)

from main_window import Ui_MainWindow
from add_word_dialog import Ui_add_word_dialog
from recall_word_dialog import Ui_recall_word_dialog

from dict_scrapers import scrape_oxford_learners_dictionary
from spaced_repetition import SpacedRepetition, Word

from functools import partial

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)
logger = logging.getLogger(__name__)


class AddWordDialog(QWidget):
    def __init__(self, db: SpacedRepetition, parent=None):
        super().__init__(parent)
        self.ui = Ui_add_word_dialog()
        self.ui.setupUi(self)
        self.db = db
        self.ui.def_options = []
        self.ui.search_def_btn.clicked.connect(self._search_defs_btn_clicked)
        self.ui.add_word_button.setEnabled(False)
        self.ui.custom_def_btn.click()
        self.current_def = ''
        self.ui.custom_def.textChanged.connect(self._custom_def_changed)
        self.ui.clear_button.clicked.connect(self._clear)
        self.ui.add_word_button.clicked.connect(self._add_button_clicked)

    def _set_current_def(self, definition: str):
        self.current_def = definition
        logger.info(f'Current definition: {self.current_def}')
        self.ui.add_word_button.setEnabled(True)

    def _custom_def_changed(self):
        if not self.ui.custom_def_btn.isChecked():
            self.ui.custom_def_btn.click()
        self._set_current_def(self.ui.custom_def.toPlainText())

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
            text = option.text()
            option.clicked.connect(partial(self._set_current_def, text))

    def _clear(self):
        self.ui.word.setText('')
        self.ui.custom_def.setText('')
        self.ui.add_word_button.setEnabled(False)
        for option in self.ui.def_options:
            option.deleteLater()

    def _add_button_clicked(self):
        word = self.ui.word.text()
        if word and len(word) > 0:
            self.db.add_word(word=word, definition=self.current_def)
        self._clear()


class RecallWordDialog(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_recall_word_dialog()
        self.ui.setupUi(self)
        self.words_to_revise = iter(())
        self.revise_coroutine = iter(())
        self.current_db = None
        self.current_word = Word('', '')
        self.ui.forgot_btn.clicked.connect(self._state_button_clicked)
        self.ui.ok_btn.clicked.connect(self._state_button_clicked)
        self.ui.recalled_btn.clicked.connect(self._state_button_clicked)
        self.ui.show_def_btn.clicked.connect(self._show_def_button_clicked)

    def _set_current_word(self, word: Word):
        logger.info(f'Current word: {word.word}')
        self.current_word = word
        self.ui.word.setText(word.word)
        self.ui.definition.setText('')

    def _show_def_button_clicked(self):
        self.ui.definition.setText(self.current_word.definition)

    def start_to_revise(self, db: SpacedRepetition):
        self.current_db = db
        self.words_to_revise = iter(db.get_words_to_revise())
        try:
            self._set_current_word(next(self.words_to_revise))
        except StopIteration:
            return
        self._set_buttons_enabled(True)

    def _set_buttons_enabled(self, enabled: bool):
        self.ui.show_def_btn.setEnabled(enabled)
        self.ui.forgot_btn.setEnabled(enabled)
        self.ui.ok_btn.setEnabled(enabled)
        self.ui.recalled_btn.setEnabled(enabled)

    def _state_button_clicked(self):
        assert self.current_word is not None
        button = self.sender()
        state = button.text()
        if state not in SpacedRepetition.states:
            raise ValueError('Incorrect status. Supported states: '
                             + ' '.join(SpacedRepetition.states))
        self.current_db.revise(word=self.current_word, state=state)
        logger.info(f'Current word: {self.current_word}, '
                    f'state: {state}, '
                    f'next revision: {self.current_word.next_rep}.')
        try:
            self._set_current_word(next(self.words_to_revise))
        except StopIteration:
            self._set_buttons_enabled(False)
            self.ui.word.setText('No words to revise')
            self.ui.definition.setText('')


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.en_db = SpacedRepetition("EN")
        self.ui.tab_widget = QTabWidget()
        self.ui.tab_widget.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding
        )
        self.ui.add_word_dialog = AddWordDialog(db=self.en_db)
        self.ui.recall_word_dialog = RecallWordDialog()
        self.ui.tab_widget.addTab(self.ui.add_word_dialog, "Add new words")
        self.ui.tab_widget.addTab(self.ui.recall_word_dialog, "Revise")
        self.ui.main_layout.addWidget(self.ui.tab_widget)
        self.ui.tab_widget.currentChanged.connect(self._revise)

        # to be added
        self.ui.french_button.setEnabled(False)
        self.ui.russian_button.setEnabled(False)

    def _revise(self):
        if self.ui.tab_widget.currentWidget() is self.ui.recall_word_dialog:
            self.ui.recall_word_dialog.start_to_revise(self.en_db)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
