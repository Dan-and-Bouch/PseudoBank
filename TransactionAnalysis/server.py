import socket
from Analysis import analysis

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('10.83.3.188', 7000)
s.bind(address)
incomingPOS = 0
incomingPhone = 0



phone_address = ("10.83.3.245", 7000)



s.listen(1)
while True:
    pos_connection, pos_address = s.accept()
    print "hi"
    incomingPOS = pos_connection.recv(1024)
    # phone_connection, phone_address = s.accept()
    p = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(5)
    p.connect(phone_address)
    incomingPhone = p.recv(1024)
    if analysis(incomingPOS, incomingPhone):
        pos_connection.send("1")
        print "yay"
    else:
        pos_connection.send("0")
        print incomingPOS, " ----- ", incomingPhone
        print "nay"

    pos_connection.close()
    p.close()
