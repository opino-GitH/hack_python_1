"""
loop: while [] output => [5,4,3,2,1,0]
"""

def fn_hack_7():
    result = []
    cont = 5
    while cont >= 0 :
        result.append(cont)
        cont -= 1
    return result 
print(fn_hack_7()) 