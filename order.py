from APIs.etri_audio import etri_audio_result
from APIs.etri_lang import etri_lang_result
import db

order_number = 1
order_list = ['치즈라면', '라면', '두 개', '돈까스오므라이스']
menu_info = db.menu_info()

# str = "참치마요 하나, 라면 두 개, 돈까스오므라이스 주세요."
# x = etri_lang_result(str)
# print(x)


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
    menus, amounts = split_menu_names_amounts(orders)
    for i in range(len(menus)):
        data.append((order_number, menus[i], amounts[i], amounts[i] * get_menu_price(menus[i])))

    print(data)
    # db.insert_order(data)

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
        print(f"get menu price i {i}")
        if i[0] == menu:
            print(f"i[2] {i[2]}")
            return i[2]

print(order_list)
remove_space(order_list)
amount_str_to_int(order_list)
insert_amount(order_list)
print(order_list)
if check_menu_name(order_list):
    insert_db(order_list)