import socket

from urlparse import urlparse

for url in ['https://qpeka.com',
            'https:mycuteoffice.com',
            'https://surgeonsquests.com',
            'http://rahulshelke.com',
            'ftp://prep.ai.mit.edu',
            'gopher://gopher.micro.umn.edu',
            'smtp://mail.example.com',
            'imap://mail.example.com',
            'imaps://mail.example.com',
            'pop3://pop.example.com',
            'pop3s://pop.example.com']:
    parsed_url = urlparse(url)
    port = socket.getservbyname(parsed_url.scheme)
    print '%6s : %s' % (parsed_url.scheme, port)
