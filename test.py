from itertools import combinations

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
clothes_dict = {}
combi_list = []
answer = 0 
for i in clothes:
    cloth = i[0]
    gear = i[1]
    if gear not in clothes_dict.keys():
        clothes_dict[gear] = []
        clothes_dict[gear].append(cloth)
    else:
        clothes_dict[gear].append(cloth)

# ! 조건 3개일 경우 fail
# length_value = 1
# for key,value in clothes_dict.items():
#     answer = answer + len(value)
#     if len(clothes_dict.keys()) > 1:
#         length_value = length_value * len(value)
#     else:
#         length_value =0
# answer = answer + length_value
#print(answer)
single = 0
key_count = 0
for key,value in clothes_dict.items():
    single = single + len(value)
    key_count = len(clothes_dict.keys())
    for j in value:
        combi_list.append(j)

combi_list = list(combinations(combi_list,key_count))
# TODO 같은 gear 2개 이상 들어간 list를 filter링해서 제거
answer = key_count + len(combi_list)
print(answer)
    

