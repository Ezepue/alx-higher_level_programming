#!/usr/bin/python3
'''
    Takes in a URL, sends a request to the URL and displays the value
    of the X-Request-Id variable found in the header of the response.
'''


if __name__ == '__main__':
    import urllib.request as ur
    from sys import argv
    url = argv[1]

    with ur.urlopen(url) as response:
        content = response.getheader('X-Request-Id')
        print(content)
