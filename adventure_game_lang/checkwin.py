import pygame

def check_win(state, playerstate):
  if "room" in state["win"]:
    if playerstate["currentRoom"] == state["win"]["room"]:
      return True
    else:
      return False
  elif "object" in state["win"]:
    if state["win"]["object"] in playerstate["objects"]:
      return True
    else:
      return False

def desc_win(state, screen, playerstate):
  if check_win(state, playerstate) == False:
    if "room" in state["win"]:
      wintext = state["win"]["room"]
      font = pygame.font.SysFont(pygame.font.get_default_font(), 30)
      text = font.render(f"enter {wintext} to win", 0, (250, 240, 230))
      screen.blit(text, (0,0))
    elif "object" in state["win"]:
      wintext = state["win"]["object"]
      font = pygame.font.SysFont(pygame.font.get_default_font(), 30)
      text = font.render(f"pickup {wintext} to win", 0, (250, 240, 230))
      screen.blit(text, (0,0))
    