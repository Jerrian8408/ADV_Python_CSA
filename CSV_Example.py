import csv
from pprint import pprint


def import_data():
    """
    Opens the CSV File and stores all the data in an array
    Removes the header from the CSV File
    Converts String ID to Ints
    """
    data = []
    with open('JBUDB.csv') as db_data:
        in_data = csv.reader(db_data, delimiter=',')
        for r in in_data:
            data.append(r)

        del data[0]

        for x in data:
            x[0]=int(x[0])

    return data


def find_by_id(id: int):
    return []


def find_by_firstname(firstname: str):
    return []


def find_by_lastname(lastname: str):
    return []


def find_by_email(email: str):
    return []


def find_by_position(position: str):
    return []


def find_by_department(department: str):
    return []


if __name__ == '__main__':
    pprint(import_data())

