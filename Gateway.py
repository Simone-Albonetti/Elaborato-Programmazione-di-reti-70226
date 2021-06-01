# -*- coding: utf-8 -*-
"""
Created on Sat May 29 12:14:23 2021

@author: simon
"""

import socket as sk

class Gateway:
    "Rappresenta il collegamento intermedio tra device e server"
    
    def __init__(self, indirizzoIpGateway, portaGateway):
        #Quando creo il Gateway viene creata anche la socket UDP verso i device
        self.socketUDP = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
        self.indirizzoGateway = (indirizzoIpGateway, portaGateway)
        self.socketUDP.bind(self.indirizzoGateway)
        print ('\n\r Gateway UDP in funzione %s porta %s' %self.indirizzoGateway)

        misurazioni = []
        indirizzi = []
        
        while True:
            # Anche qui si è scelto come nel buffer della socket del server 
            # di utilizzare un buffer piccolo poichè vengono trasferiti pochi dati
            # alla volta e il rischi di riempire il buffer è molto basso
            data, address = self.socketUDP.recvfrom(1024)
            
            #Le misurazioni vengono inserite in un array
            misurazioni.append(data.decode('utf8'))     
            
            #Gli indirizzi dei device vengono inseriti in un array
            indirizzi.append(address)
            
            #Quando sia i 2 array (indirizzi e misurazioni) hanno ricevuto i dati
            # dai 4 device, il gateway invia al server le informazioni
            if len(misurazioni) == 4 & len(indirizzi) == 4:
                self.InviaMisurazioni(misurazioni,indirizzi)
                
                #Si svuotano le misurazioni e gli indirizzi
                misurazioni = []
                indirizzi = []
     
    def InviaMisurazioni(self,misurazioni,indirizzi):
        
        #Quano il gateway ha le informazioni dei 4 device crea una connessione
        # TCP verso il server
        socketTCP = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
        indirizzoServer = ("localhost",8080)
        socketTCP.connect(indirizzoServer)
        
        # Si eseguono gli opportuni split dei dati per renderli più leggibili
        # poi vengono codificati per il trasferimento e inviati al server.
        for i in range(4):
            ora,minuti, temperatura, umidità = misurazioni[i].split('.')
            message = "Indirizzo IP: " +indirizzi[i][0] + "Porta: " + str(indirizzi[i][1]) + "- Ora: " + str(ora)+ ":" + str(minuti) + "- Temperatura: " + str(temperatura) + "- Umidità: " + str(umidità) + "\n"        
            socketTCP.send(message.encode())
           
        # Infine viene chiusa la socket TCP
        socketTCP.close()
           
        
            


    
