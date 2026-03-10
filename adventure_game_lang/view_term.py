from .describe import describe
from colorist import red, bg_blue, Color, blue, bg_yellow, bg_green

def view_term(state, playerstate):
  print("")
  if playerstate["error_message"] is not None:
    red(playerstate["error_message"])
  if playerstate["information_message"] is not None:
    bg_blue(playerstate["information_message"])
  print(describe(state, playerstate["currentRoom"]))