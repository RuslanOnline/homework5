immutable_var =[1 ,2 ,'a' ,'b']
print(immutable_var)
#immutable_var .tuple[0] = 4 #Ошибка
#Кортеж - неизменяемый тип данных, кроме списка внутри, его можно изменять.
#Кортеж хранит ссылку на список, а не сам список.
mutable_list = (1, [2, 5, 4], 9, 10)
print(mutable_list)
mutable_list[1][2] = 10
print(mutable_list)
mutable_list_mod = (1 ,2 ,3 ,)
print(mutable_list_mod)
mutable_list_mod =(1 ,2 ,3 ,'modified')
print(mutable_list_mod)
