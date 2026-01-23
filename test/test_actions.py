import adventure_game_lang as agl
import pytest

@pytest.fixture
def playerstat():
  return {
    "currentRoom": "room1",
    "objects": ["spoon"]
  }

@pytest.fixture
def tset_value():
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
  return test_value

def test_pickup(tset_value, playerstat):
  agl.pickup(tset_value, playerstat, "table", playerstat["currentRoom"])
  assert playerstat["objects"] == ["spoon", "table"]

def test_exits(tset_value, playerstat):
  agl.goto("room8", playerstat, tset_value)
  assert playerstat["currentRoom"] == "room8"