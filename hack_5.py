"""
text: "fooziman" output => "f00z1m@n"
"""

def fn_hack_5():
    result = "fooziman"
    replacements = {
        'o': '0',
        'i': '1',
        'a': '@'
    }

    result = ''.join(replacements.get(c, c) for c in result)
    return result

print(fn_hack_5())
