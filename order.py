from APIs.etri_audio import etri_audio_result
from APIs.etri_lang import etri_lang_result
import db

order_number = 1
order_list = []
menu_info = db.menu_info()

# str = "참치마요 하나, 라면 두 개, 돈까스오므라이스 주세요."
# x = etri_lang_result(str)
# print(x)

x = ['참치마', '라면', '두 개', '돈까스오므라이스']

# 각 문자열에서 공백 제거
for i in range(len(x)):
    x[i] = x[i].replace(" ", "")
# 문자열로 된 수량을 숫자로 변경
for i in range(len(x)):
    if x[i] in db.amount_string_to_int:
        x[i] = db.amount_string_to_int[x[i]]
# 수량이 없을 경우 1 삽입
# 빈 배열에 수량이 없는 부분의 인덱스 저장
idx = []
for i in range(len(x)):
    if isinstance(x[i], str):
        try:
            if not isinstance(x[i + 1], int):
                idx.append(i + 1 + len(idx))
        except IndexError:
            idx.append(i + 1 + len(idx))
# 수량이 없는 부분의 인덱스에 1 추가
for i in idx:
    x.insert(i, 1)
print(x)