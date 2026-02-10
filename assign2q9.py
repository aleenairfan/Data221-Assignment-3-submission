# Extract first table from Wikipedia and save as CSV

import requests
from bs4 import BeautifulSoup
import csv

url = "https://en.wikipedia.org/wiki/Machine_learning"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

# Get the main content
content_div = soup.find("div", id="mw-content-text")
tables = content_div.find_all("table")

table_data = []

# Find the first table with at least 3 data rows
for table in tables:
    rows = table.find_all("tr")
    if len(rows) >= 3:
        for row in rows:
            cells = row.find_all(["th", "td"])
            row_data = [cell.get_text(" ", strip=True) for cell in cells]
            if row_data:
                table_data.append(row_data)
        break  # stop after first suitable table

if not table_data:
    print("No suitable table found")
else:
    # Determine max columns
    max_cols = max(len(row) for row in table_data)

    for row in table_data:
        while len(row) < max_cols:
            row.append("")

    headers = [f"col{i+1}" for i in range(max_cols)]

    # Save to CSV
    with open("wiki_table.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(table_data)

    print("Table saved to wiki_table.csv with headers")
