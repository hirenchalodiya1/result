def make_html(rollnumber):
    import os
    first = rollnumber[:3]
    second = rollnumber[3:5]
    file_name = rollnumber + '.html'
    if(os.path.isfile(file_name)):
        pass
    else:
        try:
            (os.system('wget http://gseb.org/522lacigam/sci/'+first+'/'+second+'/'+rollnumber+'.html'))
        except:
            print('No internet connection')


def get_html(rollnumber):
    import urllib.request
    first = rollnumber[:3]
    second = rollnumber[3:5]
    file_name = rollnumber + '.html'
    url = 'http://gseb.org/522lacigam/sci/'+first+'/'+second+'/'+rollnumber+'.html'

    urllib.request.urlretrieve(url,file_name)
    print(file_name+' downloaded')