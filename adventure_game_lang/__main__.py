import adventure_game_lang as agl
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

print(agl.desc_win(state))

while not agl.check_win(state, playerstate):
  print(agl.describe(state, playerstate["currentRoom"]))
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
      print(" ".join(playerstate["objects"]))
    else:
      raise KeyError("not a valid command")
  except Exception as e:
    print(f"\nError, please try again: {e}")

print("you win lol")


   