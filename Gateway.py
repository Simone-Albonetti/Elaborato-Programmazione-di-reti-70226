# -*- coding: utf-8 -*-
"""
Created on Sat May 29 12:14:23 2021

@author: simon
"""

import socket as sk

class Gateway:
    "Rappresenta il collegamento intermedio tra device e server"
    
    def __init__(self):
        #Quando creo il Gateway viene creata anche la socket UDP verso i device
        self.gatewayUDP = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
        self.gatewayUDP.bind(("localhost", 8100))
        
        gateway_mac = "05:10:0A:CB:24:EF"
        server = ("localhost", 8000)

        device1IP = "192.168.1.1" 
        device1Mac = "32:04:0A:EF:19:CF"
        device1 = None
        device2IP = "192.168.1.2" 
        device2Mac = "10:AF:CB:EF:19:CF"
        device2 = None
        device3IP = "192.168.1.3" 
        device3Mac = "AF:04:67:EF:19:DA"
        device3 = None
        device4IP = "192.168.1.4"
        device4Mac = "AF:04:67:EF:20:DA"
        device4 = None

        misurazioni = []
        indirizzi = []
        
       
        print("Gateway in funzione...")
        while (len(misurazioni) != 4):
            # Anche qui si è scelto come nel buffer della socket del server 
            # di utilizzare un buffer piccolo poichè vengono trasferiti pochi dati
            # alla volta e il rischi di riempire il buffer è molto basso
            
            data, address = self.gatewayUDP.recvfrom(4096)

            if(device1 == None):
                device1 = address
                print("Device 1 ha inviato i dati")

            elif(device2 == None):
                device2 = address
                print("Device 2 ha inviato i dati")
            elif(device3 == None):
                device3 = address
                print("Device 3 ha inviato i dati")
            else:
                device4 = address
                print("Device 4 ha inviato i dati")
                    
        
            print("Indirizzo: ", str(address))
            
            
            #Le misurazioni vengono inserite in un array
            misurazioni.append(data.decode('utf8'))
            
             #Gli indirizzi dei device vengono inseriti in un array
            indirizzi.append(address)


            arp_table_mac = {device1IP : device1Mac, device2IP : device2Mac, device3IP : device3Mac, device4IP : device4Mac}
            if (len(misurazioni) == 4):
                
                #Quando sia i 2 array (indirizzi e misurazioni) hanno ricevuto i dati
                # dai 4 device, il gateway invia al server le informazioni
                self.InviaMisurazioni(misurazioni, arp_table_mac)
                indirizzi = []
                misurazioni = []
    
    
    def InviaMisurazioni(self,misurazioni,indirizzi):
        
        #Quano il gateway ha le informazioni dei 4 device crea una connessione
        # TCP verso il server
        gatewayTCP = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
        indirizzoServer = ("localhost",8000)
        gatewayTCP.connect(indirizzoServer)
        
        
        IP = list(indirizzi)
        MAC = list(indirizzi.values())
        
        # Si eseguono gli opportuni split dei dati per renderli più leggibili
        # poi vengono codificati per il trasferimento e inviati al server.
        for i in range(4):
            ora,minuti, temperatura, umidità = misurazioni[i].split('.')
            
            message = "Indirizzo IP: " + str(IP[i]) + " Mac:  " + str(MAC[i]) +" - Ora: " + str(ora)+ ":" + str(minuti) + " - Temperatura: " + str(temperatura) + " - Umidità: " + str(umidità) + "\n"
            gatewayTCP.send(message.encode())
            
        # Infine viene chiusa la socket TCP
        gatewayTCP.close()
           
        
            


    
