#In this file i stored all necessary functions and Classes
from decorators import *
import pygame as pg
pg.init()
res = width, height = 730, 1000
win = pg.display.set_mode(res)
white, black, red, green, blue, grey = (255, 255, 255), (0,0,0), (255, 0, 0), (144, 227, 84), (0,0, 255), (100, 133, 142)
clock = pg.time.Clock()
fps = 30
GO=pg.image.load("sprites/Gameover.jpg")
r_GO = pg.transform.scale(GO,(200,200))
#und = pg.mixer.Sound("music.wav")

#______________________________
img = pg.image.load("sprites/Lambo.png")
resize_img =pg.transform.scale(img, (50,100))
lambo = resize_img.get_rect()
@timer		
class Car:
	def __init__(self):
		self.rect = lambo
		self.rect.x,self.rect.y = 200,1000
	def draw(self):
		win.blit(resize_img,(self.rect.x, self.rect.y))
#--------------------------------
img1=pg.image.load("sprites/Left_button.png")
img2=pg.image.load("sprites/Right_button.png")
r_img1 = pg.transform.scale(img1,(100,100))
r_img2 = pg.transform.scale(img2,(100,100))
b_left = r_img1.get_rect()
b_right =r_img2.get_rect()
@timer
class Button:
	def __init__(self):
		self.rect1,self.rect2 = b_left,b_right
		self.rect1.x,self.rect1.y =20,1200
		self.rect2.x,self.rect2.y  = 600,1200
	def draw(self):
		win.blit(r_img1,(self.rect1.x,self.rect1.y))
		win.blit(r_img2,(self.rect2.x,self.rect2.y))
	def update(self):
		pass
#____________________________
opn_img = pg.image.load("sprites/red_car.png")
resize_opn = pg.transform.scale(opn_img,(50,100))
opn_rect = resize_opn.get_rect()
#######Traffic classes
@timer
class Red_Car:
	def __init__(self):
		self.rect = opn_rect
		self.rect.x = 100
		self.rect.y = 10		
	def draw(self):
		win.blit(resize_opn,(self.rect.x,self.rect.y))
#____________________________
opn_img2 = pg.image.load("sprites/blue_car.png")
resize_opn2 = pg.transform.scale(opn_img2,(50,100))
opn_rect2 = resize_opn2.get_rect()
@timer
class Green_Car:
	def __init__(self):
		self.rect = opn_rect2
		self.rect.x =200
		self.rect.y = 0
	def draw(self):
		win.blit(resize_opn2,(self.rect.x,self.rect.y))
#___________________________
opn_img3 = pg.image.load("sprites/green.png")
resize_opn3 = pg.transform.scale(opn_img3,(50,100))
opn_rect3 = resize_opn3.get_rect()
@timer
class Blue_Car:
	def __init__(self):
		self.rect = opn_rect3
		self.rect.x = 300
		self.rect.y = 0
	def draw(self):
		win.blit(resize_opn3,(self.rect.x,self.rect.y))

#___________________________
font = pg.font.Font(None, 50)
score = pg.image.load("sprites/Score.png")
score_img = pg.transform.scale(score, (100,50))
@timer
class Score:
	def __init__(self):
		self.img =score_img
		self.num= 0
		self.text2 = font.render(f'{self.num}',True,white)
	def draw(self):
		win.blit(self.img,(10,10))
		win.blit(self.text2,(120,10))
#--------------------------------

		


