my_list: list[int] = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
positive = []
index = 0
while index < len(my_list):
    if my_list [index] < 0:
        break
    positive.append(my_list[index])
    index += 1
print(positive)
