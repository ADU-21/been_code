#coding: UTF-8
import os
import string
import pygame
from pygame.locals import *
from random import *
import pdb
from math import pi
#pygame初始化
pygame.init()
chars=string.ascii_letters + string.digits
code = sample(chars,4)
# randint()
i = 3
ftext = []
t = ''
for c in code:
	t += str(c)
	text = str(c).encode()
	sur = pygame.Surface((81,26))
	# font = pygame.font.SysFont('Arial', 18)
	font = pygame.font.Font('PFDinDisplayPro-Black.ttf',24)
	# pdb.set_trace()
	ftext.append(font.render(text, False, (randint(100,255), randint(100,255), randint(100,255)),(0, 0, 0)))
for f in ftext:
	f = pygame.transform.rotate(f, randint(-30,30))
	sur.blit(f,(i,1))
	i += 20
	# pdb.set_trace()
for i in range(3):
	pygame.draw.line(sur, (randint(0,255), randint(0,255), randint(0,255)),(randint(0,81), randint(0,26)), (randint(0,81), randint(0,26)),1) 
	pygame.draw.arc(sur, (randint(0,255), randint(0,255), randint(0,255)),(randint(0,40), randint(0,10),randint(45,81), randint(11,26)),randint(1,10)/randint(1,100), (randint(1,3)*pi)/randint(1,2), 1)

pygame.image.save(sur, "C:/Users/Administrator/Desktop/open.png")#图片保存地址
# pdb.set_trace()
print(t)