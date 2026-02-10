# Extract page title and first paragraph from Wikipedia

from bs4 import BeautifulSoup
import requests

url = "https://en.wikipedia.org/wiki/Data_science"

# Set a user-agent to avoid 403 errors
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/114.0.0.0 Safari/537.36",
}

response = requests.get(url, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

# Get page title
print("Title:", soup.title.string)

# Get first paragraph
content_div = soup.find("div", id="mw-content-text")
paragraphs = content_div.find_all("p", recursive=True)

for p in paragraphs:
    text = p.get_text(separator=" ", strip=True)
    if len(text) >= 50:
        print("\nFirst paragraph:\n", text)
        break