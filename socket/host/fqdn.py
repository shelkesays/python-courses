import socket

for host in ['rahulshelke', 'surgeonsquests', 'www']:
    print '%6s : %s' % (host, socket.getfqdn(host))
