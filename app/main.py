from app.who_is_there import astros
from app.who_is_there import average
from app.user_generator import print_users
from app.user_generator import generate_users
from app.reading_a_file import reading_a_file
def main():
    reading_a_file()
    print('\n')

    users = generate_users()
    print_users(users, True)
    print('\n')

    print('Who is There\n')
    astros()
    average()