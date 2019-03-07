import json
import os

class Equipamento:
    def __init__(self, name="", layer=0, ports=[], info=""):
        self.eqp = {}
        self.eqp["Nome"] = name
        self.eqp["Layer"] = layer
        self.eqp["Portas"] = ports
        self.eqp["Info"] = info
        self.eqp["Id"] = -1

    def __writeToEqpFile(self):
        if(self.eqp["Id"] == -1):
            M = -1
            for root, dir, files in os.walk("equipamentos"):
                #print(files)
                a = [int(f[0:-5]) for f in files]
                #print(a)
            if(a != []):
                M = max(a) 
            self.eqp["Id"] = M+1
        #Assync write can generate dup Ids
        with open("equipamentos/" + str(self.eqp["Id"]) + ".json", "w") as f:
            json.dump(self.eqp, f, indent=2, sort_keys=True)
        #print(str(self.eqp["Id"]) + ".json " + self.eqp["Nome"])
        return True

    def saveEqp(self):
        ok = True
        if(not isinstance(self.eqp["Info"], str)):
            ok = False          

        if(not isinstance(self.eqp["Id"], int)):
            ok = False          

        if(not isinstance(self.eqp["Layer"], int) or self.eqp["Layer"] < 1 or self.eqp["Layer"] > 7):
            ok = False          

        if(not isinstance(self.eqp["Nome"], str) or self.eqp["Nome"] == ""):
            ok = False          

        if(not isinstance(self.eqp["Portas"], list) or self.eqp["Portas"] == []):
            ok = False          


        if(ok):
            return self.__writeToEqpFile()
        else:
            print("Objeto mal formado. Favor verificar atributos.")
            #print(str(self.eqp["Id"]) + ".json " + str(self.eqp["Nome"]))
            return False

    def __readFromEqpFile(self, fileName):
        with open(fileName) as f:
            e = json.load(f)
        #print(type(e))
        #print(e)
        return e


    def loadEqp(self, idNum):
        fileName = "equipamentos/" + str(idNum) + ".json"
        self.eqp = self.__readFromEqpFile(fileName) 

    def loadEqpByName(self, name):
        self.eqp = self.__readFromEqpFile(name) 
""" 
    def editL1Connection(self, portLocal, eqpRemote, portRemote):
        print(self.eqp["L1_conexoes"][0])
        self.eqp["L1_conexoes"][portLocal] = [eqpRemote.eqp["Id"], eqpRemote.eqp["Nome"], portRemote]


    def connectPorts(self, portLocal, eqpRemote, portRemote):
        if(self.eqp["L1_conexoes"][portLocal] != [-1, "", -1]):
            print("Porta local já conectada.")
            return False

        if(eqpRemote.eqp["L1_conexoes"][portRemote] != [-1, "", -1]):
            print("Porta remota já conectada.")
            return False

        self.editL1Connection(portLocal, eqpRemote, portRemote)
        eqpRemote.editL1Connection(portRemote, self, portLocal)
        self.saveEqp()
        eqpRemote.saveEqp()
        return True
"""
