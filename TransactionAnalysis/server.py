import socket
from Analysis import analysis
from OBPAPI import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('10.83.3.188', 7000)
s.bind(address)
incomingPOS = 0
incomingPhone = 0
openbank = auth()

phone_address = ("10.83.3.245", 7000)

s.listen(1)
while True:
    try:
        pos_connection, pos_address = s.accept()
        print "hi"
        incomingPOS = pos_connection.recv(1024)
        # phone_connection, phone_address = s.accept()
        p = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print "uuuggghhhh"
        p.settimeout(5)
        p.connect(phone_address)
        print "ugh"
        try:
            incomingPhone = p.recv(1024)
        except Exception:
            pos_connection.send("0")
            print incomingPOS, " ----- ", incomingPhone
            print "nay"

        print incomingPhone

        if incomingPhone is None:
            pos_connection.send("0")
            print incomingPOS, " ----- ", incomingPhone
            print "nay"

        else:
            if analysis(incomingPOS, incomingPhone):
                pos_connection.send("1")

                print get_balance(openbank)

                transact("1000", openbank)

                print get_balance(openbank)
                print "yay"
            else:
                pos_connection.send("0")
                print incomingPOS, " ----- ", incomingPhone
                print "nay"
    except Exception:
        pass

# 1458