from engine.model.unit import Unit
from engine.model.skills import skills, d10, d100


# IDEA: make the preview of actions (it can be premium function)
# kinda the player does some action, the prog calculates the possible result (the amount of damage, kill or not)
# and shows the player before this action is confirmed and sent as an order

def check(data, template):
    return True or False


def somehow_get(something_got_from_server=None, template=0):
    """ guy on server, we need to make connections between
     the fight engine and server, and the server and front """
    if check(something_got_from_server, template):
        return something_got_from_server
    else:
        raise Exception("Incorrect data")


def somehow_send(data_to_send_to_server=None):
    return data_to_send_to_server


def legal(un, coords):
    return True or False


def phase_1(player, Map):
    """here should be player's troops arrangement, like
    (0,
    (
        (<unit_id>, <coords>),
        (<unit_id...);

    this is template 0
    """
    data = somehow_get(None, 0)

    for unit in data[1]:
        if not legal(unit[0], unit[1]):
            somehow_send("Can't place unit(s) there")
            return
        else:
            Map[unit[1]] = unit[0]
    return list


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
    data = somehow_get(None, 1)

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


def phase_2(Map):
    global buffs
    """
    here data should be like
    (2,
        (
            (unit_position, order[, target]),
            ((4, 3, 2), "attack", (1, 3[, 0]))...
        )
    )
    orders keywords -- "attack", "defence", "move", "close_combat"
    """
    data = somehow_get(None, 2)
    effect = []
    for order in data[1]:
        if order[1] == "attack":
            x, y, z = order[0]
            damage = (d10() + Map[x][y][z].orders[0] + buffs[x][y][z])*10

    return effect


def phase_3(Map):
    return list


def apply_orders(q, Map):
    for action in q:
        if action.get("hp"):
            Map[action["unit"]].hp -= action["hp"]
        # etc




fighting = True

action_queue = [[[] for j in range(5)]for i in range(7)] # and inside every cell up to 6 lists of buffs

buffs = []

Map = [[[] for j in range(5)]for i in range(7)]  #  ... make a class Map?
                                                 #  sure, and put all buff stuff inside it

phase_1(player=1, Map=Map)
phase_1(player=2, Map=Map)


while fighting:
    prephase_2(player=1, Map=Map)
    prephase_2(player=2, Map=Map)

    phase_2(Map)

    phase_3(Map)

    data = somehow_get(None, 3)
    if data[1][0] != "continue":
        fighting = False
