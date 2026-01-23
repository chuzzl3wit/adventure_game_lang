import adventure_game_lang as agl
import json
import pytest

def test_parser():
  test_value = {
  "rooms": {},
  "objects": {}
  }
  json_str = json.dumps(test_value)
  assert agl.parser(json_str) == test_value

def parse():
  test_value = {
  "rooms": {},
  "objects": {},
  "poopoo": {}
  }

  json_str = json.dumps(test_value)
  test = agl.parser(json_str)

def test_exeption():
  with pytest.raises(SyntaxError, match="Invalid key in root, found poopoo, should be either 'rooms' or 'objects'"):
    parse()