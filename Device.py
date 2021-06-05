# -*- coding: utf-8 -*-
"""
Created on Fri May 28 12:14:21 2021

@author: simon
"""

import time
import random
import socket as sk

class Device:
    "Rappresenta il dispositivo che rileva la temperatura e umidità dal terreno"
    
    def __init__(self, clientIp, clientMac): 
       self.client_ip = clientIp
       self.client_mac = clientMac
       self.gateway = ("localhost", 8100)
       self.clientUDP = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)

    def Orario(self):                       
        #Questa funzione restituisce il momento in cui è avvenuta la misurazione
        momento = time.localtime()  

        ora = momento.tm_hour
        minuti = momento.tm_min
        orario = "%d.%d"%(ora,minuti)
        return(orario)

    def EseguiMisurazione(self):
    #Questa funzione restituisce i dati della misurazione, dove temperatura e 
    # umidità sono valori interi (casuali in questo caso).
        temperatura = random.randint(5, 40)
        umidità = random.randint(0,100)
        misurazione = "%d.%d"%(temperatura,umidità)
        return (misurazione)

    def InviaMessaggio(self):
        #Il device dopo aver eseguito la misurazione, codifica i dati e li invia
        # al gateway
        message = self.Orario()+'.'+self.EseguiMisurazione()
        print ('sending "%s"' % message)        
        self.clientUDP.sendto(message.encode(), self.gateway)
        

    