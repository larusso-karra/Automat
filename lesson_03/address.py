class Address:
    # Конструктор принимает индекс, город, улицу, дом и квартиру
    def __init__(self, index, city, street, house, apartment):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment