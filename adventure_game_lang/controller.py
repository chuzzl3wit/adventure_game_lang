from .actions import goto, pickup
from .describe import describe_obj


def controller(state, playerstate, action):
  playerstate["error_message"] = None
  playerstate["information_message"] = None

  try:
    if action.startswith("goto"):
      object = action.replace(action[0:5], "")
      goto(object, playerstate, state)
    elif action.startswith("pickup"):
      object = action.replace(action[0:7], "")
      pickup(state, playerstate, object, playerstate["currentRoom"])
    elif action == "inventory":
      if len(playerstate["objects"]) > 0:
        playerstate["information_message"] = ", ".join(playerstate["objects"])
      else:
        playerstate["information_message"] = "Empty"
    elif action.startswith("desc") and playerstate["is_term"]:
      object = action.replace(action[0:5], "")
      playerstate["information_message"] = describe_obj(object, state, playerstate)
    elif action == "h":
      playerstate["information_message"] = "pickup [object] - picks up object\ngoto [room] - goes to that room\ndesc [object] - describes that object\ninventory - shows inventory"
    else:
      raise KeyError("not a valid command")
  except Exception as e:
    playerstate["error_message"] = f"Error, please try again: {e}"