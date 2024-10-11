import requests as r
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.espncricinfo.com/records/tournament/bowling-most-wickets-career/icc-men-s-t20-world-cup-2024-15946"

response = r.get(url)
# print(response)

soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('div',class_="ds-overflow-x-auto ds-scrollbar-hide")
# print(table)
headers = table.find('tr')
Title = []
for i in headers:
    tit = i.text
    Title.append(tit)

# print(Title)

rows = []
all_rows = table.find_all("tr")
for row in all_rows:
    row_data = []
    cells = row.find_all("td")
    for cell in cells:
        row_data.append(cell.text.strip())  
    rows.append(row_data)
rows = rows[1:]
# print((rows))

df = pd.DataFrame(rows,columns=Title)
df.to_csv("T20WorldCupBollersData.csv",index=False)