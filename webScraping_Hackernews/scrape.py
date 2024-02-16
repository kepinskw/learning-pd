import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')

links = soup.select('.titleline > a')
subtext = soup.select('.subtext')


def sort_by_votes(hnlist):
    return sorted(hnlist, key=lambda key: key['votes'])


def create_custom_news(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_by_votes(hn)


if __name__ == '__main__':
    print(create_custom_news(links, subtext))
