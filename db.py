import sqlite3
import os

# db 경로
db_path = os.getenv('HOME')+'/etridb.db'

# ----------- 테이블 생성 -----------------
# db와 연결
conn = sqlite3.connect(db_path)
c = conn.cursor()

# 테이블이 이미 존재할 경우 삭제
c.execute("DROP TABLE IF EXISTS orders")
# 테이블 생성
c.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id integer,
        menu text,
        amount integer not null,
        price integer not null,
        time timestamp not null default current_timestamp,
        PRIMARY KEY (id, menu)
    );""")

# 테이블이 생성 되었는지 출력하여 확인
c.execute('SELECT * FROM sqlite_master WHERE type="table" AND name="orders";')
table_list = c.fetchall()
for i in table_list:
    for j in i:
        print(j)
# db와 연결 종료
conn.close()
# ----------- 테이블 생성 -----------------

# ----------- insert test -----------------
# db와 연결
conn = sqlite3.connect(db_path)
c = conn.cursor()
# insert 쿼리
INSERT_SQL = "INSERT INTO orders(id, menu, amount, price) VALUES (?, ?, ?, ?);"
# 데이터 한 번에 여러개 추가
data = (
    (1, "치즈 버거", 2, 10000),
    (1, "치킨 버거", 1, 5000)
)
c.executemany(INSERT_SQL, data)
# 커밋 해야 실제로 db에 반영됨
conn.commit()

# 제대로 실행되었는지 출력하여 확인
c.execute('SELECT * FROM orders;')
item_list = c.fetchall()
for i in item_list:
    print(i)
# db와 연결 종료
conn.close()
# ----------- insert test -----------------