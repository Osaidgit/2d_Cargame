#this is Controller file or Main Class
import random as ran
import pygame as pg
from world import*
@timer
class Main:
	def __init__(self):
		self.car = Car()
		self.button = Button()
		self.tcar1 = Red_Car()
		self.tcar2 = Green_Car()
		self.tcar3 = Blue_Car()
		self.score = Score()
		#self.sound = sound
#___________________________
		self.click= False
		self.left =False
		self.right = False
		self.move =True
		self.game = False
	def event(self):
		self.score.num +=1
		self.pos = pg.mouse.get_pos()
		for i in pg.event.get():
			if i.type == pg.QUIT:
				 run = False
		
			if i.type == pg.MOUSEBUTTONDOWN:
				not self.click
			if self.button.rect1.collidepoint(self.pos):
				print("left")
				self.left = True
				self.right = False
			if self.button.rect2.collidepoint(self.pos):
				print("right")
				self.right = True
				self.left = False
			
				
			
	def draw(self):
		pg.draw.rect(win,black,(10, 10, width-30, 1400))
		self.car.draw()		
		self.tcar1.draw()
		self.tcar2.draw()
		self.tcar3.draw()
		self.button.draw()
		self.score.draw()
	def update(self):
		if self.left:
			self.car.rect.x -= 5
		if self.car.rect.x <= 10:
			self.car.rect.x = 10
		if self.right:
			self.car.rect.x +=5
		if self.car.rect.x >= 650:
			self.car.rect.x = 650
			
		if self.move:
			#self.sound.play()
			self.tcar1.rect.y +=10
			self.tcar2.rect.y += 10
			self.tcar3.rect.y += 10
		if self.tcar1.rect.y ==1400:
			self.tcar1.rect.y = ran.choice([0,-500])
			self.tcar1.rect.x = ran.choice([400,50,100,630])
			
		if self.tcar2.rect.y ==1400:
			self.tcar2.rect.y = ran.choice([-100,-300])
			self.tcar2.rect.x = ran.choice([250,50,350])
			
		if self.tcar3.rect.y ==1400:
			self.tcar3.rect.y = 0
			self.tcar3.rect.x = ran.choice([50,100,350, 630])
			

		
		if self.car.rect.colliderect(self.tcar1.rect) or self.car.rect.colliderect(self.tcar2.rect) or self.car.rect.colliderect(self.tcar3.rect):
			self.move = False
			self.game = True
		
		if self.game:
			win.blit(r_GO, (200,500))
		pg.display.flip()	
		pg.display.update()
