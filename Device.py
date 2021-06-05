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
    
    def Orario(self):                       
        #Questa funzione restituisce il momento (ora:minuti) in cui è avvenuta la misurazione
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
        gateway = ("localhost", 8100)
        
        
        #Inizio a calcolare il tempo appena prima di creare la socket e inviare
        # la misurazione
        tinizio = time.time()
        clientUDP = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
        clientUDP.sendto(message.encode(), gateway)
        
        #Momento in cui invio il pacchetto
        tinvio = time.time()
        data, address = clientUDP.recvfrom(1024)
        
        #Momento in cui ricevo il pacchetto di risposta dal gateway
        tricezione = time.time()
        
        
        '''ATTENZIONE:
            Il tempo che passa tra la creazione della socket e il momento in cui 
            il pacchetto di risposta ritorna al device SPESSO è molto breve e 
            python lo arrotonda a 0
        '''
        RTT = tricezione - tinvio
        
        #Per tempo totale si intende il tempo che passa dalla creazione della 
        #socket, alla ricezione del pacchetto di risposta dal gateway
        tTot = tricezione - tinizio
                
        print("Tempo di invio pacchetto: ", tTot)
        print("RTT: " , RTT, "\n\n")
        
        clientUDP.close()


    