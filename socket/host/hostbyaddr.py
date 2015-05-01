import socket

hostname, aliases, addresses = socket.gethostbyaddr('119.81.96.50')
print 'Hostname  =', hostname
print 'Aliases   =', aliases
print 'Addresses =', addresses
