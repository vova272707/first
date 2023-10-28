class House:
    def __init__(self, house_id, street_id, name):
        self.house_id = house_id
        self.street_id = street_id
        self.name = name

class Street:
    def __init__(self, street_id, name):
        self.street_id = street_id
        self.name = name

# Тестовые данные
houses = [
    House(1, 1, "46"),
    House(2, 1, "82"),
    House(3, 2, "3"),
    House(4, 3, "51"),
    House(5, 3, "16")
]

streets = [
    Street(1, "Молодёжная"),
    Street(2, "Бауманская"),
    Street(3, "Ландышевая")
]

# Задание 1
result1 = [(house.name, street.name) for house in houses for street in streets if house.street_id == street.street_id]
result1.sort(key=lambda x: x[0])
print("Список всех связанных домов и улиц, отсортированный по домам:")
print(result1)

# Задание 2
result2 = [(street.name, sum(1 for house in houses if house.street_id == street.street_id)) for street in streets]
result2.sort(key=lambda x: x[1])
print("Список улиц с домами, отсортированный по количеству домов:")
print(result2)

# Задание 3
result3 = [(house.name, street.name) for house in houses for street in streets if house.street_id == street.street_id and house.name.endswith("я")]
print("Список всех домов, у которых название заканчивается на «я», и улицы, на которых они находятся:")
print(result3)
