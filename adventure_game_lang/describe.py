import pygame
from pygame.locals import *

def describe(code: dict, room: str, screen):
  desc= code["rooms"][room]["desc"]
  exit: list = list(code["rooms"][room]["exits"]) 
  font = pygame.font.SysFont(pygame.font.get_default_font(), 40)
  ren = font.render("Exits:", 0, (250, 240, 230))
  screen.blit(ren, (0,30))
  for i, x in enumerate(exit):
    ren = font.render(x, 0, (250, 240, 230))
    calc = 40*i
    calc=calc+70
    screen.blit(ren, (0,calc))

