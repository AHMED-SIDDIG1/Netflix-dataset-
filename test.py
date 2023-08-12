#import libraries we need 
import sqlite3
import pandas as pd

# make a connectin point and create sqlite file
conn=sqlite3.connect("netflix22.sqlite")
cur=conn.cursor()

# we drop if there's any Tabels that has the same name
cur.execute('''DROP TABLE IF EXISTS FILM ''')
cur.execute('''DROP TABLE IF EXISTS SERIES''')
cur.execute('''DROP TABLE IF EXISTS DIRECTORY''')
cur.execute('''DROP TABLE IF EXISTS COUNTRY''')

# we create our tabels and it's columns
cur.execute('''CREATE TABLE IF NOT EXISTS FILM
            (id INTEGER PRIMARY KEY,title8 TEXT UNIQUE,season TEXT ,duration INTEGER,dir_id TEXT ,genre TEXT ,rating INTEGER)''')
cur.execute('''CREATE TABLE IF NOT EXISTS DIRECTORY 
            (id INTEGER PRIMARY KEY,name TEXT )''')
cur.execute('''CREATE TABLE IF NOT EXISTS COUNTRY
            (id INTEGER PRIMARY KEY,name TEXT )''')
cur.execute('''CREATE TABLE IF NOT EXISTS SERIES
            (id INTEGER PRIMARY KEY,title1 TEXT ,season TEXT ,duration INTEGER,dir_id INTEGER,genre TEXT ,rating INTEGER)''')

# 1_ read our cvs file and select ones that has word __Movie__ on it
# 2_ insert all values on its column
df=pd.read_csv('netflix_titles.csv')
df=df[df['type'].str.contains('Movie')]
for data in df.itertuples():
    try:
        cur.execute("""INSERT OR IGNORE INTO FILM (title8,season,duration,dir_id,genre,rating) VALUES(?,?,?,?,?,?)""",
                    (data[3], data[1], data[10], data[4], data[2], data[9]))
        conn.commit()
    except:
        continue

df=pd.read_csv('netflix_titles.csv')
df1=df[df['type'].str.contains('TV Show')]
for val in df1.itertuples():
    try:
        cur.execute("""INSERT OR IGNORE INTO SERIES (title1,season,duration,dir_id,genre,rating) VALUES(?,?,?,?,?,?)""",
                    (val[3], val[1], val[10], val[4], val[2], val[9]))
        conn.commit()
    except:
        continue

df2=pd.read_csv('netflix_titles.csv')
for val2 in df2.itertuples():
    try:
        cur.execute("""INSERT OR IGNORE INTO COUNTRY (name) VALUES(?)""",(val2[6],))
        conn.commit()
    except:
        continue

df3=pd.read_csv('netflix_titles.csv')
for val3 in df3.itertuples():
    try:
        cur.execute("""INSERT OR IGNORE INTO DIRECTORY (name) VALUES(?)""",(val3[4],))
        conn.commit()
    except:
        continue


cur.close()



