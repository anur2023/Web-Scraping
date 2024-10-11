import requests as r
from bs4 import BeautifulSoup
import re
import pandas as pd
url = "https://www.cricbuzz.com/live-cricket-scorecard/100220/ind-vs-ban-1st-test-bangladesh-tour-of-india-2024"
response = r.get(url)
# print(response)

soup = BeautifulSoup(response.text, 'html.parser')

Header = soup.find('div',class_='cb-col cb-col-100 cb-scrd-hdr-rw')
# print(Header.text)

player_name = soup.find_all('a','cb-text-link')
# cb-text-link
PlayersName= []
for i in player_name:
    PlayersName.append(i.text)

# print(len(PlayersName))

Wicket_Reason = []

wicket = soup.find_all('span','text-gray')

for i in wicket:
    Wicket_Reason.append(i.text)

# print(len(Wicket_Reason))

Runs = []
run = soup.find_all('div','cb-col cb-col-8 text-right text-bold')

for i in run:
    Runs.append(i.text)

# print(len(Runs))

ball = soup.find_all('div',class_='cb-col cb-col-8 text-right')
Balls = []
for i in ball:
    Balls.append(i.text)

# print(len(Balls))

table = soup.find_all('div',class_='cb-col cb-col-100 cb-scrd-itms')
Table = []
for i in table:
    Table.append(i.text)

# print(Table)

def extract_info(entry):
    pattern = r"([A-Za-z\s\(\)]+)\s+c\s+([A-Za-z\s]+)\s+b\s+([A-Za-z\s]+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+([\d\.]+)"
    match = re.match(pattern, entry.strip())
    if match:
        return match.groups()
    return None

parsed_data = [extract_info(entry) for entry in Table if extract_info(entry) is not None]

columns = ['Player Name', 'Caught By', 'Bowler', 'Runs', 'Balls', 'Sixes', 'Fours', 'Strike Rate']
df = pd.DataFrame(parsed_data, columns=columns)

df.to_csv("Test_cricket_data.csv", index=False)

print("Data saved to 'cricket_data.csv'.")


