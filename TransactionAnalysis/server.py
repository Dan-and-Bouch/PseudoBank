import socket
from Analysis import analysis

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('10.83.3.188', 7000)
s.bind(address)
incomingPOS = 0
incomingPhone = 0

s.listen(1)
while True:
    connection, client_address = s.accept()
    print "hi"
    incomingPOS = connection.recv(1024)
    connection.close()
    connection, client_address = s.accept()
    incomingPhone = connection.recv(1024)
    analysis(incomingPOS, incomingPhone)
    # thing = incomingPOS.split(',')
    # print thing
    # break
# print type(incoming)
# incoming = str(incoming)
# print type(incoming)
#
# s.close()
# print thing
