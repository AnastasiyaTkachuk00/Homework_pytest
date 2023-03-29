import mysql.connector as mysql

db = mysql.connect(
    host="localhost",
    user="root",
    passwd="password!",
    database="test_db"
)

cursor = db.cursor()
# cursor.execute("CREATE TABLE PC (PRO_ID INT, PRO_NAME VARCHAR(255), PRO_PRICE INT, PRO_COM INT)")
query = "INSERT INTO PC (PRO_ID, PRO_NAME, PRO_PRICE, PRO_COM)" \
         "VALUES (%s, %s, %s, %s)"

values = [
    (101, "Mother Board", 3200, 15),
    (102, "Key Board", 450, 16),
    (103, "ZIP drive", 250, 14),
    (104, "Speaker", 550, 16),
    (105, "Monitor", 5000, 11),
    (106, "DVD drive", 900, 12),
    (107, "CD drive", 800, 2),
    (108, "Printer", 2600, 13),
    (109, "Refill cartridge", 350, 13),
    (110, "Mouse", 250, 12)
]

cursor.executemany(query, values)
db.commit()
print(cursor.rowcount, "records inserted")

print('===== TASK 1 =====')
query = "SELECT SUM(PRO_COM) FROM PC"
cursor.execute(query)
print(cursor.fetchall())

print('===== TASK 2 =====')
query = "SELECT AVG(PRO_COM) FROM PC"
cursor.execute(query)
print(cursor.fetchall())

print('===== TASK 3 =====')
query = "SELECT PRO_COM FROM PC WHERE PRO_PRICE > 200 AND PRO_PRICE < 600"
cursor.execute(query)
print(cursor.fetchall())

print('===== TASK 4 =====')
query = "SELECT PRO_COM FROM PC WHERE PRO_PRICE = (SELECT MAX(PRO_PRICE) FROM PC)"
cursor.execute(query)
print(cursor.fetchall())

print('===== TASK 4.1 =====')
query = "SELECT MAX(PRO_PRICE) FROM PC"
cursor.execute(query)
print(cursor.fetchall())

print('===== TASK 5 =====')
query = "SELECT PRO_COM FROM PC WHERE PRO_PRICE = (SELECT MIN(PRO_PRICE) FROM PC)"
cursor.execute(query)
print(cursor.fetchall())

db.close()
