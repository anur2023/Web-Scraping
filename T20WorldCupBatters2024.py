import requests as r
from bs4 import BeautifulSoup
import re
import pandas as pd
url = 'https://www.espncricinfo.com/records/tournament/batting-most-runs-career/icc-men-s-t20-world-cup-2024-15946'

response = r.get(url)
# print(response)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find("div",class_="ds-overflow-x-auto ds-scrollbar-hide")
# print(table)

headers = table.find("tr")
# print(headers)

titles = []

for i in headers:
    title = i.text
    titles.append(title)


# print(titles)
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

df = pd.DataFrame(rows,columns=titles)
df.to_csv('T20WorldCupBattersData.csv',index=False)
