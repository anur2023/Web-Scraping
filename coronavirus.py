import requests as r
from bs4 import BeautifulSoup
import re
import pandas as pd

url  = "https://www.worldometers.info/coronavirus/"

response = r.get(url)
# print(response)

soup = BeautifulSoup(response.text , 'html.parser')

main = soup.find('div',class_ = 'main_table_countries_div')

# print(main)

table = main.find('table')

# print(table)

header = table.find('thead')
# print(header)
headers = header.find_all('tr')
Title = []
for row in headers:
    title = row.text.strip().replace("\n", ",")
    Title.append([col.strip() for col in title.split(",") if col.strip() != ""]) 

Title = [item for sublist in Title for item in sublist]
Title=  Title[1:]
# print(Title_1D)
# print(Title)


Tbody = table.find('tbody')
# print(Tbody)

all_rows = Tbody.find_all('tr')

rows = []

for row in all_rows:
    row_data = []
    cells = row.find_all("td")
    for cell in cells:
        row_data.append(cell.text.strip())  
    rows.append(row_data)

# print(rows)
# print(Table_row)

data_frame = pd.DataFrame(rows,columns=Title)

# print(data_frame.head())

data_frame.to_csv('CoronaVirusData.csv',index=False)