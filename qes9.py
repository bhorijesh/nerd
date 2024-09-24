def mid_item(food_stuff_tp):
    mid = len(food_stuff_tp) // 2
    middle_item = food_stuff_tp[mid]
    return middle_item

fruits = ('apple','banana','mango')
vegetable = ('spinach','pumpkin','cauliflower')
animal = ('dog','cat','cow','goat','ball')

food_stuff_tp =fruits + vegetable + animal
print(food_stuff_tp)
divide = len(food_stuff_tp) //2 
middle_item = mid_item(food_stuff_tp)
print(middle_item)
tupe1 = food_stuff_tp[:divide]
tupe2 = food_stuff_tp[divide:]

print(tupe1)
print(tupe2)



