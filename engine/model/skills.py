from random import randint

d10 = lambda: randint(1, 10)
d100 = lambda: randint(1, 100)


class Skill:
    def __init__(self, skilldata):
        self.keywords = skilldata
        self.target = None
        self.effect = None
        self.range = None

    def __call__(self, *args, **kwargs):
        pass

    #  skills with keyword damage should include dm: multiplicative damage modifier
