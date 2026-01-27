import adventure_game_lang as agl
import pygame
from pygame.locals import *
import sys

if len(sys.argv) == 1:
  raise ValueError("no file inputed")
fileName = sys.argv[1]

with open(fileName) as f:
  code = f.read()

state = agl.parser(code)

playerstate = {
  "currentRoom": "room1",
  "objects": []
}

pygame.init()
screen = pygame.display.set_mode((640, 480))
running = True
fg = 250, 240, 230
errorColour = 255, 0, 0

while running:
    for event in pygame.event.get():
        if event.type == QUIT: 
            running = False
    
    agl.desc_win(state, screen, playerstate)
    pygame.display.update() 
    while not agl.check_win(state, playerstate):
      agl.describe(state, playerstate["currentRoom"], screen)
      pygame.display.update()
      action = input()
      screen.fill((0, 0, 0))
      font = pygame.font.SysFont(pygame.font.get_default_font(), 40)
      text = font.render(action, 0, fg)
      screen.blit(text, (0,440))
 
 
      try:
        if action.startswith("goto"):
          object = action.replace(action[0:5], "")
          agl.goto(object, playerstate, state)
        elif action.startswith("pickup"):
          object = action.replace(action[0:7], "")
          agl.pickup(state, playerstate, object, playerstate["currentRoom"])
        elif action == "inventory":
          print("\nInventory:\n")
          print(" ".join(playerstate["objects"]))
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
   