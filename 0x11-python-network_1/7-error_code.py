#!/usr/bin/python3
''' fetches https://alx-intranet.hbtn.io/status using requests'''


if __name__ == '__main__':
    import requests
    from sys import argv
    url = argv[1]
    content = requests.get(url)
    if content.status_code >= 400:
        print("Error code: {}".format(content.status_code))
    else:
        print(content.text)
