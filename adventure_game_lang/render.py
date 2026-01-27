import pygame
from pygame.locals import *

def render_room(code: dict, room: str, screen, dir):
  image= code["rooms"][room]["image"]
  exit: list = list(code["rooms"][room]["exits"]) 
  font = pygame.font.SysFont(pygame.font.get_default_font(), 40)
  ren = font.render("Exits:", 0, (250, 240, 230))
  screen.blit(ren, (0,30))
  for i, x in enumerate(exit):
    ren = font.render(x, 0, (250, 240, 230))
    calc = 40*i
    calc=calc+70
    screen.blit(ren, (0,calc))
  image = pygame.image.load(dir+"/"+image).convert()
  screen.blit(image, (97, 36))

def render_obj(code, room, screen, dir):
  objects = code["rooms"][room]["objects"]
  for i, x in enumerate(objects):
    imgfile= code["objects"][objects[i]]["image"]
    x: int = code["objects"][objects[i]]["x"]
    y: int = code["objects"][objects[i]]["y"]
    image = pygame.image.load(dir+"/"+imgfile)
    screen.blit(image, (x+97, y+36))



