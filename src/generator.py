import os

def create_word_file(word, ipa, definition, level, output_dir):
    """
    Creates a new Markdown file for a word with the specified content.
    """
    filename = f"{word}.md"
    file_path = os.path.join(output_dir, filename)
    if os.path.exists(file_path):
        # File already exists
        return False
    
    content = f"# {word}\n\n"
    content += f"**IPA**: /{ipa}/\n"
    content += f"**Level**: Level {level}\n\n"
    content += "### Collins Definition\n"
    content += f"{definition}\n"
    
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"Error writing to file {file_path}: {e}")
        return False
