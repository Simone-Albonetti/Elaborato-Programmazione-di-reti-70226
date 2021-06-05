# -*- coding: utf-8 -*-
"""
Created on Sat May 29 17:49:08 2021

@author: simon
"""

import time
import Device as dv

#Creo il terzo device, invio la prima misurazione e, passato 1 giorno, invierà
# una nuova misurazione 
dev3 = dv.Device()
dev3.InviaMessaggio()

while True:
     #86400 sono i secondi in un giorno. In questo modo una volta al giorno il device
    # invia le misurazioni al gateway
    time.sleep(86400)   #Per provare se funziona effettivamente ridurre il tempo di sleep
    dev3.InviaMessaggio()