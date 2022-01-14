from bs4 import BeautifulSoup
import requests
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}

for i in range(0, 1330, 35):
    print('正在爬取第{}页'.format(int(i/35)))
    time.sleep(2)
    url = 'https://music.163.com/discover/playlist/?cat=全部&order=hot&limit=35&offset=' + str(i)
    response = requests.get(url=url, headers=headers)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    # 获取包含歌单详情页网址的标签
    ids = soup.select('.dec a')
    # 获取包含歌单索引页信息的标签
    lis = soup.select('#m-pl-container li')
    for j in range(len(lis)):
        # 获取歌单详情页地址
        url = ids[j]['href']

        with open('playlist.csv', 'a+', encoding='utf-8-sig') as f:
            f.write(url + '\n')
        print(url)

