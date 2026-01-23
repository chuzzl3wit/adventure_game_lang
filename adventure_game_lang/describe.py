def describe(code: dict, room: str):
  desc= code["rooms"][room]["desc"]
  obj: list = code["rooms"][room]["objects"]
  exit: list = code["rooms"][room]["exits"]
  objOut = "\n".join(obj)
  exitOut = "\n".join(exit)
  return f"\n{desc}\n\nObjects:\n{objOut}\n\nExits:\n{exitOut}"

