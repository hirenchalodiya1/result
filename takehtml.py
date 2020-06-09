def make_html(rollnumber):
    import os
    first = rollnumber[:3]
    second = rollnumber[3:5]
    file_name = rollnumber + '.html'
    if(os.path.isfile(file_name)):
        pass
    else:
        try:
            url = f'http://gseb.org/285soipmahc/ssc/{first}/{second}/{rollnumber}.html'
            command = f'curl -v {url} -o {rollnumber}.html'
            os.system(command)
        except:
            print('No internet connection')


def get_html(rollnumber):
    import urllib.request
    first = rollnumber[:3]
    second = rollnumber[3:5]
    file_name = rollnumber + '.html'
    url = 'http://gseb.org/285soipmahc/ssc/'+first+'/'+second+'/'+rollnumber+'.html'

    urllib.request.urlretrieve(url,file_name)
    print(file_name+' downloaded')

def get_url(rollnumber):
    first = rollnumber[:3]
    second = rollnumber[3:5]
    file_name = rollnumber + '.html'
    url = 'http://gseb.org/285soipmahc/ssc/'+first+'/'+second+'/'+rollnumber+'.html'
    return url

def path_only(rollnumber):
    pass