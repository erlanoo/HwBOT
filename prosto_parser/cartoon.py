from bs4 import BeautifulSoup
import requests

URL = "https://rezka.ag/cartoons/"


HEADERS = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

def get_requests(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_data(html):
    soup = BeautifulSoup(html,"html.parser")
    items = soup.find_all("div",class_='b-content__inline_item')
    cartoon = []

    for i in items:
        cartoon.append(
            {
                'link': i.find('div',class_='b-content__inline_item-cover').find('a').get('href'),
                'image': i.find('div',class_='b-content__inline_item-cover').find('a').find('img').get('src'),
                'title': i.find('div',class_='b-content__inline_item-link').find('a').getText()
  } )
    print(items)
    return cartoon[0].values()







def scrapy_cartoon():
    html = get_requests(URL)
    if html.status_code == 200:
        cartoon = []
        html = get_requests(URL)
        cartoon.extend(get_data(html.text))
        return cartoon
    else:
        raise Exception("Error in scrapy script function")