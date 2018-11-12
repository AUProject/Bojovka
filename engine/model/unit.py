"""Unit construction args (unit_data) should look like dis"""
default = {
    "name": "Default",              # Just a name of unit
    "hp": 100,                      # Toughness / health points
    "tp": "Unique",                 # Type of a unit, "unique", "vehicle" and so on. All possible values will be
                                    # described in the unit db (or check the rules in VK)
    "orders": (0, 0, 0),            # Mods to orders
    "feats": (0, 0, 0, 0, 0, 0),    # Features like "landing", "ambush" and so on in order as they are in core rules
    "glb": 0,                       # global modifier to the dices, rolled by a unit
    "specs": (),                    # special skills, they'll be described separately in other file
   #"pos": (0, 0),                  # position of the unit
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
        self.pos = None             # unit_data['pos'] # TODO should it be a map attr or an unit's?


