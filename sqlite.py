import sqlite3

con=sqlite3.connect("c:\\work\\sample.db")
cur=con.cursor()

cur.execute(
    "create table if not exists PhoneBook " + 
    "(id integer primary key autoincrement, name text, phoneNum text);")

cur.execute("insert into PhoneBook (name, phoneNum) values ('홍길동','010-111-1234');")

name = "이순신"
phoneNumber = "010-222-1234"
cur.execute("insert into PhoneBook (name, phoneNum) values (?, ?);", (name, phoneNumber))

#다중의 데이터를 입력
datalist = (("전우치","010-123-1234"), ("박문수","010-1234-5678"), ("왕용진","010-1234-5678"))
cur.executemany("insert into PhoneBook (name, phoneNum) values (?, ?);", datalist)


#결과를 확인
cur.execute("select * from PhoneBook;")
for row in cur:
    print(row)



con.commit()
