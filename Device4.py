# -*- coding: utf-8 -*-
"""
Created on Sat May 29 17:49:22 2021

@author: simon
"""

import time
import Device as dv

#Creo il quarto device, invio la prima misurazione e, passato 1 giorno, invierà
# una nuova misurazione 
dev4 = dv.Device('192.168.1.92', 10000)
dev4.InviaMessaggio()

while True:
    time.sleep(86400) #Per provare se funziona effettivamente ridurre il tempo di sleep
    dev4.InviaMessaggio()