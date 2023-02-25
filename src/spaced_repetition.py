import logging
import os
from types import MappingProxyType
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, MetaData, Column, String, Integer, Date
from sqlalchemy.orm import declarative_base
from datetime import date, timedelta

from src.dict_scrapers import SUPPORTED_LANGUAGES

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)
logger = logging.getLogger(__name__)

Base = declarative_base()


class SpacedRepetition:
    buckets = MappingProxyType(
        {
            0: 0,
            1: 1,
            2: 3,
            3: 7,
            4: 14,
            5: 30,
        }
    )

    states = ("Forgot", "OK", "Recalled easily")

    @staticmethod
    def spaced_repetition_scheduler(bucket: int, state: str) -> int:
        """
        Get new bucket number and repetition interval
        :param bucket: current bucket
        :param state: recall success/failure
        :return: new bucket number
        """
        if bucket not in SpacedRepetition.buckets.keys():
            raise ValueError("Bucket number is incorrect.")

        if state == SpacedRepetition.states[0]:
            return 0
        elif state == SpacedRepetition.states[1]:
            return min(bucket + 1, list(SpacedRepetition.buckets.keys())[-1])
        elif state == SpacedRepetition.states[2]:
            return min(bucket + 2, list(SpacedRepetition.buckets.keys())[-1])
        else:
            raise ValueError("State is incorrect.")

    def __init__(self, language: str):
        if language not in SUPPORTED_LANGUAGES:
            raise ValueError("Language is incorrect.")

        self.language = language
        self.engine = create_engine(f"sqlite:///../data/{language}.db")
        Base.metadata.create_all(bind=self.engine)

        self.session = Session(self.engine)

    def add_word(self, word: str, definition: str):
        new_word = Word(word=word, definition=definition)
        self.session.add(new_word)
        self.session.commit()
        logger.info("Added new word: " + str(new_word))

    def get_words_to_revise(self):
        return list(
            self.session.query(Word).filter(Word.next_rep == date.today())
        )

    def revise(self, word, state: str):
        word.bucket = SpacedRepetition.spaced_repetition_scheduler(
            word.bucket, state
        )
        word.last_rep = date.today()
        word.next_rep = word.last_rep + timedelta(
            days=SpacedRepetition.buckets[word.bucket]
        )
        self.session.commit()

    def _clear_database(self):
        metadata = MetaData()
        metadata.reflect(self.engine)
        metadata.drop_all(self.engine)
        self.engine.dispose()
        logger.info("Cleared database.")

    @staticmethod
    def _test_revise():
        """
        Tests revise() function
        !!! For some reason I wasn't able to make
            the test work in test_spaced_repetition.py
        !!! I always get OperationalError
            when I try to do anything involving the engine
        !!! To be analysed later
        :return:
        """
        db = SpacedRepetition("__test__")
        for i in range(5):
            db.add_word(word=f"Word{i}", definition=f"Definition{i}")

        words_to_revise = db.get_words_to_revise()
        for i, word in enumerate(words_to_revise):
            assert word.word == f"Word{i}"
            db.revise(word, state="OK")

        assert db.get_words_to_revise() == []
        db._clear_database()
        os.remove("../data/__test__.db")
        logger.debug("revise() test passed.")


class Word(Base):
    __tablename__ = "vocabulary"

    id = Column(Integer, primary_key=True)
    word = Column(String)
    definition = Column(String)
    bucket = Column(Integer)
    last_rep = Column(Date)
    next_rep = Column(Date)

    def __repr__(self) -> str:
        return (
            f"{self.word} : {self.definition}, "
            f"last repetition: {self.last_rep}, "
            f"next repetition: {self.next_rep}"
        )

    def __init__(self, word: str, definition: str):
        super().__init__()
        self.word = word
        self.definition = definition
        self.bucket = 0
        self.last_rep = date.today()
        self.next_rep = date.today()


if __name__ == "__main__":
    SpacedRepetition._test_revise()
