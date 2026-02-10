import adventure_game_lang as agl
from colorist import red, bg_blue, Color, blue, bg_yellow
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

blue(agl.desc_win(state))

while not agl.check_win(state, playerstate):
  print(agl.describe(state, playerstate["currentRoom"]))
  print(f"\nEnter Command: {Color.BLUE}(h for help){Color.OFF}")
  action = input()

  try:
    if action.startswith("goto"):
      object = action.replace(action[0:5], "")
      agl.goto(object, playerstate, state)
    elif action.startswith("pickup"):
      object = action.replace(action[0:7], "")
      agl.pickup(state, playerstate, object, playerstate["currentRoom"])
    elif action == "inventory":
      print(" ")
      bg_blue(", ".join(playerstate["objects"]))
    elif action.startswith("desc"):
      object = action.replace(action[0:5], "")
      bg_blue(agl.describe_obj(object, state, playerstate))
    else:
      raise KeyError("not a valid command")
  except Exception as e:
    red(f"\nError, please try again: {e}")

bg_yellow("you win lol")


   