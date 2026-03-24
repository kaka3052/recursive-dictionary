from watchdog.events import FileSystemEventHandler
import os
import time
from .parser import extract_links
from .dictionary import fetch_word_info
from .generator import create_word_file
from .state import get_level, set_level, load_state

class WordLinkEventHandler(FileSystemEventHandler):
    """
    Handles file modification events and creates word files for new links.
    """
    def __init__(self, state, output_dir):
        self.state = state
        self.output_dir = os.path.abspath(output_dir)

    def on_modified(self, event):
        if not event.is_directory and event.src_path.endswith(".md"):
            # Only process if it's in our target directory
            if os.path.dirname(os.path.abspath(event.src_path)) == self.output_dir:
                time.sleep(0.5)
                self.process_file(event.src_path)

    def on_created(self, event):
        if not event.is_directory and event.src_path.endswith(".md"):
            if os.path.dirname(os.path.abspath(event.src_path)) == self.output_dir:
                time.sleep(0.5)
                self.process_file(event.src_path)

    def process_file(self, file_path):
        """
        Processes a file for links and creates word files for them.
        """
        filename = os.path.basename(file_path)
        
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Extract links
            words = extract_links(content)
            
            # Determine parent level
            parent_level = get_level(self.state, filename)
            target_level = parent_level + 1
            
            for word in words:
                word_filename = f"{word}.md"
                word_file_path = os.path.join(self.output_dir, word_filename)
                
                if not os.path.exists(word_file_path):
                    print(f"New word found: [[{word}]] in {filename}. Fetching info...")
                    ipa, definition = fetch_word_info(word)
                    
                    if ipa and definition:
                        if create_word_file(word, ipa, definition, target_level, self.output_dir):
                            set_level(self.state, word_filename, target_level)
                            print(f"Created {word_filename} at Level {target_level} in {self.output_dir}.")
                        else:
                            print(f"Failed to create {word_filename}.")
                    else:
                        print(f"Could not find info for word: {word}")
        
        except Exception as e:
            print(f"Error processing file {file_path}: {e}")
