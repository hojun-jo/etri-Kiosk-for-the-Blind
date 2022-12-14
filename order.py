from APIs.etri_audio import etri_audio_result
from APIs.etri_lang import etri_lang_result
import db


# 각 문자열에서 공백 제거
def remove_space(orders):
    for i in range(len(orders)):
        orders[i] = orders[i].replace(" ", "")

# 문자열로 된 수량을 숫자로 변경
def amount_str_to_int(orders):
    for i in range(len(orders)):
        if orders[i] in db.amount_string_to_int:
            orders[i] = db.amount_string_to_int[orders[i]]

# 수량이 없을 경우 1 삽입
# 빈 배열에 수량이 없는 부분의 인덱스 저장
def insert_amount(orders):
    idx = []
    for i in range(len(orders)):
        if isinstance(orders[i], str):
            try:
                if not isinstance(orders[i + 1], int):
                    idx.append(i + 1 + len(idx))
            except IndexError:
                idx.append(i + 1 + len(idx))
    # 수량이 없는 부분의 인덱스에 1 추가
    for i in idx:
        orders.insert(i, 1)

# 메뉴 정보에서 메뉴 이름만 가져오기
def get_menu_names():
    res = []
    for i in menu_info:
        res.append(i[0])
    return res

# 메뉴 이름이 db에 있는 이름인지 확인
def check_menu_name(orders):
    for i in orders[0::2]:
        menus = get_menu_names()
        if i not in menus:
            print("--------------menu is not in db-----------------")
            return False
    return True


# 주문 내역 DB에 저장
def insert_db(orders):
    data = []
    global order_number
    menus, amounts = split_menu_names_amounts(orders)
    for i in range(len(menus)):
        data.append((order_number, menus[i], amounts[i], amounts[i] * get_menu_price(menus[i])))
    # print(data)
    db.insert_order(data)
    order_number += 1

# 주문 내역에서 메뉴 이름, 수량 분리
def split_menu_names_amounts(orders):
    menus = []
    amounts = []
    for i in orders[0::2]:
        menus.append(i)
    for i in orders[1::2]:
        amounts.append(i)
    return menus, amounts

# 메뉴의 가격 찾기
def get_menu_price(menu):
    for i in menu_info:
        if i[0] == menu:
            return i[2]


# 주문 번호 = 1
order_number = 1
# 테스트용 주문
# order_list = ['치즈라면', '라면', '두 개', '돈까스오므라이스']
# api 사용한 주문
order_list = etri_lang_result(etri_audio_result())
# 전체 메뉴 정보
menu_info = db.menu_info()
print("===== order =====")
print(order_list)
remove_space(order_list) # 주문 정보에서 공백 제거
amount_str_to_int(order_list) # 수량 정보 int로 변환
insert_amount(order_list) # 수량 정보 결측시 1로 삽입
print(order_list)
if check_menu_name(order_list): # 메뉴 이름 DB에 있는지 확인
    insert_db(order_list) # DB에 삽입