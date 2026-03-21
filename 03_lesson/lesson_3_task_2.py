from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "Galaxy S25 FE", "+799 999 99 99"),
    Smartphone("Xiaomi", "Redmi Note 14", "+799 999 99 98"),
    Smartphone("iPhone", "17 Pro Max", "+799 999 99 97"),
    Smartphone("Tecno", "Camon 40 Premier", "+799 999 99 96"),
    Smartphone("POCO", "C65", "+799 999 99 95")
]
    
for phone in catalog:
    print(f"{phone.phone_brand} - {phone.phone_model}. {phone.number}")