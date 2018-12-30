import urllib.request

try:
    url = urllib.request.urlopen('https://www.python.org/')
    content = url.read()
except urllib.error.HTTPError as e:
    print('Cannot find web page.')
    print(e)
    exit()
except Exception as e:
    print(e)

f = open('python.html', 'wb')
f.write(content)
f.close()
