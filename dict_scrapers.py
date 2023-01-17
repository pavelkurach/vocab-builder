import requests
from bs4 import BeautifulSoup


def scrape_oxford_learners_dictionary(word: str) -> list[str]:
    url = lambda i: f'https://www.oxfordlearnersdictionaries.com/definition/english/{word}_{i}'

    # The website filters out requests without a proper User-Agent
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0',
    }

    list_of_definitions = []

    for i in range(1, 5, 1):
        response = requests.get(url(i), headers=headers)
        if response.status_code != 200:
            break
        page = response.text
        soup = BeautifulSoup(page, 'html.parser')

        try:
            pos = soup.find('span', class_='pos').text
        except AttributeError:
            pos = '-'

        try:
            senses = soup.find('ol', class_='senses_multiple')
            list_of_senses = senses.find_all('li', class_='sense', recursive=False)
        except AttributeError:
            try:
                senses = soup.find('ol', class_='sense_single')
                list_of_senses = senses.find_all('li', class_='sense', recursive=False)
            except AttributeError:
                break

        for sense in list_of_senses:
            definition = sense.find('span', class_='def')
            list_of_definitions.append(f'({pos}) ' + definition.text)

    return list_of_definitions
