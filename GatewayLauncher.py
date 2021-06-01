# -*- coding: utf-8 -*-
"""
Created on Sat May 29 21:42:23 2021

@author: simon
"""

import Gateway as gt

#Creo il gateway e si mette in ascolto sulla socket UDP verso i device
gateway = gt.Gateway('192.168.1.92', 10000)
