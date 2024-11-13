first = input()
second = input()
third = input()
if first == second == third:
    print(first, second, third)
elif first == third or second == third:
    print(first, second)
elif first != second != third:
    print(0)