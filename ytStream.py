import bs4, requests, os
from pynput import keyboard

def on_press(key):
    try:
        if key.char is 'r':
            global repeat
            repeat = False
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

#some global variables
search_result = []
repeat = False

def take_seach_keyword():
    _search = input('\nSearch >> ')

    if _search == '--1':
        return -1

    _keyword = '+'.join(_search.split())
    return 'https://www.youtube.com/results?search_query='+_keyword


def search_youtube(_query):
    _search_result = requests.get(_query).text
    _soup = bs4.BeautifulSoup(_search_result, features="html5lib")

    div = [d for d in _soup.find_all('div', attrs={'class':'yt-lockup-dismissable'})]
    return div

def format_search_result(_result):
    
    _search_result = [] #[[href, track_title, track_period]]

    for r in _result:
        _a = [x for x in r.find_all('a') if x.has_attr('title')][0]
        _span = r.find_all('span', attrs={'class':'video-time'})

        _href = _a['href']
        _title = _a['title']
        _track_len = 'PLAYLIST'
        _str_len = str(_span)
    
        if _str_len != '[]':
            _str_len = _str_len.replace('>', '<')
            _track_len = _str_len.split('<')[2]
    
        if len(_href) != 0 and len(_title) != 0:
            _search_result.append([_href, _title, _track_len])

    return _search_result

def interpret_usr_input(_usr_input):
    global search_result
    _s_usr_input = _usr_input.split()
    print(_s_usr_input)

    if len(_s_usr_input) is 4:
        if _s_usr_input[0] is 'p':
            for i in range (int(_s_usr_input[1]), int(_s_usr_input[3])+1):
                play_music_bluk('https://www.youtube.com'+search_result[i-1][0])

        #elif _s_usr_input[0] is 'd':
            #download

    elif len(_s_usr_input) is 2:
        if _s_usr_input[0] is 'p':
            play_music('https://www.youtube.com'+search_result[int(_s_usr_input[1])-1][0])
    return None

def play_music(_href):
    # global repeat
    play = True

    while play is True:
        _cmd = 'mpv {0} --no-video'.format(_href)
        os.system(_cmd) 
        
        _usr_flag = input('>> ')
        
        if _usr_flag is 'b':
            play = False

def play_music_bluk(_href):
    _cmd = 'mpv {0} --no-video'.format(_href)
    os.system(_cmd)

def main():
    while True:
        keyword = take_seach_keyword()

        if keyword is -1:
            print('quit')
            break

        res = search_youtube(keyword)
        global search_result 
        search_result = format_search_result(res)

        index = 1
        for _r in search_result:
            if _r != '[]':
                print('{0}. {1} :: {2}'.format(index, _r[1], _r[2]))
                index+=1

        _usr_input = input('\n>> ')
        interpret_usr_input(_usr_input)

if __name__ == "__main__":
    main()


   
    
