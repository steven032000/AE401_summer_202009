from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()

length=20
width=20
height=10

block=57
air=0
lamp=91

# 外框
mc.setBlocks(x,y,z,x+length,y+height,z+width,block)
mc.setBlocks(x+1,y+1,z+1,x+length-1,y+height-1,z+width-1,air)

#天花板燈
mc.setBlocks(x,y+height,z,x+length,y+height,z+width,lamp)


mc.setBlocks(x+1,y+(height/2),z+1,x+length-1,y+(height/2),z+width-1,lamp)
mc.setBlocks(x+2,y+(height/2),z+2,x+length-2,y+(height/2),z+width-2,air)

mc.setBlocks(x+3,y+1,z,x+6,y+(height/2),y+3,z,air)