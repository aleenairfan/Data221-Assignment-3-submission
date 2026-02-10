# Extract eadings from Wikipedia and save to file

import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Data_science"

# Set a user-agent to avoid 403 errors
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/114.0.0.0 Safari/537.36",
}

response = requests.get(url, headers=headers)
response.raise_for_status()

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find the main content div
content_div = soup.find("div", id="mw-content-text")

headings = content_div.find_all("h2")

clean_headings = []

# Words to exclude
exclude_words = ["References", "External links", "See also", "Notes"]

for h in headings:

    text = h.get_text(separator=" ", strip=True)

    text = text.replace("[edit]", "").strip()

    if not any(word in text for word in exclude_words):
        clean_headings.append(text)

# Save headings to file
with open("headings.txt", "w", encoding="utf-8") as f:
    for heading in clean_headings:
        f.write(heading + "\n")

print("Headings saved to headings.txt")