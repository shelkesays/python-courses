import socket

for host in ['homer', 'www', 'www.python.org', 'rahulshelke.com', 'surgeonsquests.com']:
    try:
        print '%15s : %s' % (host, socket.gethostbyname(host))
    except socket.error as msg:
        print '%15s : ERROR: %s' % (host, msg)
