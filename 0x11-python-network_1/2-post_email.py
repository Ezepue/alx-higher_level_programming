#!/usr/bin/python3
'''
    Takes in a URL and an email, sends a POST request
    to the passed URL with the email as a parameter,
    and displays the body of the response (decoded in utf-8).
'''


if __name__ == '__main__':
    import urllib.request as ur
    import urllib.parse as up
    from sys import argv
    url = argv[1]
    variables = {'email': '{}'.format(argv[2])}
    datta = up.urlencode(variables).encode('utf-8')

    with ur.urlopen(url, data=datta) as response:
        content = response.read()
        print(content.decode('utf-8'))
