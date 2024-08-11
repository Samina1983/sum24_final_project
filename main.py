import mysql.connector
import requests
from bs4 import BeautifulSoup
import itertools

mydb = mysql.connector.connect(
  host="localhost",
  user="samina",
  password="1234",
  database="mydatabase"
)
cursor = mydb.cursor()


cursor.execute("CREATE TABLE c_details (country VARCHAR(255), capital VARCHAR(255))")

URL = "https://www.scrapethissite.com/pages/simple/"

page = requests.get(URL)

results = BeautifulSoup(page.content, "html.parser")

countries = results.find_all("h3", class_="country-name")

capitals = results.find_all("span", class_="country-capital")

for (currCount, currCapt) in zip(countries, capitals):
    cuc = currCount.text.strip()
    cac = currCapt.text.strip()
    sql = "INSERT INTO c_details (country, capital) VALUES (%s, %s)"
    val = (cuc, cac)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record inserted.")
