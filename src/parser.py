import re

def extract_links(content):
    """
    Extracts words within [[ ]] from the content.
    Returns a set of unique words found.
    """
    # Pattern to match [[word]] or [[word|alias]]
    pattern = r"\[\[(.*?)\]\]"
    matches = re.findall(pattern, content)
    
    words = set()
    for match in matches:
        # Handle cases like [[word|alias]]
        if "|" in match:
            word = match.split("|")[0].strip()
        else:
            word = match.strip()
        
        if word:
            words.add(word)
    
    return words
