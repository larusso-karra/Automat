from smartphone import Smartphone

# Список экземпляров класса Smartphone
catalog = [
    Smartphone("Apple", "iPhone 13", "+79161234567"),
    Smartphone("Samsung", "Galaxy S22", "+79201234678"),
    Smartphone("Xiaomi", "Redmi Note 10", "+79341234789"),
    Smartphone("Huawei", "P50 Pro", "+79451234890"),
    Smartphone("OnePlus", "9 Pro", "+79561234901")
]

# Проходим по списку и выводим информацию о каждом смартфоне
for smartphone in catalog:
    print(smartphone.brand, "-", smartphone.model, ".", smartphone.phone_number)