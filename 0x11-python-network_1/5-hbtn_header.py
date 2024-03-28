#!/usr/bin/python3
'''
Sends a request to the URL and displays the value
of the variable X-Request-Id in the response header.
'''


if __name__ == '__main__':
    import requests
    from sys import argv
    url = argv[1]
    content = requests.get(url)
    request_id = content.headers.get('X-Request-Id')
    print(request_id)
