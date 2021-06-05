# -*- coding: utf-8 -*-
"""
Created on Sat May 29 21:15:40 2021

@author: simon
"""

import socket as sk

class Server:
    "Rappresenta il server che visualizza le misurazioni, ricevute dal gateway"
    
    serverTCP = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
    indirizzoServer = ('', 8000)
    serverTCP.bind(indirizzoServer)
    
    server_ip = "10.10.10.1"
    server_mac = "00:00:0A:BB:28:FC"
    gateway_mac = "05:10:0A:CB:24:EF"
    serverTCP.listen(1)
    

    while True:
        #Il server entra in funzione e si mette in ascolto
        print('Server in funzione...')
        
        #Quando riceve richiesta di connessione crea la socket per il trasferimento
        socketTrasferimento, indirizzoSocketTrasferimento = serverTCP.accept()          
        try:
            #Il buffer di trasferimento è di 1024 byte. E' più che sufficiente
            # poichè i dati trasferiti sono relativamente pochi e quindi il 
            # rischio di riempire il buffer è molto basso
            messaggio = socketTrasferimento.recv(4096)
            print("Indirizzo socketTrasferimento" + str(indirizzoSocketTrasferimento))
            print(messaggio.decode())
        except:
            print("Qualcosa è andato storto nella decodifica")
            
        #Una volta ricevuti i messaggi e mostrati a video viene chiusa la socket
        # di trasferimento
        socketTrasferimento.close()
  