# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 11:20:39 2020

@author: carols1107
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z=mc.player.getTilePos()

mc.spawnEntity(x,y,z,63)
