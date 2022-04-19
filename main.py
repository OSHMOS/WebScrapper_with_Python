# return
# return a value
# quit the function
def p_plus(a, b):
    print(a + b)

def r_plus(a, b):
    return a + b
    print(a + b) # do not print

p_result = p_plus(2, 3)
r_result = r_plus(2, 3)

print(p_result, r_result)