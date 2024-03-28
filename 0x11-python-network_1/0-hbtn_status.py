#!/usr/bin/python3
''' fetches https://alx-intranet.hbtn.io/status using urllib'''


if __name__ == '__main__':
    import urllib.request as ur
    url = 'https://alx-intranet.hbtn.io/status'

    with ur.urlopen(url) as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf8')))
