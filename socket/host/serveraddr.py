import socket

def get_constants(prefix):
    """ Create dictionary mapping socket module constants to their names."""
    return dict((getattr(socket, n), n)
                for n in dir(socket)
                if n.startswith(prefix)
                )


families = get_constants('AF_')
types = get_constants('SOCK_')
protocols = get_constants('IPPROTO_')

for response in socket.getaddrinfo('surgeonsquests.com', 'https'):

    # Unpack the response tuple
    family, socktype, proto, canonname, sockaddr = response

    print 'Family        :', families[family]
    print 'Type          :', types[socktype]
    print 'Protocol      :', protocols[proto]
    print 'canonical name:', canonname
    print 'Socket address:', sockaddr
    print
