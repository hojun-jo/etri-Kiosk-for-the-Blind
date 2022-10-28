import sqlite3
import os


# 주문 갯수 문자에서 숫자로 바꿀 변수
amount_string_to_int = { 
    "하나" : 1, "한개" : 1, 
    "둘" : 2, "두개" : 2,
    "셋" : 3, "세개" : 3, 
    "넷" : 4, "네개" : 4,
    "다섯" : 5, "다섯개" : 5,
    "여섯" : 6, "여섯개" : 6,
    "일곱" : 7, "일곱개" : 7,
    "여덟" : 8, "여덟개" : 8,
    "아홉" : 9, "아홉개" : 9
    }

# db 경로
db_path = os.getenv('HOME')+'/etridb.db'


# 테이블 생성
def create_table():
    # db와 연결
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    # 테이블 생성
    c.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id integer primary key autoincrement,
            order_number integer not null,
            menu text not null,
            amount integer not null,
            price integer not null,
            time timestamp default current_timestamp
        );
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS menus (
            menu text primary key,
            category text not null
        );
    """)

    # 테이블이 생성 되었는지 출력하여 확인
    c.execute('SELECT * FROM sqlite_master WHERE type="table" AND name="orders";')
    table_list = c.fetchall()
    for i in table_list:
        for j in i:
            print(j)
    c.execute('SELECT * FROM sqlite_master WHERE type="table" AND name="menus";')
    table_list = c.fetchall()
    for i in table_list:
        for j in i:
            print(j)

    # db와 연결 종료
    conn.close()

# DB에 메뉴 목록 insert
def insert_menus():
    # db와 연결
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    # insert 쿼리
    INSERT_SQL = "INSERT INTO menus(menu, category, price) VALUES (?, ?, ?);"
    # 데이터 한 번에 여러개 추가
    # data = (
    #     ("라면", "분식", 2500),
    #     ("치즈라면", "분식", 3000),
    #     ("유부우동", "분식", 2500),
    #     ("새우튀김우동", "분식", 3600),
    #     ("꼬치어묵우동", "분식", 3500),
    #     ("돈까스우동정식", "분식", 5000),
    #     ("햄치즈순두부찌개", "분식", 5200),
    #     ("돼지고기김치찌개", "분식", 4800),
    #     ("새우튀김알밥", "비빔밥", 4500),
    #     ("육회비빔밥", "비빔밥", 5500),
    #     ("에비카레동", "비빔밥", 4500),
    #     ("치킨가라아카레동", "비빔밥", 5000),
    #     ("콩불덮밥", "비빔밥", 4800),
    #     ("간장돼불덮밥", "비빔밥", 4500),
    #     ("소떡소떡", "돈까스", 3000),
    #     ("고구마돈까스", "돈까스", 4500),
    #     ("오므라이스", "돈까스", 3500),
    #     ("양념치킨오므라이스", "돈까스", 5000),
    #     ("소시지오므라이스", "돈까스", 4500),
    #     ("돈까스오므라이스", "돈까스", 4800)
    # )
    data = (
        ("김치햄치즈볶음밥", "한식", 4500),
        ("소금덮밥", "한식", 4500),
        ("뼈다귀해장국", "한식", 4000),
        ("소고기미역국", "한식", 4000),
        ("냉면", "한식", 4000),
        ("간장불고기", "한식", 4500),
        ("제육볶음", "한식", 4500),
        ("짜장면", "중식", 2500),
        ("짬뽕", "중식", 2500),
        ("계란볶음밥", "중식", 3800),
        ("탕수육", "중식", 5000),
        ("군만두", "중식", 3000),
        ("떡볶이", "분식", 3000),
        ("라볶이", "분식", 3000),
        ("라면", "분식", 2500),
        ("순대", "분식", 3000),
        ("오므라이스", "분식", 3800),
        ("야채김밥", "분식", 2000),
        ("참치김밥", "분식", 2200),
        ("크림파스타", "양식", 3000),
        ("토마토파스타", "양식", 3000),
        ("알리오올리오", "양식", 3000),
        ("연어샐러드", "양식", 3000),
        ("감바스", "양식", 3000),
        ("왕돈까스", "일식", 4500),
        ("치킨까스", "일식", 4500),
        ("치즈돈까스", "일식", 4500),
        ("냉모밀", "일식", 2500),
        ("우동", "일식", 2500),
        ("김치나베", "일식", 3500),
        ("돈까스나베", "일식", 4000),
        ("물", "음료", 1000),
        ("콜라", "음료", 1000),
        ("사이다", "음료", 1000),
        ("환타", "음료", 1000),
        ("제로콜라", "음료", 1000),
        ("제로사이다", "음료", 1000)
    )
    c.executemany(INSERT_SQL, data)
    # 커밋 해야 실제로 db에 반영됨
    conn.commit()
    # 제대로 실행되었는지 출력하여 확인
    c.execute('SELECT * FROM menus;')
    item_list = c.fetchall()
    for i in item_list:
        print(i)
    ### 메뉴 insert

    # db와 연결 종료
    conn.close()

# DB에 주문 내역 insert
def insert_order(data):
    # db와 연결
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    # insert 쿼리
    INSERT_SQL = "INSERT INTO orders(order_number, menu, amount) VALUES (?, ?, ?);"
    # 데이터 한 번에 여러개 추가
    c.executemany(INSERT_SQL, data)
    # 커밋 해야 실제로 db에 반영됨
    conn.commit()
    # 제대로 실행되었는지 출력하여 확인
    print("===== db =====")
    c.execute('SELECT * FROM orders;')
    item_list = c.fetchall()
    for i in item_list:
        print(i)
    
    # db와 연결 종료
    conn.close()

# DB에서 메뉴 정보 가져오기
def menu_info(category):
    # 메뉴 정보 저장할 변수
    menu_info = []
    # db와 연결
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    # select 쿼리
    SELECT_SQL = 'SELECT menu FROM menus WHERE category = "%s";' % category

    # select로 가져오기
    c.execute(SELECT_SQL)
    menu_info = c.fetchall()

    # db와 연결 종료
    conn.close()
    return menu_info

# 테이블 삭제
def drop_table():
    # db와 연결
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    # 테이블이 이미 존재할 경우 삭제
    c.execute("DROP TABLE IF EXISTS orders")
    c.execute("DROP TABLE IF EXISTS menus")
    # db와 연결 종료
    conn.close()


drop_table()
create_table()
insert_menus()
menu = {
    "korean" : menu_info("한식"),
    "chinese" : menu_info("중식"),
    "schoolfood" : menu_info("분식"),
    "Westernfood" : menu_info("양식"),
    "japanesefood" : menu_info("일식"),
    "beverage" : menu_info("음료")
}
print(menu)