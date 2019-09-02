from model.skills import d10, d100, Skill

"""Core stats/Unit construction args (unit_data) should look like dis"""
default = {
    "id": "0",                                  # unit index on the map
    "name": "Default",                          # Just a name of unit
    "hp": 100,                                  # Toughness / health points
    "tp": "Unique",                             # Type of a unit, "unique", "vehicle" and so on. All possible values
                                                # will be described in the unit db (or check the rules in VK)
    "orders": (0, 0, 0),                        # Mods to orders (attack, defence, move)
    "glb": 0,                                   # global modifier to the dices, rolled by a unit
    "specs": (),                                # special skills, they'll be described separately in other file
    "chance": 0,                                # default chance of skills trigger
    "side": 0,                                  # belonging to one of the sides of the battle
    "dead": False,                              # Unit being dead or not. Should be changed during the battle,
                                                # when hp drops below 0, but nobody prohibits spawning corpses)
    "dead_pos": (0, 0),                         # unit death place
}


class Unit:
    ID = 0
    skill_list = eval(((open("engine/model/skills/terra_unification")).read()).replace("\n", ""))
    status_list = eval(((open("engine/model/statuses/terra_unification")).read()).replace("\n", ""))

    def __init__(self, unit_data):
        self.id = Unit.ID                       # core stats
        Unit.ID += 1
        self.name = unit_data['name']
        self.base_hp = unit_data['hp']
        self.type = unit_data['tp']
        self.global_mod = unit_data['glb']
        self.orders = unit_data['orders']
        self.specs = unit_data['specs']
        self.chance = unit_data['chance']

        self.dead_pos = None                    # condition-like stats
        self.dead = False
        self.side = 0
        self.defencing = False
        self.been_attacked_by = []

