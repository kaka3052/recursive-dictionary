import json
import os

STATE_FILE = "levels.json"

def load_state():
    """
    Loads the levels from levels.json.
    """
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading state: {e}")
            return {}
    return {}

def save_state(state):
    """
    Saves the state to levels.json.
    """
    try:
        with open(STATE_FILE, "w", encoding="utf-8") as f:
            json.dump(state, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error saving state: {e}")

def get_level(state, filename):
    """
    Returns the level of a given filename.
    Defaults to 0 if not found.
    """
    return state.get(filename, 0)

def set_level(state, filename, level):
    """
    Sets the level for a given filename and saves the state.
    """
    state[filename] = level
    save_state(state)
