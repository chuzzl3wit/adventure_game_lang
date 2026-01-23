#i cant write json lol
import json
value = {
"rooms": {
  "room1": {
    "desc": "cool room",
    "objects": ["table", "chair"],
    "exits": ["room2", "room8"]
  },
  "room2": {
    "desc": "empty room",
    "objects": ["spoon"],
    "exits": ["room9", "room1"]
  },
  "room8": {
    "desc": "other cool room",
    "objects": ["spoon"],
    "exits": ["room1"]
  }
},
"objects": {},
"win": {
  "object": "spoon"
}
}

print(json.dumps(value))