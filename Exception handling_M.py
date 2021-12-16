try:
    print(10 / 0)
except ZeroDivisionError as msg:
    print(print("exception raised and its description is:", msg))

try:
    x = int(input("Enter First Number: "))
    y = int(input("Enter Second Number: "))
    print(x / y)
except ZeroDivisionError:
    print("Can't Divide with Zero")
except ValueError:
    print("please provide int value only")
finally:
    print("done")