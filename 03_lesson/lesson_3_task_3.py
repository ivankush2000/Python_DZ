from Address import Address
from Mailing import Mailing 

# Адрес отправителя
from_add = Address(
    indeks = "655432",
    city = "Москва",
    street = "ул. Ленина",
    hom = "56",
    apartment = "23"
)

# Адрес получателя
to_add = Address(
    indeks = "591236",
    city = "Уфа",
    street = "ул. Новая",
    hom = "105",
    apartment = "9"
)

#  Почтовое отправление
Mai = Mailing(
    to_address = to_add,
    from_address = from_add,
    cost=250,
    track="AB123456789CD"
)

print(
    f"Отправление {Mai.track} из "
    f"{Mai.from_address.indeks}, {Mai.from_address.city}, {Mai.from_address.street}, "
    f"{Mai.from_address.hom} - {Mai.from_address.apartment} в "
    f"{Mai.to_address.indeks}, {Mai.to_address.city}, {Mai.to_address.street}, "
    f"{Mai.to_address.hom} - {Mai.to_address.apartment}. Стоимость {Mai.cost} рублей."
)