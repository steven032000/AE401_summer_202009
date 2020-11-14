# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 10:34:43 2020

@author: carols1107
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()

for i in range(20):
    mc.setBlock(x+i,y,z+i,1)
    
    mc.setBlocks(x+i,y-1,z+i,x+2+i,y-1,z+i,1)