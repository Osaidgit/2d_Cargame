#this is main file
import pygame as pg
from world import *
from node1 import *


node =Main()
run = True
while run:
	win.fill(blue)
	
	node.event()
	node.draw()
	node.update()
	
	clock.tick(fps)
	
pg.quit()
quit()

if '__name__' == '__main__':
	main()


