from .describe import describe
from .render import render_obj, render_room
from colorist import red, bg_blue, Color, blue, bg_yellow, bg_green
import pygame
import os

def view_term(state, playerstate):
  print("")
  if playerstate["error_message"] is not None:
    red(playerstate["error_message"])
  if playerstate["information_message"] is not None:
    bg_blue(playerstate["information_message"])
  print(describe(state, playerstate["currentRoom"]))



fileDir = os.path.dirname(os.path.realpath(__file__))
fileDir = os.path.dirname(fileDir)
assetDir = fileDir+"/assets"

def view_pygame(gameState, playerState, action, screen):
   screen.fill((0, 0, 0))
   if playerState["error_message"] is not None:
      error = playerState["error_message"]
      fontErr = pygame.font.SysFont(pygame.font.get_default_font(), 30)
      textErr = fontErr.render(f"Error, please try again: {error}", 0, (255, 0, 0))
      screen.blit(textErr, (0,0))
   render_room(gameState, playerState["currentRoom"], screen, assetDir)
   render_obj(gameState, playerState["currentRoom"], screen, assetDir)
   font = pygame.font.SysFont(pygame.font.get_default_font(), 40)
   text = font.render(action, 0, (250, 240, 230))
   screen.blit(text, (0,440))
   if playerState["information_message"] is not None:
    fontI = pygame.font.SysFont(pygame.font.get_default_font(), 30)
    textI = fontI.render(" ".join(playerState["objects"]), 0, (0, 255, 255))
    screen.blit(textI, (0,0))
    pygame.display.update()

  


