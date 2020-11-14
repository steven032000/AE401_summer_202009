# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 10:03:51 2020

@author: carols1107
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
     hits=mc.events.pollBlockHits()
     if len(hits)> 0:
         hit=hits[0]
         x, y, z=hit.pos
         block=mc.getBlock(x,y,z)
         
         mc.postToChat("恭喜你獵到了"+str(block))
    