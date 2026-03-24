from curl_cffi import requests
from bs4 import BeautifulSoup

word = "consciousness"
url = f"https://www.collinsdictionary.com/dictionary/english/{word}"
response = requests.get(url, impersonate="chrome120")
soup = BeautifulSoup(response.content, "html.parser", from_encoding="utf-8")

definition_elements = soup.find_all("div", class_="def")
if not definition_elements:
    definition_elements = soup.select(".content.definitions .sense .def")

print("Current (broken) extraction:")
for i, d in enumerate(definition_elements):
    print(f"{i+1}. {d.get_text(strip=True)}")

print("\nProposed fix (with separator=' '):")
for i, d in enumerate(definition_elements):
    # We can use separator=' ' to ensure spaces between tags
    # and then clean up double spaces if any.
    text = d.get_text(separator=" ", strip=True)
    # Clean up multiple spaces that might result from the separator
    import re
    text = re.sub(r'\s+', ' ', text)
    print(f"{i+1}. {text}")
