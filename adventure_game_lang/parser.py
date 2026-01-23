import json

def parser(json_str: str) -> dict: 
  parsed = json.loads(json_str)
  for key in parsed.keys():
    if key == "rooms":
      continue
    elif key == "objects":
      continue
    elif key == "win":
      continue
    else:
      raise SyntaxError(f"Invalid key in root, found {key}, should be either 'rooms' or 'objects'")
  return parsed


