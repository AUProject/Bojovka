d = {
    "name": "",
    "keywords": {"attack_order", "move_order", "defence_order", "trigger", "activation", "diversion", "warp", "range"},
    "aoe": {"unit", "cell", "column", "row", "all", "range"},
    "conditions": {
        "stat_is": {
            "hp": ("greater", 50)
        },
        "status": {
            "stun"   : 1,
            "frank"  : 0,
        },
        "cast_chance": "auto"
    },
    "effect": {
        "power": 3,             #dice multiplier
        "effect_to_enemy": ["damage", "heal", "exterminate", "revive", "*status0*", "*status2*", ],
        "effect_to_friend": ["damage", "heal", "exterminate", "revive", "*status0*", "*status2*", ],
        },
}
dd = [
    {
    "name": "Spess Mehreen",
    "hp": 230,
    "tp": "infantry",
    "orders": (0, 0, 0),
    "feats": (0, 1, 0, 0, 0, 0),
    "glb": 0,
    "specs": (),
    },
    {
    "name": "Terminators",
    "hp": 290,
    "tp": "infantry",
    "orders": (1, 1, 1),
    "feats": (0, 1, 0, 0, 0, 0),
    "glb": 0,
    "specs": (),
    },
    {
    "name": "Cryptec",
    "hp": 230,
    "tp": "Unique",
    "orders": (0, 0, 0),
    "feats": (0, 0, 0, 0, 0, 0),
    "glb": 1,
    "specs": (0, 1, 2),
    }
]
