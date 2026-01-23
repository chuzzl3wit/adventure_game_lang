import adventure_game_lang as agl
test_value = {
"rooms": {
  "room1": {
    "desc": "cool room",
    "objects": ["table", "chair"],
    "exits": ["room2", "room8"]
  }
},
"objects": {}
}

def test_describe():
  assert "cool room" in agl.describe(test_value, "room1")