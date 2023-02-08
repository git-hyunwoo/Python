import sqlite3

conn = sqlite3.connect('test.db')

cursor = conn.cursor()

creare_sql = \
'''
create table if not exists Item(
	id integer primary key autoincrement,
	code text not null,
	artist text not null,
	price integer not null
	);
'''

cursor.execute(creare_sql)

cursor.execute('select * from sqlite_master where type = "table" and name = "Item"')
table_list = cursor.fetchall()
for i in table_list:
	for j in i:
		print(j)
		
cursor.close()
