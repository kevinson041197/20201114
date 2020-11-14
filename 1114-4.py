from mcpi.minecraft import Minecraft
mc=Minecraft.create()

x,y,z=mc.player.getTilePos()
mc.setBlocks(x+10,y,z+10,x-10,y,z-10,46,25)