def plus(a, b):
    return a + b
    
result = plus(b=30, a=1)
print(result)

def say_hello(name, age):
    return f'Hello {name}. You are {age} years old'

hello = say_hello(24, 'oshmos')
print(hello)
hello = say_hello(name='oshmos', age=24)
print(hello)