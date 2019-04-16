from engine.model.skills import  d10, d100


"""Unit construction args (unit_data) should look like dis"""
default = {
    "id": "0",                      # id of ubit model in db (model file)
    "name": "Default",              # Just a name of unit
    "hp": 100,                      # Toughness / health points
    "tp": "Unique",                 # Type of a unit, "unique", "vehicle" and so on. All possible values will be
                                    # described in the unit db (or check the rules in VK)
    "orders": (0, 0, 0),            # Mods to orders (attack, defence, move)
    "feats": (0, 0, 0, 0, 0, 0),    # Features like "landing", "ambush" and so on in order as they are in core rules
    "glb": 0,                       # global modifier to the dices, rolled by a unit
    "specs": (),                    # special skills, they'll be described separately in other file
    "chance": 0,                    # chance of skills trigger
    "side": 0,                      # belonging to one of the sides of the battle
    "dead": False,                  # Unit being dead or not. Should be changed during the battle, when hp drops below 0
                                    # but nobody prohibits spawning corpses)
    "pos": (0, 0),                  # position of the unit
    "dr": 0,                        # damage reducing rises to 0.5 when executing defence order or is affected otherwise
}


class Unit:

    def __init__(self, unit_data):
        self.name = unit_data['name']
        self.hp = unit_data['hp']
        self.type = unit_data['tp']
        self.global_mod = unit_data['glb']
        self.feats = unit_data['feats']
        self.orders = unit_data['orders']
        self.specs = unit_data['specs']
        self.pos = None             # unit_data['pos'] : should it be a map attr or an unit's? Both.
        #  self.chance = unit_data['chance']
        #  TODO refactor this mess of stats
        self.dead = False
        self.dr = 0
        self.side = 0
        self.buffs = []
        self.defencing = False
        self.been_attacked_by = []
        self.succ_of_last_cast = False

    def attack(self, target):
        if self.type != "titan" and self.type != "aviation":
            damage = (d10() + self.global_mod + self.orders[0])*10
            if len(target) == 3:
                if len(self[target[0]][target[1]][target[2]]) > 0:
                    return True
            elif len(target) == 4:
                if type(self[target[0]][target[1]][target[2]][target[3]]) == Unit:
                    return True
                    pass

        return 0

    def update(self):
        if self.hp <= 0:
            self.dead = True
            self.hp = 0
            self.defencing = False
            return -1
        self.been_attacked_by = []

