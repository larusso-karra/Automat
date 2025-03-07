from address import Address
from mailing import Mailing

# Создаём объекты классов Address
to_address = Address("123456", "Москва", "Ленинградский проспект", "15", "20")
from_address = Address("654321", "Санкт-Петербург", "Невский проспект", "25", "30")

# Создаём объект класса Mailing
mailing = Mailing(to_address, from_address, 500, "ABC12345")

# Выводим информацию об отправлении
print(
    f"Отправление {mailing.track} из {mailing.from_address.index}, "
    f"{mailing.from_address.city}, {mailing.from_address.street}, "
    f"{mailing.from_address.house}-{mailing.from_address.apartment} в "
    f"{mailing.to_address.index}, {mailing.to_address.city}, "
    f"{mailing.to_address.street}, {mailing.to_address.house}-"
    f"{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей."
)