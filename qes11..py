def sameType(lst):
    if not lst:
        return True  
    
    first_type = type(lst[0])  
    
    for item in lst:  
        if type(item) != first_type:  
            return False  
            
    return True  

print(sameType([1, 2, 30]))         
print(sameType(['rijesh', 1, 2]))