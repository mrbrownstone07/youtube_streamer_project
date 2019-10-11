import bs4, requests, vlc, pafy, os

_search = input('\nsearch >> ')
_keyword = '+'.join(_search.split())

_query = 'https://www.youtube.com/results?search_query='+_keyword

page = requests.get(_query).text
soup = bs4.BeautifulSoup(page, features="html5lib")

div = [d for d in soup.find_all('div', attrs={'class':'yt-lockup-dismissable'})]

index = 1
LIST = []
for d in div:
    img0 = d.find_all('img')[0]
    a = [x for x in d.find_all('a') if x.has_attr('title')]
    img_link = img0['src'] if not img0.has_attr('data-thumb') else img0['data-thumb']
    _span = d.find_all('span', attrs={'class':'video-time'})

    _href = a[0]['href']
    _title = a[0]['title']

    _track_len = 'PLAYLIST'
    _str_len = str(_span)

    if _str_len != '[]':
        _str_len = _str_len.replace('>', '<')
        _track_len = _str_len.split('<')[2]

    LIST.append([_href, _title, _track_len])
    print('{}. {} :: {}'.format(index, _title, _track_len))
    index+= 1


i = int(input('\n>> '))

print('playing >> {}'.format(LIST[i-1][1]))
_link = 'https://www.youtube.com'+LIST[i-1][0]

cmd = 'mpv '+_link+' --no-video' 
os.system(cmd)


