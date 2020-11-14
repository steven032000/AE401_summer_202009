# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 11:29:47 2020

@author: carols1107
"""
from mcpi.minecraft import Minecraft

import random
import time

mc = Minecraft.create()

x,y,z=mc.player.getTilePos()

while True:
    y = y+30
    x = x+random.uniform(-20,20)
    z = z+random.uniform(-20,20)

    mc.spawnEntity(x,y,z,53)
                 
    
    time.sleep(0.01)

