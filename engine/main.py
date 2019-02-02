from random import randint
from engine.model.unit import Unit

d6 = lambda: randint(1, 6)

# IDEA: make the preview of actions (it can be premium function)


def somehow_get(something_got_from_server=None):
    """ guy on server, we need to make connections between
     the fight engine and server, and the server and front """
    return something_got_from_server

def somehow_send(data_to_send_to_server=None):
    return data_to_send_to_server


def order(cell_a, cell_b):
    pass


def legal(un, coords):
    return True or False


def phase_1(player, Map):
    data = somehow_get()  # here should be player's troops arrangement, like ((<unit_id>, <coords>), (<unit_id...)
    for unit in data:
        if not legal(unit[0], unit[1]):
            somehow_send("Can't place unit(s) there")
        else:
            Map[unit[1]] = unit[0]


def prephase_2(player, Map):
    pass


def phase_2(Map):
    pass


def phase_3(Map):
    pass


fighting = True


""" """

Map = [[[] for j in range(5)]for i in range(7)]