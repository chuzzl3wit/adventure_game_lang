#i cant write json lol
import json
value = {
"rooms": {
  "room1": {
    "image": "room1.png",
    "objects": ["table", "chair"],
    "exits": ["room2", "room8"]
  },
  "room2": {
    "image": "room2.png",
    "objects": [],
    "exits": ["room9", "room1"]
  },
  "room8": {
    "image": "room8.png",
    "objects": ["spoon"],
    "exits": ["room1"]
  },
    "room9": {
    "image": "test_lowkey.png",
    "objects": [],
    "exits": ["room2", "room1"]
  }
},
"objects": {
  "table": {
    "image": "table.png",
    "x": 100,
    "y": 200
  },
  "chair": {
    "image": "chair.png",
    "x": 0,
    "y": 0
  },
  "spoon": {
    "image": "spoon.png",
    "x": 224,
    "y": 256
  }
},
"win": {
  "object": "table"
}
}

print(json.dumps(value))