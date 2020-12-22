from controller import Controller
from models.details import Details


def dbb():
    from database import Database
    database = Database()
    # print(database.select_id(Details, 'Overcast'))
    # print(database.select_f(Details, 'Overcasst', Details.conditions))
    print(database.backup())

# dbb()

cntr = Controller()

