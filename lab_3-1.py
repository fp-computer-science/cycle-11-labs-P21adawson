# Azaan Dawson amdg

def double_stuffed(lst):
    for index, value in enumerate(lst):
        lst[index] = 2 * value
    return lst

result = double_stuffed([1, 2, 3, 4, 5])
print(result)        
print(double_stuffed([1,2,3,4,5]) == [2,4,6,8,10])