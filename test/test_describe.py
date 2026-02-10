import adventure_game_lang as agl
test_value = {
"rooms": {
  "room1": {
    "desc": "cool room",
    "objects": ["table", "spoon"],
    "exits": ["room2", "room8"]
  }
},
"objects": {
  "spoon": {
    "desc": "a silver spoon"
  },
}
}

playerstate = {
  "currentRoom": "room1",
  "objects": []
}

def test_describe():
  assert "cool room" in agl.describe(test_value, "room1")

def test_descObj():
  assert "a silver spoon" in agl.describe_obj("spoon", test_value, playerstate)