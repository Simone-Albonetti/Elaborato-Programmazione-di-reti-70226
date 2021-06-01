# -*- coding: utf-8 -*-
"""
Created on Sat May 29 21:15:40 2021

@author: simon
"""

import socket as sk

class Server:
    "Rappresenta il server che visualizza le misurazioni, ricevute dal gateway"
    
    socketTCP = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
    indirizzoServer = ('localhost', 8080)
    socketTCP.bind(indirizzoServer)
    socketTCP.listen(1)
    print(indirizzoServer)
        
    while True:
        #Il server entra in funzione e si mette in ascolto
        print('Server in funzione...')
        
        #Quando riceve richiesta di connessione crea la socket per il trasferimento
        socketTrasferimento, indirizzoSocketTrasferimento = socketTCP.accept()          
        try:
            #Il buffer di trasferimento è di 1024 byte. E' più che sufficiente
            # poichè i dati trasferiti sono relativamente pochi e quindi il 
            # rischio di riempire il buffer è molto basso
            messaggio = socketTrasferimento.recv(1024)
            print(messaggio.decode())
        except:
            print("Qualcosa è andato storto nella decodifica")
            
        #Una volta ricevuti i messaggi e mostrati a video viene chiusa la socket
        # di trasferimento
        socketTrasferimento.close()
        