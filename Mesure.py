import visa
import Fenetre
import Parcourir
import datetime

ID = 'TCPIP0::192.168.1.30::inst0::INSTR'
try:
    rm = visa.ResourceManager()
    rm.list_resources()
    VNA = rm.open_resource(ID)
except:
    print("Connection VNA impossible\n")
s11 = []
s12 = []
s21 = []
s22 = []
Sxx = ''
repD = 0
repF = 0
Flag = 0
Flag2 = 0
Flag3 = 0
Flag4 = 0


def AskData():
    commandefmin = ":SENSe:FREQuency:STARt?\n"
    commandefmax = ":SENSe:FREQuency:STOP?\n"
    commandenbpoint = ":SENSe:SWEep:POINts?\n"
    commandecal = ":SENS:CORRection:STATe?\n"
    listData = []
    try:
        response = VNA.query(commandefmin)
        fmin = int(response)
        response = VNA.query(commandefmax)
        fmax = int(response)
        response = VNA.query(commandenbpoint)
        nbPoints = int(response)
        response = VNA.query(commandecal)
        if response == '1':
            isCalibrated = True
        else:
            isCalibrated = False
        listData = [fmin, fmax, nbPoints, isCalibrated]
    except:
        print("Error !")

    # get S11 param
    # Demander S11 sur trace 1
    # Mettre en domaine fq
    # Récupérer les données
    # 8 premiers caractères nuls et le restes séparés par une virgule
    # Sortie : un tableau de double reel imaginaire [reel][imaginaire][reel][imaginaire][reel][imaginaire]


def S11():
    S11Trace1 = ":SENSe:TRACe1:SPARams S11\n"
    Tracefq = ":SENSe:TRACe1:DOMain FREQuency\n"
    GetS11 = ":TRACe:DATA? 1\n"
    Sxx = 'S11'

    try:
        VNA.write(S11Trace1)
        VNA.write(Tracefq)
        response = VNA.query(GetS11)
        response = response[1:]  # on enleve le #
        nbDigit = response[0]
        response = response[1:]  # on enleve le digit number
        nb = response[0:int(nbDigit)]
        response = response[int(nbDigit):]
        s11Tab = response.split(",")
        if Fenetre.Form1 is 1:
            s11TabT = str(s11Tab)
            s11TabT = s11TabT.replace("[\'", "")
            s11TabT = s11TabT.replace("\'", "")
            s11TabT = s11TabT.replace("'']", "")
            s11TabT = s11TabT.replace("]", "")
            s11TabT = s11TabT.replace(",", ";")
            Eregistrer(s11TabT)
            Eregistrer("\n")
    except:
        print("error getting S11")


def S12():
    S12Trace1 = ":SENSe:TRACe2:SPARams S12\n"
    Tracefq = ":SENSe:TRACe2:DOMain FREQuency\n"
    GetS12 = ":TRACe:DATA? 2\n"
    Sxx = 'S12'

    try:
        VNA.write(S12Trace1)
        VNA.write(Tracefq)
        response = VNA.query(GetS12)
        response = response[1:]  # on enleve le #
        nbDigit = response[0]
        response = response[1:]  # on enleve le digit number
        nb = response[0:int(nbDigit)]
        response = response[int(nbDigit):]
        s12Tab = response.split(",")
        if Fenetre.Form1 is 1:
            s12TabT = str(s12Tab)
            s12TabT = s12TabT.replace("[\'", "")
            s12TabT = s12TabT.replace("\'", "")
            s12TabT = s12TabT.replace("'']", "")
            s12TabT = s12TabT.replace("]", "")
            s12TabT = s12TabT.replace(",", ";")
            Eregistrer(s12TabT)
            Eregistrer("\n")
    except:
        print("error getting S12")


def S21():
    global s21
    S21Trace1 = ":SENSe:TRACe3:SPARams S21\n"
    Tracefq = ":SENSe:TRACe3:DOMain FREQuency\n"
    GetS21 = ":TRACe:DATA? 3\n"
    Sxx = 'S21'

    try:
        VNA.write(S21Trace1)
        VNA.write(Tracefq)
        response = VNA.query(GetS21)
        response = response[1:]  # on enleve le #
        nbDigit = response[0]
        response = response[1:]  # on enleve le digit number
        nb = response[0:int(nbDigit)]
        response = response[int(nbDigit):]
        s21Tab = response.split(",")
        if Fenetre.Form1 is 1:
            s21TabT = str(s21Tab)
            s21TabT = s21TabT.replace("[\'", "")
            s21TabT = s21TabT.replace("\'", "")
            s21TabT = s21TabT.replace("'']", "")
            s21TabT = s21TabT.replace("]", "")
            s21TabT = s21TabT.replace(",", ";")
            Eregistrer(s21TabT)
            Eregistrer("\n")
    except:
        print("error getting S21")


def S22():
    S22Trace1 = ":SENSe:TRACe4:SPARams S22\n"
    Tracefq = ":SENSe:TRACe4:DOMain FREQuency\n"
    GetS22 = ":TRACe:DATA? 4\n"
    Sxx = 'S22'

    try:
        VNA.write(S22Trace1)
        VNA.write(Tracefq)
        response = VNA.query(GetS22)
        response = response[1:]  # on enleve le #
        nbDigit = response[0]
        response = response[1:]  # on enleve le digit number
        nb = response[0:int(nbDigit)]
        response = response[int(nbDigit):]
        s22Tab = response.split(",")
        if Fenetre.Form1 is 1:
            s22TabT = str(s22Tab)
            s22TabT = s22TabT.replace("[\'", "")
            s22TabT = s22TabT.replace("\'", "")
            s22TabT = s22TabT.replace("'']", "")
            s22TabT = s22TabT.replace("]", "")
            s22TabT = s22TabT.replace(",", ";")
            Eregistrer(s22TabT)
            Eregistrer("\n")
    except:
        print("error getting S22")


def STATUS():
    commandestatus = ":STATus:OPERation? \n"
    Fstat = False
    try:
        Stat = VNA.query(commandestatus)
        if Stat == 0:
            Stat = VNA.query(commandestatus)
            Fstat = False
        else:
            Fstat = True
    except:
        print("Error !")
    return Fstat


def Eregistrer(res):
    global Flag, repD
    if Fenetre.Form1 is 1:
        path = str(Parcourir.fileName)
        if ".csv" in path:
            Fichier = path
        else:
            Fichier = path + ".csv"
        try:
            if Flag == 0:
                Ans = open(Fichier, "a")
                Ans.write(str(res))
                Ans.close()
            else:
                Ans = open(Fichier, "w+")
                Freqquery()
                Nb = NBsweepPoint_Req()
                inter = (repF - repD) / Nb
                while repD <= repF:
                    Ans.write(repD)
                    Ans.write(" Hz")
                    Ans.write(";")
                    repD = repD + inter
                Ans.write("\n")
                Ans.write(str(res))
                Ans.close()
                Flag = True
        except:
            pass


def Enregistrer_Mark(mark):
    global Flag3
    if Fenetre.Form2 is 1:
        path = str(Parcourir.fileName)
        if "_Mark.text" in path:
            Fichier = path
        else:
            Fichier = path + "_Mark.txt"
        try:
            if Flag3 == 0:
                Ans = open(Fichier, "a")
                Ans.write(str(mark))
                Ans.close()
            else:
                Ans = open(Fichier, "w+")
                Ans.write(str(mark))
                Ans.close()
                Flag3 = True
        except:
            pass


def Enregistrer_log():
    global Flag4, cal2
    pos = 0
    date = str(datetime.datetime.now())
    path = str(Parcourir.fileName)
    if "_Log.txt" in path:
        Fichier = path
    else:
        Fichier = path + "_Log.txt"
    if ".csv_Log.txt" in Fichier:
        Fichier = Fichier.replace('.csv_Log.txt', '_Log.txt')
    Freqquery()
    repF2 = repF / 1000000
    repD2 = repD / 1000000
    Nb = NBsweepPoint_Req()
    IFBW = VNA.query(":SENSe:SWEep:IFBW?")
    Av = VNA.query(":SENSe:AVERage:COUNt?")
    cal = VNA.query(':SENSe:CORRection:STATe?')
    if "1" in cal:
        cal2 = "Calibration ON"
    else:
        cal2 = "Calibration OFF"
    try:
        Ans = open(Fichier, "a")
        Ans.write(Fichier)
        Ans.write("\n\n")
        Ans.write("Date and hour : ")
        Ans.write(date)
        Ans.write("\n\n")
        Ans.write("Start Frequency : ")
        Ans.write(str(repD2))
        Ans.write(" MHz \n")
        Ans.write("End Frequency : ")
        Ans.write(str(repF2))
        Ans.write(" MHz \n")
        Ans.write("Number of sweep points : ")
        Ans.write(str(Nb))
        Ans.write("\n")
        Ans.write("IFBW : ")
        Ans.write(str(IFBW))
        Ans.write(" Hz \n")
        Ans.write("Average : ")
        Ans.write(str(Av))
        Ans.write("\n")
        Ans.write(cal2)
        Ans.write("\n\n")
        Ans.write(str(Fenetre.axis1))
        Ans.write(" : ")
        Ans.write("\n")
        Ans.write("\tStart : ")
        Ans.write(str(Fenetre.Pmin1))
        Ans.write("mm\n")
        Ans.write("\tEnd : ")
        Ans.write(str(Fenetre.Pmax1))
        Ans.write("mm\n")
        if Fenetre.axis2 is not '':
            Ans.write(str(Fenetre.axis2))
            Ans.write(" : ")
            Ans.write("\n")
            Ans.write("\tStart : ")
            Ans.write(str(Fenetre.Pmin2))
            Ans.write("mm\n")
            Ans.write("\tEnd : ")
            Ans.write(str(Fenetre.Pmax2))
            Ans.write("mm\n")
            Ans.close()
        else:
            Ans.close()
    except:
        print("Error Write Log")


def NBsweepPoint():
    rep = Fenetre.Fnb
    VNA.write(":SENSe:SWEep:POINts " + rep + "\n")


def NBsweepPoint_Req():
    rep = int(VNA.query(":SENSe:SWEep:POINts?"))
    return rep


def HoldToggle():
    rep = VNA.query(":INITiate:HOLD?\n")
    if '1' in rep:
        VNA.write(":INITiate:HOLD 0\n")
    else:
        VNA.write(":INITiate:HOLD 1\n")


def SetFreq():
    commandD = ':SENSe:FREQuency:STARt' + str(Fenetre.FreqD) + 'GHZ\n'
    commandF = ':SENSe:FREQuency:STOP' + str(Fenetre.FreqF) + 'GHZ\n'
    VNA.write(commandD)
    VNA.write(commandF)


def Freqquery():
    global repD, repF
    commandD = ':SENSe:FREQuency:STARt?'
    commandF = ':SENSe:FREQuency:STOP?'
    repD = float(VNA.query(commandD))
    repF = float(VNA.query(commandF))


def Holdinit():
    rep = VNA.query(":INITiate:HOLD?\n")
    if '1' in rep:
        VNA.write(":INITiate:HOLD 0\n")
    else:
        pass


def Marker():
    if Fenetre.Form2 is 1:
        Mark = VNA.query(':CALCulate:MARKer:DATA?')
        Enregistrer_Mark(Mark)
        Enregistrer_Mark("\n")


def init():
    global repD
    Freqquery()
    Nb = NBsweepPoint_Req()
    inter = (repF - repD) / Nb
    while repD <= repF:
        Eregistrer(repD)
        Eregistrer(" Hz")
        Eregistrer(";")
        repD = repD + inter
    Eregistrer("\n")
