from curl_cffi import requests
from bs4 import BeautifulSoup
import re

url = "https://www.collinsdictionary.com/dictionary/english/knowledge"
resp = requests.get(url, impersonate="chrome120")
soup = BeautifulSoup(resp.content, "html.parser")

definition_elements = soup.find_all("div", class_="def")
if not definition_elements:
    definition_elements = soup.select(".content.definitions .sense .def")

for i, d in enumerate(definition_elements):
    text = d.get_text(separator=" ", strip=True)
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\s+([,.!?;:])', r'\1', text)
    if "awareness" in text:
        print(f"{i+1}. {text}")
        print(f"RAW: {d}")
