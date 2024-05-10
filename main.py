import requests
from bs4 import BeautifulSoup

def get_python_org_headlines():
    url = "https://www.amazon.in/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    headlines = []
    for headline in soup.find_all('h2'):
        headlines.append(headline.text)

    return headlines

headlines = get_python_org_headlines()
for headline in headlines:
    print(headline)