# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 11:07:08 2020

@author: carols1107
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z=mc.player.getTilePos()

mc.setSign(x,y,z,63,0,
           "我愛","python","","也愛minecraft")