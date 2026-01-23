
def pickup(state, inventory, objecT, room):
  if objecT in state["rooms"][room]["objects"]:
    index: int = state["rooms"][room]["objects"].index(objecT)
    del state["rooms"][room]["objects"][index] 
    inventory["objects"].append(objecT)
  else:
    raise KeyError(f"{objecT} does not exist in {room}")
  
def goto(room, playerstate, state):
  cRoom = playerstate["currentRoom"]
  if room in state["rooms"][cRoom]["exits"]:
    playerstate["currentRoom"] = room
  else:
    raise KeyError(f"cant exit to {room} from {cRoom}")