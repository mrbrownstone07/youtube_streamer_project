import bs4, requests, os

def __search_and_play():
    _search = input('search>> ')
    
    if _search == '--q':
        return -1

    _keyword = '+'.join(_search.split())

    _query = 'https://www.youtube.com/results?search_query='+_keyword

    page = requests.get(_query).text
    soup = bs4.BeautifulSoup(page, features="html5lib")

    div = [d for d in soup.find_all('div', attrs={'class':'yt-lockup-dismissable'})]

    index = 1
    LIST = [[]]
    for d in div:
        img0 = d.find_all('img')[0]
        a0 = [x for x in d.find_all('a') if x.has_attr('title')]
        img_link = img0['src'] if not img0.has_attr('data-thumb') else img0['data-thumb']
        len = d.find_all('span', attrs={'class':'video-time'})
        _track_len = 'PLAYLIST'
        _str_len = str(len)
        if _str_len != '[]':
            _str_len = _str_len.replace('>', '<')
            _track_len = _str_len.split('<')[2]
        
        LIST.append([a0[0]['href'], a0[0]['title']])

        print(str(index)+'.'+a0[0]['title']+' :: '+_track_len)
        index+= 1

    i = int(input('>> '))

    if i < 1:
        return 0

    _link = 'https://www.youtube.com'+LIST[i][0]

    print('Playing >> '+LIST[i][1])

    cmd = 'mpv '+_link+' --no-video'
    while True: 
        os.system(cmd)
        _job_flag = input("r to repeat / q to go back to search? >> ")
        if _job_flag == 'r':
            print('REPEATING')
            continue
        elif _job_flag == 'q':
            return 0
        else: 
            main()

def main():
    while True:
       r = __search_and_play()
       if r is -1:
           break
        


if __name__ == "__main__":
    main()


# _query = 'https://www.youtube.com/results?search_query=queens+of+the+stone+age'
# page = requests.get(_query).text
# soup = bs4.BeautifulSoup(page, features="html5lib")

# div = [d for d in soup.find_all('div', attrs={'class':'yt-lockup-dismissable'})]

# index = 1

# for d in div:
#     img0 = d.find_all('img')[0]
#     a0 = [x for x in d.find_all('a') if x.has_attr('title')]
#     img_link = img0['src'] if not img0.has_attr('data-thumb') else img0['data-thumb']
    
#     len = d.find_all('span', attrs={'class':'video-time'})
#     _track_len = 'PLAYLIST'
#     _str_len = str(len)
#     if _str_len != '[]':
#         _str_len = _str_len.replace('>', '<')
#         _track_len = _str_len.split('<')[2]
        
#     print(str(index)+'.'+a0[0]['title']+' :: '+_track_len)
#     index+= 1