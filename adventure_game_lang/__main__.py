import adventure_game_lang as agl
import pygame
from pygame.locals import *
import sys
import os

if len(sys.argv) == 1:
  raise ValueError("no file inputed")
fileName = sys.argv[1]

with open(fileName) as f:
  code = f.read()

gameState = agl.parser(code)

playerState = {
  "currentRoom": "room1",
  "objects": []
}

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption(fileName[0:len(fileName)-4])
running = True
fg = 250, 240, 230
errorColour = 255, 0, 0

fileDir = os.path.dirname(os.path.realpath(__file__))
fileDir = os.path.dirname(fileDir)
assetDir = fileDir+"/assets"

while running:
    for event in pygame.event.get():
        if event.type == QUIT: 
            running = False
    
    agl.desc_win(gameState, screen, playerState)
    pygame.display.update() 
    while not agl.check_win(gameState, playerState):
      agl.render_room(gameState, playerState["currentRoom"], screen, assetDir)
      agl.render_obj(gameState, playerState["currentRoom"], screen, assetDir)
      pygame.display.update()
      action = input()
      screen.fill((0, 0, 0))
      font = pygame.font.SysFont(pygame.font.get_default_font(), 40)
      text = font.render(action, 0, fg)
      screen.blit(text, (0,440))
      try:
        if action.startswith("goto"):
          object = action.replace(action[0:5], "")
          agl.goto(object, playerState, gameState)
        elif action.startswith("pickup"):
          object = action.replace(action[0:7], "")
          agl.pickup(gameState, playerState, object, playerState["currentRoom"])
        elif action == "inventory":
          fontI = pygame.font.SysFont(pygame.font.get_default_font(), 30)
          textI = fontI.render(" ".join(playerState["objects"]), 0, (0, 255, 255))
          screen.blit(textI, (0,0))
        else:
          raise KeyError("not a valid command")
      except Exception as e:
        fontErr = pygame.font.SysFont(pygame.font.get_default_font(), 30)
        textErr = fontErr.render(f"Error, please try again: {e}", 0, errorColour)
        screen.blit(textErr, (0,0))

    screen.fill((0, 0, 0))
    winFont = pygame.font.SysFont(pygame.font.get_default_font(), 100)
    winText = winFont.render("you win lol", 0, (255, 255, 0))
    screen.blit(winText, (135,180))


pygame.quit()
   