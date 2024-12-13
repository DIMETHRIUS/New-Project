class House:
    def go_to(self, new_floor):
        for i in range(1, new_floor + 1):
            if 1 <= new_floor <= self.number_of_floors:
                print(i)
            elif 1 <= new_floor:
                print(f'Такого этажа не существует')
                break
    def __init__(self, name, number_of_floors,):
        self.name = name
        self.number_of_floors = number_of_floors


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

h1.go_to(5)
h2.go_to(10)
