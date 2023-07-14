from faker import Faker
from typing import NamedTuple
from collections.abc import Iterator

faker=Faker()
class User(NamedTuple):
    name: str
    email: str

def generate_user()->User:
    return User(
        name= faker.first_name(),
        email= faker.email(),
    )
def generate_users(amount: int =100) -> Iterator[User]:
    for index in range(1, amount +1):
        yield generate_user()

def print_users():
    for index, user in enumerate(generate_users()):
        string = (f'{index} Name: {user.name}, email: {user.email}')
        print(string)
