import adventure_game_lang as agl
from colorist import blue, bg_yellow
import pygame
import sys
import os

if len(sys.argv) == 1:
  raise ValueError("no file inputed")
fileName = sys.argv[1]

if sys.argv[2] == "1":
  graphical = False
elif sys.argv[2] == "2":
  graphical = True
else:
  raise ValueError(f"unrecognised option ")

with open(fileName) as f:
  code = f.read()

state = agl.parser(code)

playerstate = {
  "currentRoom": "room1",
  "objects": [],
  "error_message": None,
  "information_message": agl.desc_win(state),
  "is_term": True,
}

if graphical:
  pygame.init()
  screen = pygame.display.set_mode((640, 480))
  pygame.display.set_caption(fileName[0:len(fileName)-4])
  running = True
  fg = 250, 240, 230
  errorColour = 255, 0, 0



#blue(agl.desc_win(state))

while not agl.check_win(state, playerstate):
  action = input()
  if not graphical:
    agl.view_term(state, playerstate)
  else:
    agl.view_pygame(state, playerstate, action, screen)
  agl.controller(state, playerstate, action)

if graphical:
  screen.fill((0, 0, 0))
  winFont = pygame.font.SysFont(pygame.font.get_default_font(), 100)
  winText = winFont.render("you win lol", 0, (255, 255, 0))
  screen.blit(winText, (135,180))
else:
  bg_yellow("you win lol")

