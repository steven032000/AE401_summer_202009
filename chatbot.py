from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()

try:
    blockId = int(input('請問你想放什麼方塊ID呢'))
    mc.setBlock(x,y,z,blockId)

except:
     mc.postToChat("輸入數字")
