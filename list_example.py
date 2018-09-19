'''
Created on Sep 19, 2018

@author: lenovo
'''
print("list example")
list_obj = [1,10,'raj',99.99]

def append(value):
    list_obj.append(value)
    return list_obj
    
def remove(value):
    list_obj.remove(value)
    return list_obj

def pop_elem():
    list_obj.pop()
    return list_obj
    
print(append(100))
print(remove('raj'))
print(pop_elem())