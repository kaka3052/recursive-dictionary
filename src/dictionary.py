from curl_cffi import requests
from bs4 import BeautifulSoup
import re

def fetch_word_info(word):
    """
    Fetches the Collins definition and IPA for a given word.
    """
    url = f"https://www.collinsdictionary.com/dictionary/english/{word.lower().replace(' ', '-')}"
    
    try:
        # Use impersonate to mimic a real browser's TLS fingerprint
        response = requests.get(url, impersonate="chrome120")
        
        if response.status_code != 200:
            return None, None

        # Ensure we use the correct encoding, Collins usually uses utf-8
        soup = BeautifulSoup(response.content, "html.parser", from_encoding="utf-8")

        # Extract IPA - Collins often uses class 'pron'
        ipa = "N/A"
        ipa_element = soup.find("span", class_="pron")
        if not ipa_element:
            ipa_element = soup.find("span", class_="ipa")
        
        if ipa_element:
            # Only remove elements that are definitely not part of the pronunciation (like sound icons)
            for extra in ipa_element.find_all(["a", "span"], class_=["ptr", "hwd_sound", "audio_play_button"]):
                extra.decompose()
            ipa = ipa_element.get_text(strip=True)

        # Extract Collins Definition
        # Definitions are usually in divs with class 'def'
        # We'll try a few common selectors for Collins
        definition_elements = soup.find_all("div", class_="def")
        if not definition_elements:
            # Fallback for different page structures
            definition_elements = soup.select(".content.definitions .sense .def")

        definitions = []
        for d in definition_elements:
            # Use space separator to avoid merging words from nested tags
            text = d.get_text(separator=" ", strip=True)
            # Clean up multiple spaces
            text = re.sub(r'\s+', ' ', text)
            # Optional: Clean up spaces before punctuation (e.g., "word ." -> "word.")
            text = re.sub(r'\s+([,.!?;:])', r'\1', text)
            definitions.append(text)
        
        # Format definitions into a string
        if definitions:
            formatted_definition = "\n".join([f"{i+1}. {defn}" for i, defn in enumerate(definitions)])
        else:
            formatted_definition = "No definition found in Collins."

        return ipa, formatted_definition

    except Exception as e:
        print(f"Error fetching info for {word}: {e}")
        return None, None
