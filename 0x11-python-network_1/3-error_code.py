#!/usr/bin/python3
''' fetches https://alx-intranet.hbtn.io/status using urllib'''


if __name__ == '__main__':
    import urllib.error as ue
    import urllib.request as ur
    from sys import argv
    url = argv[1]
    try:
        with ur.urlopen(url) as response:
            content = response.read()
            print(content.decode('utf8'))
    except ue.HTTPError as e:
        print("Error code: {}".format(e.code))
