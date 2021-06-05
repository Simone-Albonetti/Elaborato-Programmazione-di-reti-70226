# -*- coding: utf-8 -*-
"""
Created on Sat May 29 17:48:40 2021

@author: simon
"""

import time
import Device as dv

#Creo il secondo device, invio la prima misurazione e, passato 1 giorno, invierà
# una nuova misurazione 
dev2 = dv.Device("192.168.1.2", "10:AF:CB:EF:19:CF")
dev2.InviaMessaggio()

while True:
    time.sleep(86400)   #Per provare se funziona effettivamente ridurre il tempo di sleep
    dev2.InviaMessaggio()