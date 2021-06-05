# -*- coding: utf-8 -*-
"""
Created on Sat May 29 17:47:52 2021

@author: simon
"""

import time
import Device as dv

#Creo il primo device, invio la prima misurazione e, passato 1 giorno, invierà
# una nuova misurazione 
dev1 = dv.Device("192.168.1.1", "32:04:0A:EF:19:CF")
dev1.InviaMessaggio()

while True:
    time.sleep(86400) #Per provare se funziona effettivamente ridurre il tempo di sleep
    dev1.InviaMessaggio()
