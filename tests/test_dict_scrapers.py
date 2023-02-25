import pytest

from src.dict_scrapers import scrape_oxford_learners_dictionary


@pytest.mark.parametrize(
    "word, defs",
    [
        (
            "cat",
            [
                "(noun) a small animal with soft fur "
                "that people often keep as a pet. "
                "Cats catch and kill birds and mice.",
                "(noun) a wild animal of the cat family",
                "(-) a first name for girls, short for Catherine or Katherine",
            ],
        ),
        (
            "cucumber",
            [
                "(noun) a long vegetable with dark green skin "
                "that is light green inside, usually eaten raw"
            ],
        ),
        (
            "rub",
            [
                "(verb) to move your hand, a cloth, etc., "
                "backwards and forwards over a surface while pressing it",
                "(verb) to press two surfaces against each other "
                "and move them backwards and forwards; "
                "to be pressed together and move in this way",
                "(verb) to move backwards and forwards "
                "many times against something "
                "while pressing it, especially causing pain or damage",
                "(verb) to spread a liquid or other substance "
                "over a surface while pressing it",
                "(noun) an act of rubbing a surface",
                "(noun) a problem or difficulty",
            ],
        ),
        ("justsomenonsense", []),
    ],
)
def test_scrape_oxford_learners_dictionary(word, defs):
    assert scrape_oxford_learners_dictionary(word) == defs
