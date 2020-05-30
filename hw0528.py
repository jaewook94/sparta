import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

a = 0
songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
#music-list-wrap > table > tbody > tr
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
for song in songs:
    a = a+1
    # td.title > div > a
    rank_tag = song.select_one('td.number')
    title_tag = song.select_one('td.info > a.title.ellipsis')
    artist_tag = song.select_one('td.info > a.artist.ellipsis')

    if title_tag is not None:
        # rank = rank_tag.text
        rank = a #이 부분이 문제...그냥 1에서 50까지 줌..
        title_row = title_tag.text #공백이 아직 존재하는 row title
        title = title_row.lstrip() #구글링 lstrip은 왼쪽 공백을 모두 제거
        artist = artist_tag.text
        print(rank, title, "| By.",artist)
        # print({:<10} artist.format(rank))
                                            