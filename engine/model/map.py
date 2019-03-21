from engine.model.unit import Unit


class Map(object):
    DEBUG = True
    if DEBUG:
        unit_list = eval(((open("engine/model/model")).read()).replace("\n", ""))
    obj = None

    def __new__(cls, *args, **kwargs):
        if cls.obj is None:
            cls.obj = object.__new__(cls)
        return cls.obj

    def __init__(self):
        self.map = [None]                                             #  Titan place for Player 1
        self.map.append([[None], [None], [None], [None], [None]])     #  place for aviation Player 1
        self.map.append([[[] for j in range(5)] for i in range(5)])   #  Battlefield
        self.map.append([[None], [None], [None], [None], [None]])     #  place for aviation Player 2
        self.map.append(None)                                         #  Titan place for Player 2

        self.buff_stack = []    #  [(buff_id, dependencies), ..  There will be all buffs wth lifetime
                                #  dependencies should be (lifetime, [unit, unit...])
        self.dead = []
        self.descent = []
        self.concealed = []
        self.all = {}

    def __getitem__(self, item):
        return self.map[item]

    def __setitem__(self, key, value):
        self.map[key] = value

    "Validates if placement of unit is correct"
    def validate(self, unit, coords):
        if len(coords) < 1:
            return "Invalid format"
        if type(unit) != Unit:
            unit = Unit(self.__class__.unit_list[unit])
        if unit.type == "titan":
            if not(unit.side == 0 and coords[0] == 0 or unit.side == 2 and coords[0] == 4):
                return "Invalid placement"
            elif not(self[coords[0]] is None):
                return "Cell is already full"
            else:
                return 0

        if len(coords) < 2:
            return "Invalid format"

        if unit.type == "aviation":
            if unit.side == 0 and coords[0] == 1 and 0 <= coords[1] <= 4:
                if not(self[1][coords[1]] is None):
                    return "Cell is already full"
                else:
                    return 0
            elif unit.side == 1 and coords[0] == 3 and 0 <= coords[1] <= 4:
                if not (self[3][coords[1]] is None):
                    return "Cell is already full"
                else:
                    return 0
            else:
                return "Invalid placement"

        if len(coords) < 3:
            return "Invalid format"

        if coords[0] != 2 or not(0 <= coords[1] <= 4) or not(0 <= coords[2] <= 4):
            return "Invalid placement"
        elif len(self[coords[0]][coords[1]][coords[2]]) > 5:
            return "Cell is already full"
        else:
            return 0

    def place(self, unit, coords, player):
        if self.check(unit):
            unit = Unit(self.__class__.unit_list[unit])
            unit.side = player
        response = self.validate(unit, coords)
        if response != 0:
            return "Cannot place, " + response
        else:
            unit.pos = coords
            if unit.type == "titan":
                self[coords[0]].append(unit)
            elif unit.type == "aviation":
                self[coords[0]][coords[1]].append(unit)
            else:
                self[coords[0]][coords[1]][coords[2]].append(unit)
            return 0

    def simple_check(self, coords):
        try:
            if len(coords) == 1:
                if type(self[coords[0]]) == Unit:
                    return True
            elif len(coords) == 2:
                if type(self[coords[0]][coords[1]]) == Unit:
                    return True
            elif len(coords) == 3:
                if len(self[coords[0]][coords[1]][coords[2]]) > 0:
                    return True
            elif len(coords) == 4:
                if type(self[coords[0]][coords[1]][coords[2]][coords[3]]) == Unit:
                    return True
            else:
                raise IndexError
        except IndexError:
            return False

    @staticmethod
    def check(unit):
        if type(unit) != Unit:
            return 1
        else:
            return 0

    "Recalculating buffs and applying deaths"
    def update(self):
        if not self.check(self[0]):
            if self[0].hp <= 0:
                self[0].dead = True
                self.dead.append(self[0])
                self[0] = None
        if not self.check(self[4]):
            if self[4].hp <= 0:
                self[4].dead = True
                self.dead.append(self[4])
                self[4] = None
        for i in range(5):
            if not self.check(self[1][i]):
                if self[1][i].hp <= 0:
                    self[1][i].dead = True
                    self.dead.append(self[1][i])
                    self[1][i] = None
            if not self.check(self[3][i]):
                if self[3][i].hp <= 0:
                    self[3][i].dead = True
                    self.dead.append(self[3][i])
                    self[1][i] = None
            for j in range(5):
                for k in range(len(self[2][i][j]) - 1, -1, -1):
                    if self[2][i][j][k] is None:
                        self[2][i][j].pop(k)
                    elif self[2][i][j][k].hp <= 0:
                        self[2][i][j][k].dead = True
                        self.dead.append(self[2][i][j][k])
                        self[2][i][j].pop(k)
        return 0

    def gay_detector(self, unit, target_side=-1):
        gay_order = (
            (0, 0),
            (1, 0),
            (1, 1),
            (0, 1),
            (-1, 1),
            (-1, 0),
            (-1, -1),
            (0, -1),
            (1, -1),
            (2, 0),
            (0, 2),
            (-2, 0),
            (0, -2),
        )
        gay_list = []
        coords = unit.pos
        for i in gay_order:
            i_coords = (coords[0], coords[1] + i[0], coords[2] + i[1])
            inside_the_field = (0 <= i_coords[1] <= 4) and (0 <= i_coords[2] <= 4)
            if self.simple_check(i_coords) and inside_the_field:
                for j in self[i_coords[0]][i_coords[1]][i_coords[2]]:
                    if target_side == -1 or j.side == target_side:
                        gay_list.append(j)
        return gay_list

