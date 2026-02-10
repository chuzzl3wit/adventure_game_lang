from colorist import style_text, Effect

def describe(code: dict, room: str):
  desc= code["rooms"][room]["desc"]
  obj: list = code["rooms"][room]["objects"]
  exit: list = code["rooms"][room]["exits"]
  objOut = "\n".join(obj)
  exitOut = "\n".join(exit)
  objText = style_text("Objects:", Effect.BOLD)
  exitText = style_text("Exits:", Effect.BOLD)
  return f"\n{desc}\n\n{objText}\n{objOut}\n\n{exitText}\n{exitOut}"

def describe_obj(obj, state, playerstate):
  currentRoom =playerstate["currentRoom"]
  if obj in state["rooms"][currentRoom]["objects"]:
    return state["objects"][obj]["desc"]
  else:
    raise KeyError(f"{obj} does not exist in {currentRoom}")


