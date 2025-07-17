"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""
import json

def fn_hack_10():
    result = "fooziman"
    resultList=[]
    
    for i in range(len(result)):
       if result[i] == "f":
            resultList.append("F")
       elif result[i] == "o":
             resultList.append("0")
       elif result[i] == "z":
             resultList.append("Z")
       elif result[i] == "i":
             resultList.append("1")
       elif result[i] == "m":
             resultList.append("M")
       elif result[i] == "a":
             resultList.append("@")
       elif result[i] == "n":
             resultList.append("N")
    return resultList

print(json.dumps(fn_hack_10()))



