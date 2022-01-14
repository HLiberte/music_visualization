from bs4 import BeautifulSoup
import pandas as pd
import requests
import time

df = pd.read_csv('playlist.csv', header=None, error_bad_lines=False, names=['url'])

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}

for i in df['url']:
    time.sleep(2)
    url = 'https://music.163.com' + i
    response = requests.get(url=url, headers=headers)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    # 获取歌单标题
    title = soup.select('h2')[0].get_text().replace(',', '，')
    # 歌单作者
    author = soup.select('.name a')[0].get_text().replace(',', '，')
    # 日期
    date = soup.select('.user.f-cb span')[1].get_text().replace(' ', '').replace('创建', '')
    # 获取标签
    tags = []
    tags_message = soup.select('.u-tag i')
    for p in tags_message:
        tags.append(p.get_text())
    # 对标签进行格式化
    if len(tags) > 1:
        tag = '-'.join(tags)
    else:
        tag = tags[0]
    # 获取歌单收藏量
    collection = soup.select('#content-operation i')[1].get_text().replace('(', '').replace(')', '')
    # 转发量
    transmit = soup.select('#content-operation i')[2].get_text().replace('(', '').replace(')', '')
    # 评论数
    comments = soup.select('#cnt_comment_count')[0].get_text()
    # 歌曲数
    songs = soup.select('#playlist-track-count')[0].get_text()
    # 播放量
    play = soup.select('.s-fc6')[0].get_text()

    print(title, author, date, tag, collection, transmit, comments, songs, play)
    # 将详情页信息写入CSV文件中
    with open('music_message.csv', 'a+', encoding='utf-8-sig') as f:
        f.write(title + ',' + author + ',' + date + ',' + tag + ',' + collection + ',' + transmit + ',' + comments + ',' + songs + ',' + play + '\n')


