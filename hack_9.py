"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    resultNew =[]
    i = 0
    while i < len(result):
        resultNew.append(result[i])
        resultNew.append('@')
        i += 1
    return resultNew
print(fn_hack_9())

