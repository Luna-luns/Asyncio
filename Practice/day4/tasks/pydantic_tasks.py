from pydantic import BaseModel

# Task 1
class User(BaseModel):
    id: int
    name: str
    email: str

user_data = {"id": 1, "name": "Иван", "email": "ivan@example.com"}
user = User(**user_data)
user_json = user.model_dump_json()
print(user_json)  # Сериализация словаря в JSON
print(user.name, user.email)  # Десериализация JSON обратно в экземпляр модели


# Task 2
class User2(BaseModel):
    id: int
    name: str
    email: str
    age: int | None = None

user_data = {"id": 1, "name": "Иван", "email": "ivan@example.com", "age": 30}
user_data2 = {"id": 2, "name": "Петр", "email": "petr@example.com"}
user = User2(**user_data)
user_json = user.model_dump_json()
print(user_json)  # Сериализация словаря в JSON
user = User2(**user_data2)
user_json2 = user.model_dump_json()
print(user_json2)  # Сериализация словаря в JSON

# Task 3
class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User3(BaseModel):
    id: int
    name: str
    email: str
    address: Address

user_data = {
    "id": 1,
    "name": "Иван",
    "email": "ivan@example.com",
    "address": {"street": "Тверская", "city": "Москва", "zip_code": "123456"}
}

user = User3(**user_data)
user_json = user.model_dump_json()
print(user_json)  # Сериализация словаря в JSON
print(user.name, user.email, user.address)  # Десериализация JSON обратно в экземпляр модели

# Task 4
class Item(BaseModel):
    name: str
    price: float

class Order(BaseModel):
    items: list[Item]

order_data = {"items": [{"name": "Яблоко", "price": 1.5}, {"name": "Банан", "price": 2.0}]}
order = Order(**order_data)
order_json = order.model_dump_json()
print(order_json)  # Сериализация словаря в JSON
print(*order.items)  # Десериализация JSON обратно в экземпляр модели

# Task 5
class User4(BaseModel):
    id: int
    name: str
    email: str

users_data = [
    {"id": 1, "name": "Иван", "email": "ivan@example.com"},
    {"id": 2, "name": "Петр", "email": "petr@example.com"}
]
for user in users_data:
    user_ex = User4(**user)
    print(user_ex.id, user_ex.name, user_ex.email)  # Десериализация JSON обратно в экземпляр модели
