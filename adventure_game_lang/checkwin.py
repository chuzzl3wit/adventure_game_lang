def check_win(state, playerstate):
  if "room" in state["win"]:
    if playerstate["currentRoom"] == state["win"]["room"]:
      return True
    else:
      return False
  elif "object" in state["win"]:
    if state["win"]["object"] in playerstate["objects"]:
      return True
    else:
      return False

def desc_win(state):
  if "room" in state["win"]:
    wintext = state["win"]["room"]
    return f"enter {wintext} to win"
  elif "object" in state["win"]:
    wintext = state["win"]["object"]
    return f"pickup {wintext} to win"
    