import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the Premier League table
url = "https://www.bbc.com/sport/football/premier-league/table"

# Send request
page = requests.get(url)

# Parse HTML
soup = BeautifulSoup(page.text, "html.parser")

# Find the table
table = soup.find("table")

# Extract headers
headers = []
for th in table.find_all("th"):
    headers.append(th.text.strip())

# Create DataFrame
league_table = pd.DataFrame(columns=headers)

# Extract rows
for tr in table.find_all("tr")[1:]:
    row_data = tr.find_all("td")
    row = [td.text.strip() for td in row_data]

    if len(row) == len(headers):   # ensure correct row length
        league_table.loc[len(league_table)] = row

# Print result
print(league_table)

