burger_list=[]
drink_list=[]
for i in range(3):
    burger_price=int(input())
    burger_list.append(burger_price)
for i in range(2):
    drink_price=int(input())
    drink_list.append(drink_price)
print(min(burger_list)+min(drink_list)-50)