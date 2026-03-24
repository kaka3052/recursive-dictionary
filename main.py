import time
import os
import json
from watchdog.observers import Observer
from src.monitor import WordLinkEventHandler
from src.state import load_state, set_level

def load_config():
    if os.path.exists("config.json"):
        with open("config.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return {"root_file": "root.md"}

def main():
    config = load_config()
    root_file_path = config.get("root_file", "root.md")
    
    # Ensure absolute path
    root_file_path = os.path.abspath(root_file_path)
    root_dir = os.path.dirname(root_file_path)
    root_filename = os.path.basename(root_file_path)
    
    if not os.path.exists(root_dir):
        print(f"Error: Directory {root_dir} does not exist.")
        return

    # Load existing state
    state = load_state()
    
    # Ensure root file is Level 0
    if root_filename not in state:
        set_level(state, root_filename, 0)
    
    # Initialize the event handler and observer
    event_handler = WordLinkEventHandler(state, root_dir)
    observer = Observer()
    observer.schedule(event_handler, root_dir, recursive=False)
    
    # Start the observer
    print(f"Starting to watch directory: {root_dir}")
    print(f"Root file: {root_filename} (Level 0)")
    print("Press Ctrl+C to stop.")
    
    observer.start()
    
    # Process the root file on startup
    print(f"Scanning root file: {root_filename} for existing links...")
    event_handler.process_file(root_file_path)
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    
    observer.join()

if __name__ == "__main__":
    main()
