from bs4 import BeautifulSoup
import requests
import sqlite3
lst = ['ASUS','HP','MSI','acer','Lenovo','DELL','APPLE']
print("select brand: ")
idx = 0
for i in range(len(lst)):
    print(i, lst[i])
idx = int(input())
url = f'https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&p%5B%5D=facets.brand%255B%255D%3D{lst[idx]}'
title_lst = []
specs_lst = []
price_lst = []
rating_lst = []
page = requests.get(url)
soup = BeautifulSoup(page.text,"html.parser")
title = soup.find_all("div", {"class": "_4rR01T"})
specs = soup.find_all("ul", {"class": "_1xgFaf"})
price = soup.find_all("div", {"class": "_30jeq3 _1_WHN1"})
rating = soup.find_all("div", {"class": "_3LWZlK"})
for t in title:
    print(t.text)
    title_lst.append(t.text)
for s in specs:
    xx = s.find_all("li", {"class": "rgWa7D"})
    sp = []
    for x in xx:
        sp.append(x.text)
    print(sp)
    specs_lst.append(sp)
    
for p in price:
    print(p.text)
    price_lst.append(p.text)

for r in rating:
    print(r.text)
    rating_lst.append(r.text)

try:
    sql3 = sqlite3.connect('sql.db')
    cursor = sql3.cursor()
    listOfTables = cursor.execute("""SELECT name FROM sqlite_master WHERE type='table' AND name='laptops'; """).fetchall()
     
    if listOfTables == []:
        cursor.execute("""create table laptops(id integer primary key AUTOINCREMENT, name text, price text, specs text, rating real);""")
    for i in range(len(title_lst)):
        if i >= len(rating_lst):
            rating = 0
        else:
            rating = rating_lst[i]
        query = 'insert into laptops(name,specs,price,rating) values(?,?,?,?);'
        params = (title_lst[i],str(specs_lst[i]),str(price_lst[i]),float(rating))
        cursor.execute(query,params)
        sql3.commit()
        print(cursor.fetchall())
    cursor.close()
except sqlite3.Error as err:
    print(err)
finally:
    if sql3:
        sql3.close()
        print("closed connection")

