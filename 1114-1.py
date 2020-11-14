from mcpi.minecraft import Minecraft
mc=Minecraft.create()

while True:
    x,y,z=mc.player.getTilePos()
    mc.postToChat("你在x: "+str(x)+"y: "+str(y)+"z: "+str(z))
    i