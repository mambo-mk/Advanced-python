for i in range(1, 51):
    if (i % 5 == 0) and (i % 3 == 0):
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(str(i))
print(i)

x = [1,2,3]
print(sum(x))
