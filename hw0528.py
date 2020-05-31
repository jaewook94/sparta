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
    # a = a+1
    rank_tag = song.select_one('td.number')
    span_elements = rank_tag.find_all("span")
    for span in span_elements:
        span.extract()  #불필요한 부분(span)을 빼는 과정
    
    title_tag = song.select_one('td.info > a.title.ellipsis')
    artist_tag = song.select_one('td.info > a.artist.ellipsis')
    
    

    if title_tag is not None:
        # rank = a # 1에서 50까지 줌..(수정 전!)
        rank_with_blank = rank_tag.text
        rank = rank_with_blank.rstrip() #오른쪽 공백 제거

        title_with_blank = title_tag.text 
        title = title_with_blank.lstrip() #왼쪽 공백 제거

        artist = artist_tag.text
        
        print(rank, title, "| By.",artist)
        # print({:<10} artist.format(rank))
                                            