# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 11:53:08 2020

@author: carols1107
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
     hits = mc.events.pollProjectileHits()
     if len(hits)> 0:
         hit= hits[0]
         x, y, z=hit.pos
        
         
         mc.createExplosion(x,y,z,  100)
    