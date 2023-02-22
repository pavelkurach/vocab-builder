import bs4
import requests
from bs4 import BeautifulSoup

SUPPORTED_LANGUAGES = ("EN", "__test__")


def scrape_oxford_learners_dictionary(word: str) -> list[str]:
    def url(i: int) -> str:
        return (
            f"https://www.oxfordlearnersdictionaries.com"
            f"/definition/english/{word}_{i}"
        )

    # The website filters out requests without a proper User-Agent
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) "
                      "Gecko/20100101 Firefox/42.0",
    }

    list_of_definitions = []

    for i in range(1, 5, 1):
        response = requests.get(url(i), headers=headers)
        if response.status_code != 200:
            break
        page = response.text
        soup = BeautifulSoup(page, "html.parser")

        find_pos = soup.find("span", class_="pos")
        if isinstance(find_pos, bs4.Tag):
            pos = find_pos.text
        else:
            pos = "-"

        find_senses = soup.find("ol", class_="senses_multiple")
        if isinstance(find_senses, bs4.Tag):
            list_of_senses = find_senses.find_all(
                "li", class_="sense", recursive=False
            )

        else:
            find_senses = soup.find("ol", class_="sense_single")
            if isinstance(find_senses, bs4.Tag):
                list_of_senses = find_senses.find_all(
                    "li", class_="sense", recursive=False
                )
            else:
                break

        for sense in list_of_senses:
            definition = sense.find("span", class_="def")
            list_of_definitions.append(f"({pos}) " + definition.text)

    return list_of_definitions
