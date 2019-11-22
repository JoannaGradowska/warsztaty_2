from psycopg2 import connect, OperationalError
from models.User import User
from local_settings import user, password, host, database


def connecting():
    try:
        cnx = connect(user=user, password=password, host=host, database=database)
    except OperationalError as e:
        return f"Nie udało się ustanowić połączenia ({e})"
    else:
        cnx.autocommit = True
        cursor = cnx.cursor()
        return cursor


# example = User()
# example.username = "example_name"
# example.email = "example@mail.pl"
# example.set_password("example_password")
# example.save_to_db(connecting())
