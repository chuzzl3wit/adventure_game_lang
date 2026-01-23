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
    "objects": {},
    "win": {
      "room": "room1"
    }
  }
  return test_value

def test_checkwin(tset_value, playerstat):
  assert agl.check_win(tset_value, playerstat)

def test_checklose(tset_value, playerstat):
  tset_value["win"]["room"] = "room2"
  assert not agl.check_win(tset_value, playerstat)