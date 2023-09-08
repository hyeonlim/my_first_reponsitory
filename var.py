"""
my_var = 10
print(my_var)

my_list = [1, 2, 3]
print(my_list)
print(*my_list)  #별표(*)를 붙이면. 괄호와 쉼표를 없애고 print (저장된 모든 값)
 # shift + alt + a, 그냥 주석은 ctrl + /

my_int = 10
my_float = 3.14
my_complx = 3 + 4j

print(my_int)
print(my_float)
print(my_complx)

my_character = 'A'
my_char = "@"
print(my_character)
print(my_char)

my_string = 'Hello, World!'
str_name = "python"
print(my_string)
print(str_name)

my_bool = True
bFlag = False
print(my_bool)
print(bFlag) """

""" my_list = [10, 3, 8, 9, 42, "hello"]
print(my_list)

print(my_list.__len__()) # __len__은 리스트의 크기를 확인

print(my_list[3]) #인덱스, my_list의 세번째 요소를 가져다 줘

list_el = my_list[2]
print(list_el)

my_list[3] = 11 #엘레멘트 변경
print(my_list) 

n_add = my_list[3] + my_list[2]
print(n_add) #데이터 타입 확인해서 넣기!

print(my_list[2:5]) #두번째부터 다섯번째까지 출력하라
print(my_list[0:3]) #영번째부터 세번째까지 출력하라
print(my_list[4:]) #네번째부터 마지막까지 출력하라 """

#이중리스트

""" my_list = [10, 3, 8, 9, 42, "hello", [5, 4, 2, "world"]]

print(my_list)

print(my_list[6][1]) #my_list의 요소 6번째의 2번째 데이터를 출력하라

print(my_list[6][2:]) """

# 메소드

""" my_list = [10, 3, 8, 9, 42, "hello"]
print(my_list)

my_list.insert(2, 4) # 2번째에 데이터값 4 삽입

print(my_list.index(3)) #리스트 안에 데이터값 3이 몇개 있어?

my_list.append(22) #리스트의 마지막에 데이터값 22 추가
print(*my_list)

print(my_list.count(8)) #value와 동일한 요소, 갯수 출력 인덱스와 달리 오류 없음

print(my_list.pop()) # 마지막 요소 출력 후 삭제
print(*my_list)
 """
 
""" my_list = [10, 3, 8, 9, 42, 8]

print(my_list)

my_list.sort() #<

print(*my_list)

my_list.reverse()

print(*my_list) #> 

my_list = [10, 3, 8, 9, 42, 8, "hello"]
list_tmp = [5, 7, "world"]

print(my_list, list_tmp)

my_list.extend(list_tmp) #결합

print(*my_list)

list_tmp.clear()
print(list_tmp)

my_list.remove(3) #요소 3을 삭제하라... 이말이여
print(*my_list)

del my_list[2] #두번째 요소를 지우라
print(*my_list) """

#튜플 (리스트와 비슷하지만 가변성이 없어서 수정 불가능)

""" my_tup = (4, 2, 6, 1, "py", "w")
print(my_tup)
print(*my_tup)
print(my_tup.__len__())

#참조는 가능함
print(my_tup[2])
# my_tup[3] = 2 가변성 없어서 변경 안됨

print(my_tup[2] + my_tup[0])

n_add = my_tup[1] + my_tup[3]
print(n_add)

print(*my_tup)

print(my_tup[2:5])
print(my_tup[1:4])
print(my_tup[:3])
print(my_tup[2:]) """

#이중튜플
""" my_tup = (4, 2, 6, 1, "py", "w", ("h", 8, 7, 3))
print(my_tup)

print(my_tup[6][0]) #h만 출력하기 """

#메소드
""" my_tup = (4, 2, 6, 1, "py", "w")

print(my_tup.index(2, 0, 3)) #0~3까지 중에 2가 몇번째 있냐

print(my_tup.index("py", 3, 5)) #3~5까지 중에 py가 몇번째에 있냐 """

#딕셔너리

""" 
# 인덱싱
my_dict = {'key1': 'value1', 'key2': 'value2'}
dicData = {"name" : "python", "number" : 23564897}

print(my_dict)
print(*my_dict)

my_item = my_dict.items()
print(my_item)

idx = ("key1", "key2", "key3")
dicts = dict.fromkeys(idx, "0")
print(dicts)

print(my_dict["key1"])

my_str = my_dict.get("key2")
print(my_str) 

#print(my_dict.pop("key1"))
#print(my_dict) """

#복사
""" my_dict = {'key1': 'value1', 'key2': 'value2'}
dicts = my_dict.copy()
print(dicts)
print(my_dict)
 """
 
#추가 변경
""" my_dict = {'key1': 'value1', 'key2': 'value2'}
dicData = {"name" : "python", "number" : 23564897}

my_dict["key3"] = "value3"

print(my_dict) """


""" my_dict = {'key1': 'value1', 'key2': 'value2'}

my_dict.setdefault("key3")

print(my_dict) """


""" my_dict = {'key1': 'value1', 'key2': 'value2'}

my_dict.update({"key1" : "v4"})

print(my_dict) """


""" my_dict = {'key1': 'value1', 'key2': 'value2'}

del my_dict["key2"]

print(my_dict) """


""" 
my_dict = {'key1': 'value1', 'key2': 'value2'}
print("key2" in my_dict)
print("key3" in my_dict) 
"""

""" my_dict = {'key1': 'value1', 'key2': 'value2'}
my_list = list(my_dict.key())
print(my_list) """

""" my_dict = {'key1': 'value1', 'key2': 'value2'}
my_set = set(my_dict.keys())
print(my_set)
 """
my_dict = {'key1': 'value1', 'key2': 'value2'}
my_dict.clear()
print(my_dict)

