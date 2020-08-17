import socket

IP = '192.168.1.100'
PORT = 50000
Fichier = "Ressource\Action.seq"
Answer = "Ressource\Answer.txt"
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
except:
    print("Connection controleur impossible\n")
Ans = open(Answer, "wb")
Ack = False
s.send(b"SL40\n")
s.send(b"SD1000\n")
s.send(b"AD500\n")


def Envois():
    try:
        LB = open(Fichier, "rb")
        EB = LB.read()
        s.send(EB)
        LB.close()
    except socket.error as msg:
        s.close()


def Reception():
    global Data, iRep, Ack
    Ans.write(b'')
    Ack = False
    try:
        Data = s.recv(1024)
        Ans.write(Data)
    except socket.error as msg:
        pass
    iRep = Data
    Ack = True
    return Ack


def Choix_Axe(x):
    if x is 0:
        s.send(b"AS0\n")
    elif x is 1:
        s.send(b"AS1\n")
    elif x is 2:
        s.send(b"AS2\n")
    elif x is 3:
        s.send(b"AS3\n")


def Choix_position(iVal):
    oVal = float(iVal) * 100
    iPos = str(oVal)
    oSeq = open(Fichier, "w")
    oSeq.write("TP" + iPos + "\n")
    oSeq.close()
    Envois()
    s.send(b"GT\n")


def Increment_pos(Val):
    global iPos
    s.send(b'CP\n')
    Reception()
    iRep2 = int(iRep)
    iVal = iRep2 / 100
    oVal = (iVal + Val) * 100
    iPos = str(oVal)
    oSeq = open(Fichier, "w")
    oSeq.write("TP" + iPos + "\n")
    oSeq.close()
    Envois()
    s.send(b"GT\n")


def Position_request():
    Ans.write(b"")
    s.send(b'CP\n')
    Reception()
    iRep2 = int(iRep)
    iVal = iRep2 / 100
    return iVal


def SO():
    flag = False
    s.send(b"AS1\n")
    s.send(b"SO\n")
    Reception()
    if b'E0' in Data and flag is False:
        s.send(b"AS2\n")
        s.send(b"SO\n")
        flag = True
        Reception()
    if b'E0' in Data and flag is True:
        s.send(b"AS3\n")
        s.send(b"SO\n")
        flag = False
        s.close()


def Set_origine():
    s.send(b'PZ\n')


def STOP():
    try:
        s.send(b'HI\n')
    except:
        print("problème stop")
