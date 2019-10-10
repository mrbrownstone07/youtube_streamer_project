import bs4, requests, vlc, pafy, os

_search = input('search>> ')
_keyword = '+'.join(_search.split())

_query = 'https://www.youtube.com/results?search_query='+_keyword

page = requests.get(_query).text
soup = bs4.BeautifulSoup(page, features="html5lib")

div = [d for d in soup.find_all('div', attrs={'class':'yt-lockup-dismissable'})]

index = 1
LIST = []
for d in div:
    img0 = d.find_all('img')[0]
    a0 = [x for x in d.find_all('a') if x.has_attr('title')]
    img_link = img0['src'] if not img0.has_attr('data-thumb') else img0['data-thumb']
    LIST.append(a0[0]['href'])
    print(str(index)+'.'+a0[0]['title'])
    index+= 1

i = int(input('>> '))

_link = 'https://www.youtube.com'+LIST[i-1]

cmd = 'mpv '+_link+' --no-video' 
os.system(cmd)


