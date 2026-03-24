from src.dictionary import fetch_word_info
from src.generator import create_word_file
import os

ipa, definition = fetch_word_info("knowledge")
create_word_file("knowledge_test", ipa, definition, 1, "notes")
print("Generated notes/knowledge_test.md")
