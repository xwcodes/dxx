import requests
import bs4

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 Edg/86.0.622.51'}


def get_target():
    url = 'http://news.cyol.com/gb/channels/vrGlAKDl/index.html'
    res = requests.get(url, headers=header)
    res.encoding = res.apparent_encoding
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    now_url = soup.select_one('li >h3 >a')['href']
    return now_url


def get_title(target):
    res = requests.get(target, headers=header)
    res.encoding = res.apparent_encoding
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    title = soup.head.title.string
    return title


def get_end_image(url):
    img_url = 'https://h5.cyol.com/special/daxuexi/{}/images/end.jpg'.format(url.split('/')[-2])
    return img_url


def write_html():
    target = get_target()
    title = get_title(target)
    img_url = get_end_image(target)
    with open('./template.html', encoding="utf-8") as f:
        html = f.read()
        html = html.replace('{title}', title)
        html = html.replace('{url}', img_url)
    with open('./index.html', 'w',encoding="utf-8") as h:
        h.write(html)


if __name__ == '__main__':
    write_html()
