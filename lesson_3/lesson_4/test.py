
text = 'I love Python'
print ('love' in text)
print ('Love' in text)


b = 2
c = 2
d = 258
e = 258
print(id(b))
print(id(c))
print(id(d))
print(b is c)
print(d is not e)

a = '1'
print(type(a))
a = int(a)
print(type(a))
a = str(a)
print(type(a))
b = 'True'
print(type(b))
b = bool(b)
print(type(b))
a = float(a)
print(type(a))
print(a)

user_inp = int(input('Введи что-нибудь'))
print(type(user_inp))
print(user_inp + 2)


my_list =[1, 3, 6 ,7, None, 'ext', False, 2.42, 'last', 'last2']
print(my_list[2])
print(my_list[4])
print(my_list[-1])
print(my_list[-5])

my_list[2] = 42555
print(my_list)


listik = list()
listik.append(42)
listik.append('text')
print(listik)
print(len(my_list))
print(my_list.index(42555))
poped = my_list.pop(0)
print(my_list)
print(poped)

print(3 in my_list)


my_tuple =(1, 3, 6 ,7, None, 'ext', False, 2.42, 'last', 'last2')
print(my_tuple[1])
print(my_tuple[5])
print(my_tuple[-1])
#my_tuple[4] = 42

my_tuple = ()
my_tuple = tuple()
my_tuple = (1, 2, 2, 3, 4, 5)
print(my_tuple)
print(my_tuple.count(2))
print(my_tuple.index(5))

llist = [56]
print(llist)
ttuple = (56,)
print(ttuple)
print(type(ttuple))


my_set ={1, 3, 6 ,7, None, 'ext', False, 2.42, 'last', 'last2', 3, 'last'}
#print(my_set[2])
my_set.add(4555)
print(my_set)


list1 = list(set([1, 2, 5, 7, 3, 2, 1, 9]))
#list1 = set(list1)
#list1 = list(list1)
print(list1)


my_set = {}     #словарь
print(type(my_set))
my_set = set() # пустой сет можно создать только так
print(type(my_set))


my_dict = {'one': 'value', 'two': 'value2'}
print(my_dict['two'])
print(my_dict)
print(len(my_dict))
my_dict['one'] = 'myoneoneone'
my_dict['three'] = 'value3'
print(my_dict)
my_dict['four'] = False
my_dict['five'] = [1, 3, 5]
my_dict['six'] = {1, 3, 5}
my_dict[2] = 'fsdfsdfsdfsfsdfsdf'
my_dict[True] = '123123123'
my_dict[2.42] = True
my_dict[(666666)] = 'True'
print(my_dict)
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())