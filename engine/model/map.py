


class Map(object):
    obj = None

    def __new__(cls, *args, **kwargs):
        if cls.obj is None:
            cls.obj = object.__new__(cls)
        return cls.obj

    def __init__(self):
        self.map = [None]                                           #  Titan place for Player 1
        self.map.append([[], [], [], [], []])                       #  place for aviation Player 1
        self.map.append([[] for j in range(5)] for i in range(5))   #  Battlefield
        self.map.append([[], [], [], [], []])                       #  place for aviation Player 2
        self.map.append(None)                                       #  Titan place for Player 2

        self.buff_stack = []    #  [(buff_id, dependencies), ..  There will be all buffs wth lifetime
                                #  dependencies should be (lifetime, [unit, unit...])

    def __getitem__(self, item):
        return self.map[item]

    "Validates if placement of unit is correct"
    def validate(self, unit, coords):
        if len(coords) < 1:
            return "Invalid format"

        if unit.type == "Titan":
            if not(unit.side == 0 and coords[0] == 0 or unit.side == 2 and coords[0] == 4):
                return "Invalid placement"
            elif not(self[coords[0]] is None):
                return "Cell is already full"
            else:
                return 0

        if len(coords) < 2:
            return "Invalid format"

        if unit.type == "Aviation":
            if unit.side == 0 and coords[0] == 1 and 0 <= coords[1] <= 5:
                if not(self[1][coords[1]] is None):
                    return "Cell is already full"
                else:
                    return 0
            elif unit.side == 1 and coords[0] == 3 and 0 <= coords[1] <= 5:
                if not (self[3][coords[1]] is None):
                    return "Cell is already full"
                else:
                    return 0
            else:
                return "Invalid placement"

        if len(coords) < 3:
            return "Invalid format"

        if coords[0] != 2 or 0 <= coords[1] <= 5 or 0 <= coords[2] <= 5:
            return "Invalid placement"
        elif len(self[coords[0]][coords[1]][coords[2]]) > 5:
            return "Cell is already full"
        else:
            return 0

    "Recalculates all the buffs"
    def update_buffs(self):
        pass

    "Applying movements and death"
    def update(self):
        pass



