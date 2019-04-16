"""Here be skill list """
from random import randint


d10 = lambda: randint(1, 10)
d100 = lambda: randint(1, 100)


def Chronometron(data, MAP):
    """data for this skill should be like dis
    {
        'target': (4, 3), # target cell
        'side': 2,        # affected side
        'action' 0        # buff/debuff
    }
    """
    action = data['action']  # 0 if buffing own troops, 1 -- debuffing opponents

    for unit in MAP[data['target'][0], data['target'][1]]:
        if unit.side == data["side"]:
            if action:
                unit.glb += 1
            else:
                unit.glb -= 1

    if data['target'][0] < 6:
        for unit in MAP[data['target'][0] + 1, data['target'][1]]:
            if unit.side == data["side"]:
                if action:
                    unit.glb += 1
                else:
                    unit.glb -= 1

    if data['target'][1] < 6:
        for unit in MAP[data['target'][0], data['target'][1] + 1]:
            if unit.side == data["side"]:
                if action:
                    unit.glb += 1
                else:
                    unit.glb -= 1

    if data['target'][0] > 1:
        for unit in MAP[data['target'][0] - 1, data['target'][1]]:
            if unit.side == data["side"]:
                if action:
                    unit.glb += 1
                else:
                    unit.glb -= 1

    if data['target'][1] > 1:
        for unit in MAP[data['target'][0], data['target'][1] - 1]:
            if unit.side == data["side"]:
                if action:
                    unit.glb += 1
                else:
                    unit.glb -= 1


def Moleculary_griefing(data, Map):
    """data for this skill should be like dis
        {
            'target': (4, 3), # target cell
            'side': 2,        # affected side
            'action' 0        # buff/debuff
        }
        """
    effect = 9*d10()
    if len(data['target']) == 3:
        if Map[data['target']].side == data['side']:
            if data['action'] == 0:
                Map[data['target']].hp += effect
            else:
                Map[data['target']].hp -= effect
    else:
        for unit in Map[data['target'][0], data['target'][1]]:
            if unit.side == data["side"]:
                if data['action']:
                    Map[data['target']].hp += effect
                else:
                    Map[data['target']].hp -= effect


def Technomancing(data, Map):
    """data for this skill should be like dis
            {
                'target': (4, 3), # target cell
                'side': 2,        # casting side
            }
            """
    for unit in Map[data['target'][0], data['target'][1]]:
        if unit.side != data["side"]:
            if unit.type == "vehicle":
                if d10() < 6:
                    if d10() < 6:
                        unit.side = data['side']
                        """manipulations with player control changing"""
                    else:
                        unit.hp -= unit.hp


def caucasus_psykers(data, Map):
    """data for this skill should be like dis
                {
                    'Unit': Unit object # caster
                }
            """
    pass


def prophecy(data, Map):
    """data for this skill should be like dis
                    {
                        'Unit': Unit object # caster
                    }
                """
    pass


def biomancy(data, Map):
    """data for this skill should be like dis
                    {
                        'Unit': Unit object # caster
                    }
                """
    pass


def telepatics(data, Map):
    """data for this skill should be like dis
                    {
                        'Unit': Unit object # caster
                    }
                """
    pass


def explosion(data, Map):
    """data for this skill should be like dis
                    {
                        'Unit': Unit object # caster
                    }
                """
    pass


def prepared_defence(data, Map):
    """data for this skill should be like dis
                    {
                        'Unit': Unit object # caster
                    }
                """
    pass


def fire_support(data, Map):
    """data for this skill should be like dis
                    {
                        'Unit': Unit object # caster
                    }
                """
    pass


def defence_mode(data, Map):
    """data for this skill should be like dis
                    {
                        'Unit': Unit object # caster
                    }
                """
    pass


def relocation(data, Map):
    """data for this skill should be like dis
                    {
                        'Unit': Unit object # caster
                    }
                """
    pass


def exterminate(data, Map):
    """data for this skill should be like dis
                    {
                        'Unit': Unit object # caster
                    }
                """
    pass


'''all EMPRAH's passive skills and weapons should be built in its model, there are too of them and not usable'''
#  todo split this shit to "reaction" "passive" and "castable"


skills = {
    "0": Chronometron,
    "1": Moleculary_griefing,
    "2": Technomancing,
    "3": caucasus_psykers,
}
