def are_items_unique(input_list):
    return len(input_list) == len(set(input_list))

my_list = [1, 2, 3, 4]
print(are_items_unique(my_list))  

my_list_with_duplicates = [1, 2, 2, 4]
print(are_items_unique(my_list_with_duplicates))  

