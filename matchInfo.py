import requests as r
from bs4 import BeautifulSoup

url = "https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2024-1411166/match-schedule-fixtures-and-results"

response = r.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# print(response)

Main_Body = soup.find('div','ds-mb-4')
# print(Main_Body)

Content_Box = Main_Body.find_all('div')

# print(Content_Box)

