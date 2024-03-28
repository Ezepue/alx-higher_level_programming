#!/usr/bin/python3
''' fetches https://alx-intranet.hbtn.io/status using requests'''


if __name__ == '__main__':
    import requests
    from sys import argv
    url = argv[1]
    data = {'email': argv[2]}
    content = requests.post(url, data=data)
    print(content.text)
