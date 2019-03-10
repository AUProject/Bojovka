from engine.model.unit import Unit
from random import randint
from math import floor
from engine.model.skills import skills, d10, d100
from engine.model.map import Map as mp

"todo: make a class Data and put all this shit inside"
"todo: make whole coordinate handling a part of Map class"

DEBUG = True


def check(data, template):
    pass
    return True


def somehow_get(something_got_from_server=None, template=0):
    """ guy on server, we need to make connections between
     the fight engine and server, and the server and front """
    if check(something_got_from_server, template):
        if DEBUG:
            pass
        else:
            return something_got_from_server
    else:
        raise Exception("Incorrect data")


def legal(un, coords):
    return True or False


def somehow_send(data_to_send_to_server=None):
    if DEBUG:
        print(data_to_send_to_server)
    return data_to_send_to_server


def phase_1(player, Map):
    """here should be player's troops arrangement, like
    (0,
    (
        (<unit_id>, <coords>),
        (<unit_id...);

    this is template 0
    for coordinate writing rules check engine/model/map.py
    """
    if DEBUG:
        global i
        data = DATA[i]
        i += 1
    else:
        data = somehow_get((), 0)
    success = True
    for unit in data[1]:
        responce = Map.place(unit[0], unit[1], player)
        if responce != 0:
            success = False
    return success


def prephase_2(player, Map):
    """here data should look like
    (1,
        (
            (caster, skill, data)  #  this is data for certain skill, not for phase overall
            (caster, skill, data)... # caster is Unit object
        ),
        (
            (unit, coords), # introduction into battle/descent
            (unit, coords)
        )
    )
    """
    if DEBUG:
        global i
        data = DATA[i]
        i += 1
    else:
        data = somehow_get((), 0)

    for action in data[1]:
        if d100 <= action[0].chance:
            action[1](action[2], Map)
        else:
            print("skill casting failed")

    for unit in data[2]:
        if not legal(unit[0], unit[1]):
            somehow_send("Can't place unit(s) there")
            return
        else:
            Map[unit[1]] = unit[0]
    Map.update()


def phase_2(Map):
    """
    here data should be like
    (2,
        (
            (unit_position, order[, target]),
            ((2, 4, 3, 2), "attack", (2, 1, 3[, 0]))...
        )
    )
    orders keywords -- "attack", "defence", "move", "close" #  close -> close combat
    """
    if DEBUG:
        global i
        data = DATA[i]
        i += 1
    else:
        data = somehow_get((), 2)
    effect = []
    for order in data[1]:
        if len(order) == 3:
            a, x, y, z = order[0]
            if len(order[2]) == 4:  #  it can be only attack or close combat-- exact coords of unit
                if Map.simple_check(order[0]) and Map.simple_check(order[2]):
                    damage = (d10() + Map[a][x][y][z].global_mod + Map[a][x][y][z].orders[0]) * 10
                    b, x1, y1, z1 = order[2]
                    Map[b][x1][y1][z1].hp -= damage
            if len(order[2]) == 3:
                if order[1] == "attack":
                    damage = (d10() + Map[a][x][y][z].global_mod + Map[a][x][y][z].orders[0]) * 10
                    b, x1, y1, = order[2]
                    z1 = randint(0, len(Map[b][x1][y1]) - 1)
                    Map[b][x1][y1][z1].hp -= damage
                elif order[1] == "defence":
                    pass
                elif order[1] == "move":
                    unit = Map[a][x][y][z]
                    if Map.place(unit, order[2], unit.side) == 0:
                        Map[a][x][y][z] = None



    "how it should be -- firstly coordinates are handled by Map, then it should be interaction" \
    "Unit objects "
    Map.update()
    return effect


def phase_3(Map):
    """Here data should be (3, 1) or (3, 0). 0 is "continue battle", 1 is "retreat" """
    if DEBUG:
        global i
        data = DATA[i]
        i += 1
    else:
        data = somehow_get(None, 3)
    if data[1][0] != "continue":
        return 0
    else:
        return 1


DATA = eval(((open("scenario.sc")).read()).replace("\n", ""))
fighting = True
Map = mp()
i = 0


phase_1(player=0, Map=Map)
phase_1(player=1, Map=Map)

while fighting:
    prephase_2(player=0, Map=Map)
    prephase_2(player=1, Map=Map)

    phase_2(Map)

    fighting = phase_3(Map)*phase_3(Map)


