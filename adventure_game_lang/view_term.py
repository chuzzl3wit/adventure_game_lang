from .describe import describe
from colorist import red, bg_blue, Color, blue, bg_yellow, bg_green
import pygame

def view_term(state, playerstate):
  print("")
  if playerstate["error_message"] is not None:
    red(playerstate["error_message"])
  if playerstate["information_message"] is not None:
    bg_blue(playerstate["information_message"])
  print(describe(state, playerstate["currentRoom"]))


  def view_pygame(state, playerstate):
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
      fontI = pygame.font.SysFont(pygame.font.get_default_font(), 30)
      textI = fontI.render(" ".join(playerState["objects"]), 0, (0, 255, 255))
      screen.blit(textI, (0,0))
      fontErr = pygame.font.SysFont(pygame.font.get_default_font(), 30)
      textErr = fontErr.render(f"Error, please try again: {e}", 0, (255, 0, 0))
      screen.blit(textErr, (0,0))

    screen.fill((0, 0, 0))
    winFont = pygame.font.SysFont(pygame.font.get_default_font(), 100)
    winText = winFont.render("you win lol", 0, (255, 255, 0))
    screen.blit(winText, (135,180))