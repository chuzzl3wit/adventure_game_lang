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
screen = pygame.display.set_mode((500, 500))
running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT: 
            running = False
    
    print(agl.desc_win(state))
    screen.fill((0,0,0))
    while not agl.check_win(state, playerstate):
      print(agl.describe(state, playerstate["currentRoom"]))
      action = input()
      my_font = pygame.font.SysFont('Comic Sans MS', 30)
      text_surface = my_font.render("bosh", False, (0, 0, 0))
      screen.blit(text_surface, (0,0))

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
        print(f"\nError, please try again: {e}")

    print("you win lol")
    pygame.quit()

pygame.quit()
   