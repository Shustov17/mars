from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

def main():
    db_session.global_init("db/mars_explorer.db")
    session = db_session.create_session()

    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    user.hashed_password = "cap"
    user.set_password(user.hashed_password)
    session.add(user)

    user = User()
    user.surname = "Marco"
    user.name = "Reus"
    user.age = 31
    user.position = "cam"
    user.speciality = "assistant"
    user.address = "module_2"
    user.email = "marco_reus@mars.org"
    user.hashed_password = "11"
    user.set_password(user.hashed_password)
    session.add(user)

    user = User()
    user.surname = "Quincy"
    user.name = "Promes"
    user.age = 29
    user.position = "lw"
    user.speciality = "goleador"
    user.address = "module_3"
    user.email = "mask_off@mars.org"
    user.hashed_password = "10"
    user.set_password(user.hashed_password)
    session.add(user)

    user = User()
    user.surname = "Alexandr"
    user.name = "Sobolev"
    user.age = 24
    user.position = "st"
    user.speciality = "dolphine"
    user.address = "module_4"
    user.email = "sashka_sobol@mars.org"
    user.hashed_password = "7"
    user.set_password(user.hashed_password)
    session.add(user)


if __name__ == '__main__':
    main()
