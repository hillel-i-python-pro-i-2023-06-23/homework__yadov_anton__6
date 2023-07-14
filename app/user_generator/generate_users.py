from faker import Faker
from typing import NamedTuple
from collections.abc import Iterator
class User(NamedTuple):
    name: str
    email: str

faker=Faker()
def generate_user()->User:
    return User(
        name= faker.first_name(),
        email= faker.email(),
    )
def generate_users(amount: int =100) -> Iterator[User]:
    for index in range(1, amount +1):
        yield generate_user()


def print_users(users, is_print_index=False):
    for index, user in enumerate(users):
        string= (f'Name: {user.name}, email:{user.email}')
        if is_print_index:
            string = (f'{index} Name: {user.name}, email: {user.email}')
        print(string)
