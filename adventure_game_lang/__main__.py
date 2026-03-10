import adventure_game_lang as agl
from colorist import blue, bg_yellow
import sys

if len(sys.argv) == 1:
  raise ValueError("no file inputed")
fileName = sys.argv[1]

with open(fileName) as f:
  code = f.read()

state = agl.parser(code)

playerstate = {
  "currentRoom": "room1",
  "objects": [],
  "error_message": None,
  "information_message": None,
  "is_term": True,
}

blue(agl.desc_win(state))

while not agl.check_win(state, playerstate):
  agl.view_term(state, playerstate)
  action = input()
  agl.controller(state, playerstate, action)

bg_yellow("you win lol")

