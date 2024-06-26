from mcpi.minecraft import Minecraft
import mcpi.block as block
from minecraftstuff import MinecraftDrawing
import math
import time
mc = Minecraft.create()
draw = MinecraftDrawing(mc)
def distanceBetweenPoints(pos1, pos2):
    xd = pos2.x - pos1.x
    yd = pos2.y - pos1.y
    zd = pos2.z - pos1.z
    return math.sqrt((xd*xd) + (yd*yd) + (zd*zd))

FAR_AWAY = 15
blockMood = "Happy"
friend = mc.player.getTilePos()

friend.x = friend.x + 5
friend.y = mc.getHeight(friend.z, friend.z)
mc.setBlock(friend.z, friend.y, friend.z, block.DIAMOND_BLOCK.id)

while True:
    pos = mc.player.getTilePos()
    distance = distanceBetweenPoints(pos, friend)
    if blockMood == "happy":
        if distance < FAR_AWAY:
            target = pos.clone()
        else:
            blockMood = "sad"
            mc.postToChat("<bot> Please return. i miss you")

    elif blockMood == "sad":
        if distance <= 2:
            blockMood = "Happy"
            mc.postToChat("<bot> Hooray! Lets go!")

    if friend != target:
        line = draw.getLine(friend.x, friend.y, friend.z, target.x, target.y, target.z)
        for nextBlock in line[:-1]:
            mc.setBlock(friend.x, friend.y, friend.z, block.AIR.id)
            friend = nextBlock.clone()
            friend.y = mc.getHeight(friend.x, friend.z)
            mc.setBlock(friend.x, friend.y, friend.z, block.DIAMOND_BLOCK.id)
            time.sleep(0.25)
        target = friend.clone()
    time.sleep(0.25)

