# time do jogador
import random

time = {}

# mochila

bag = {"POTION": 10,
       "POKEBALL": 10
}

# efeitos
effects = {"time":{},
           "pokedex": {},
           "duelist": {}

}
# time do oponente
duelist = {}

# ataques

attacks = {"TACKLE":
               {
                   "TYPE": "NORMAL",
                   "POWER": 40,
               },
            "BUG BITE":
               {
                   "TYPE": "BUG",
                   "POWER": 60,
               },
            "STRING SHOT":
               {
                   "TYPE": "BUG",
                   "POWER": 0,
               },
            "GUST":
               {
                   "TYPE": "FLYING",
                   "POWER": 40,
               },
            "QUICK ATTACK":
               {
                   "TYPE": "NORMAL",
                   "POWER": 40,
               },
            "VINE WHIP":
               {
                   "TYPE": "GRASS",
                   "POWER": 45,
               },
            "LEECH SEED":
               {
                   "TYPE": "GRASS",
                   "POWER": 0,
               },
            "POISON POWDER":
               {
                   "TYPE": "POISON",
                   "POWER": 0,
               },
            "DOUBLE KICK":
                {
                    "TYPE": "FIGHTING",
                    "POWER": 30,
                },
            "GROWL":
                {
                    "TYPE": "NORMAL",
                    "POWER": 0,
                },
            "BITE":
                {
                    "TYPE": "DARK",
                    "POWER": 60,
                },
            "MOONBLAST":
                {
                    "TYPE": "FAIRY",
                    "POWER": 95,
                },
            "CHARM":
                {
                    "TYPE": "FAIRY",
                    "POWER": 0,
                },
            "SCRATCH":
                {
                    "TYPE": "NORMAL",
                    "POWER": 40,
                },
            "EMBER":
                {
                    "TYPE": "FIRE",
                    "POWER": 55,
                },
            "DRAGON BREATH":
                {
                    "TYPE": "DRAGON",
                    "POWER": 60,
                },
            "TAIL WHIP":
                {
                    "TYPE": "NORMAL",
                    "POWER": 0,
                },
            "WATER GUN":
                {
                    "TYPE": "WATER",
                    "POWER": 40,
                },
            "WATER PULSE":
                {
                    "TYPE": "WATER",
                    "POWER": 60,
                },
            "AIR SLASH":
                {
                    "TYPE": "FLYING",
                    "POWER": 75,
                },
            "HEADBUTT":
                {
                    "TYPE": "NORMAL",
                    "POWER": 70,
                },
            "AURORA BEAM":
                {
                    "TYPE": "ICE",
                    "POWER": 65,
                },
            "THUNDER FANG":
                {
                    "TYPE": "ELECTRIC",
                    "POWER": 65,
                },
            "FIRE FANG":
                {
                    "TYPE": "FIRE",
                    "POWER": 65,
                },
            "SMOG":
                {
                    "TYPE": "POISON",
                    "POWER": 30,
                },
            "MAGICAL LEAF":
                {
                    "TYPE": "GRASS",
                    "POWER": 60,
                },
            "ICE FANG":
                {
                    "TYPE": "ICE",
                    "POWER": 65,
                },
            "SNOWSCAPE":
                {
                    "TYPE": "ICE",
                    "POWER": 0,
                },
            "THUNDER SHOCK":
                {
                    "TYPE": "ELECTRIC",
                    "POWER": 40,
                },
            "IRON TAIL":
                {
                    "TYPE": "STEEL",
                    "POWER": 100,
                },
            "FURY CUTTER":
                {
                    "TYPE": "BUG",
                    "POWER": 40,
                },
            "BULLET SEED":
                {
                    "TYPE": "GRASS",
                    "POWER": 25,
                },
            "POISON FANG":
                {
                    "TYPE": "POISON",
                    "POWER": 50,
                },
            "BUG BUZZ":
                {
                    "TYPE": "BUG",
                    "POWER": 90,
                },
            "ZEN HEADBUTT":
                {
                    "TYPE": "PSYCHIC",
                    "POWER": 80,
                },
            "CROSS CHOP":
                {
                    "TYPE": "FIGHTING",
                    "POWER": 70,
                },
            "ASSURANCE":
                {
                    "TYPE": "DARK",
                    "POWER": 60,
                },
            "CLOSE COMBAT":
                {
                    "TYPE": "FIGHTING",
                    "POWER": 80,
                },
            "ROCK THROW":
                {
                    "TYPE": "ROCK",
                    "POWER": 50,
                },
            "DEFENSE CURL":
                {
                    "TYPE": "NORMAL",
                    "POWER": 0,
                },
            "EARTHQUAKE":
                {
                    "TYPE": "GROUND",
                    "POWER": 90,
                },
            "HEX":
                {
                    "TYPE": "GHOST",
                    "POWER": 65,
                },
            "DARK PULSE":
                {
                    "TYPE": "DARK",
                    "POWER": 80,
                },
            "LICK":
                {
                    "TYPE": "GHOST",
                    "POWER": 30,
                },
            "STOMPING TANTRUM":
                {
                    "TYPE": "GROUND",
                    "POWER": 75
                },
            "BONE RUSH":
                {
                    "TYPE": "GROUND",
                    "POWER": 25
                },
            "BODY SLAM":
                {
                    "TYPE": "BODY SLAM",
                    "POWER": 85
                },
            "SNORE":
                {
                    "TYPE": "NORMAL",
                    "POWER": 50
                },
            "PSYBEAM":
                {
                    "TYPE": "PSYCHIC",
                    "POWER": 65
                },
            "DISARMING VOICE":
                {
                    "TYPE": "FAIRY",
                    "POWER": 40
                },
            "FLASH CANON":
                {
                    "TYPE": "STEEL",
                    "POWER": 80
                },
            "DRAGON TAIL":
                {
                    "TYPE": "DRAGON",
                    "POWER": 60
                },
            "HYPER BEAM":
                {
                    "TYPE": "NORMAL",
                    "POWER": 100
                },
            "AQUA TAIL":
                {
                    "TYPE": "WATER",
                    "POWER": 70
                },
            "SHADOW BALL":
                {
                    "TYPE": "GHOST",
                    "POWER": 80
                },
            "FIRE PUNCH":
                {
                    "TYPE": "FIRE",
                    "POWER": 75
                },
            "METAL CLAW":
                {
                    "TYPE": "STEEL",
                    "POWER": 50
                },
            "FIERY DANCE":
                {
                    "TYPE": "FIRE",
                    "POWER": 80
                },
            "ICE BEAM":
                {
                    "TYPE": "ICE",
                    "POWER": 90
                },
            "SHADOW CLAW":
                {
                    "TYPE": "GHOST",
                    "POWER": 70
                },
            "PLUCK":
                {
                    "TYPE": "FLYING",
                    "POWER": 60
                },
            "NIGHT SLASH":
                {
                    "TYPE": "DARK",
                    "POWER": 70
                },
}

# pokemons
pokedex = {"BUTTERFREE" :
           {"TYPE" : "BUG",
            "MAX_HEALTH": 60,
            "HEALTH" : 60,
            "ATTACK_POWER" : 45,
            "SPEED" : 70,
            "DEFENSE": 50,
            "ATTACKS" :
                { "TACKLE",
                "BUG BITE",
                "STRING SHOT",
                "GUST",
                },
           },
           "PIDGEY" :
           {"TYPE" : ("NORMAL", "FLYING"),
            "MAX_HEALTH": 83,
            "HEALTH" : 83,
            "ATTACK_POWER" : 80,
            "SPEED" : 101,
            "DEFENSE": 75,
            "ATTACKS" :
                {"TACKLE",
                 "AIR SLASH",
                 "GUST",
                 "QUICK ATTACK",
                },
           },
            "BULBASSAUR":
              {"TYPE": ("GRASS", "POISON"),
               "HEALTH": 80,
               "MAX_HEALTH": 80,
               "ATTACK_POWER": 82,
               "SPEED": 80,
               "DEFENSE": 83,
               "ATTACKS":
               {"TACKLE",
                "VINE WHIP",
                "LEECH SEED",
                "POISON POWDER",
                },
               },
           "WOOLOO":
           {"TYPE": "NORMAL",
            "MAX_HEALTH": 72,
            "HEALTH": 72,
            "ATTACK_POWER": 80,
            "SPEED": 88,
            "DEFENSE": 100,
            "ATTACKS":
                {"TACKLE",
                 "DOUBLE KICK",
                 "GROWL",
                 "HEADBUTT",
                },
           },
           "SYLVEON" :
            {"TYPE": "FAIRY",
             "MAX_HEALTH": 95,
             "HEALTH": 95,
             "ATTACK_POWER": 75,
             "SPEED": 60,
             "DEFENSE": 65,
             "ATTACKS":
                {"BITE",
                 "MOONBLAST",
                 "CHARM",
                 "TACKLE",
                },
            },
            "CHARMANDER":
            {"TYPE": "FIRE",
             "MAX_HEALTH": 78,
             "HEALTH": 78,
             "ATTACK_POWER": 84,
             "SPEED": 100,
             "DEFENSE": 78,
             "ATTACKS":
                {"SCRATCH",
                 "EMBER",
                 "DRAGON BREATH",
                 "GROWL",
                },
            },
            "SQUIRTLE" :
            {"TYPE": "WATER",
             "MAX_HEALTH": 79,
             "HEALTH": 79,
             "ATTACK_POWER": 83,
             "SPEED": 78,
             "DEFENSE": 100,
             "ATTACKS":
                {"TACKLE",
                 "TAIL WHIP",
                 "WATER GUN",
                 "WATER PULSE"
                },
            },
           "VAPOREON":
               {"TYPE": "WATER",
                "MAX_HEALTH": 130,
                "HEALTH": 130,
                "ATTACK_POWER": 75,
                "SPEED": 65,
                "DEFENSE": 60,
                "ATTACKS":
                    {"GROWL",
                     "TACKLE",
                     "AURORA BEAM",
                     "WATER PULSE"
                     },
                },
           "JOLTEON":
               {"TYPE": "ELECTRIC",
                "MAX_HEALTH": 65,
                "HEALTH": 65,
                "ATTACK_POWER": 80,
                "SPEED": 130,
                "DEFENSE": 60,
                "ATTACKS":
                    {"QUICK ATTACK",
                     "BITE",
                     "THUNDER FANG",
                     "GROWL"
                     },
                },
           "FLAREON":
               {"TYPE": "FIRE",
                "MAX_HEALTH": 65,
                "HEALTH": 65,
                "ATTACK_POWER": 110,
                "SPEED": 65,
                "DEFENSE": 60,
                "ATTACKS":
                    {"QUICK ATTACK",
                     "SMOG",
                     "FIRE FANG",
                     "TACKLE"
                     },
                },
           "GLACEON":
               {"TYPE": "ICE",
                "MAX_HEALTH": 65,
                "HEALTH": 65,
                "ATTACK_POWER": 80,
                "SPEED": 65,
                "DEFENSE": 110,
                "ATTACKS":
                    {"CHARM",
                     "ICE FANG",
                     "TACKLE",
                     "SNOWSCAPE"
                     },
                },
           "PIKACHU":
               {"TYPE": "ELECTRIC",
                "MAX_HEALTH": 60,
                "HEALTH": 60,
                "ATTACK_POWER": 90,
                "SPEED": 110,
                "DEFENSE": 55,
                "ATTACKS":
                    {"THUNDER SHOCK",
                     "IRON TAIL",
                     "GROWL",
                     "QUICK ATTACK"
                     },
                },
           "PARAS":
               {"TYPE": ("BUG","GRASS"),
                "MAX_HEALTH": 60,
                "HEALTH": 60,
                "ATTACK_POWER": 80,
                "SPEED": 30,
                "DEFENSE": 80,
                "ATTACKS":
                    {"SCRATCH",
                     "POISON POWDER",
                     "FURY CUTTER",
                     "BULLET SEED"
                     },
                },
           "VENONAT":
               {"TYPE": ("BUG", "POISON"),
                "MAX_HEALTH": 70,
                "HEALTH": 70,
                "ATTACK_POWER": 65,
                "SPEED": 90,
                "DEFENSE": 60,
                "ATTACKS":
                    {"TACKLE",
                     "POISON POWDER",
                     "POISON FANG",
                     "BUG BUZZ"
                     },
                },
           "PSYDUCK":
               {"TYPE": "WATER",
                "MAX_HEALTH": 80,
                "HEALTH": 80,
                "ATTACK_POWER": 82,
                "SPEED": 85,
                "DEFENSE": 78,
                "ATTACKS":
                    {"WATER GUN",
                     "TAIL WHIP",
                     "ZEN HEADBUTT",
                     "WATER PULSE"
                     },
                },
           "MANKEY":
               {"TYPE": "FIGHTING",
                "MAX_HEALTH": 65,
                "HEALTH": 65,
                "ATTACK_POWER": 105,
                "SPEED": 95,
                "DEFENSE": 60,
                "ATTACKS":
                    {"SCRATCH",
                     "CROSS CHOP",
                     "ASSURANCE",
                     "CLOSE COMBAT"
                     },
                },
           "GEODUDE":
               {"TYPE": ("ROCK", "GROUND"),
                "MAX_HEALTH": 80,
                "HEALTH": 80,
                "ATTACK_POWER": 90,
                "SPEED": 45,
                "DEFENSE": 130,
                "ATTACKS":
                    {"DEFENSE CURL",
                     "TACKLE",
                     "ROCK THROW",
                     "EARTHQUAKE"
                     },
                },
           "GENGAR":
               {"TYPE": ("GHOST", "POISON"),
                "MAX_HEALTH": 60,
                "HEALTH": 60,
                "ATTACK_POWER": 75,
                "SPEED": 110,
                "DEFENSE": 60,
                "ATTACKS":
                    {"HEX",
                     "SMOG",
                     "DARK PULSE",
                     "SHADOW BALL"
                     },
                },
           "CUBONE":
               {"TYPE": "GROUND",
                "MAX_HEALTH": 60,
                "HEALTH": 60,
                "ATTACK_POWER": 80,
                "SPEED": 45,
                "DEFENSE": 110,
                "ATTACKS":
                    {"GROWL",
                     "HEADBUTT",
                     "BONE RUSH",
                     "STOMPING TANTRUM"
                     },
                },
           "SNORLAX":
               {"TYPE": "NORMAL",
                "MAX_HEALTH": 140,
                "HEALTH": 140,
                "ATTACK_POWER": 70,
                "SPEED": 30,
                "DEFENSE": 65,
                "ATTACKS":
                    {"TACKLE",
                     "BODY SLAM",
                     "SNORE",
                     "DEFENSE CURL"
                     },
                },
           "ESPEON":
               {"TYPE": "PSYCHIC",
                "MAX_HEALTH": 65,
                "HEALTH": 65,
                "ATTACK_POWER": 80,
                "SPEED": 110,
                "DEFENSE": 60,
                "ATTACKS":
                    {"CHARM",
                     "PSYBEAM",
                     "TACKLE",
                     "GROWL"
                     },
                },
           "UMBREON":
               {"TYPE": "DARK",
                "MAX_HEALTH": 95,
                "HEALTH": 95,
                "ATTACK_POWER": 65,
                "SPEED": 65,
                "DEFENSE": 110,
                "ATTACKS":
                    {"BITE",
                     "DARK PULSE",
                     "TACKLE",
                     "TAIL WHIP"
                     },
                },
           "GARDEVOIR":
               {"TYPE": ("PSYCHIC", "FAIRY"),
                "MAX_HEALTH": 68,
                "HEALTH": 68,
                "ATTACK_POWER": 75,
                "SPEED": 80,
                "DEFENSE": 65,
                "ATTACKS":
                    {"CHARM",
                     "DISARMING VOICE",
                     "PSYBEAM",
                     "MOONBLAST"
                     },
                },
           "MELTAN":
               {"TYPE": "STEEL",
                "MAX_HEALTH": 66,
                "HEALTH": 66,
                "ATTACK_POWER": 65,
                "SPEED": 34,
                "DEFENSE": 65,
                "ATTACKS":
                    {"TUNDER SHOCK",
                     "DEFENSE CURL",
                     "TAIL WHIP",
                     "FLASH CANON"
                     },
                },
           "DRAGONITE":
               {"TYPE": "DRAGON",
                "MAX_HEALTH": 91,
                "HEALTH": 91,
                "ATTACK_POWER": 120,
                "SPEED": 80,
                "DEFENSE": 95,
                "ATTACKS":
                    {"DRAGON TAIL",
                     "HYPER BEAM",
                     "AQUA TAIL",
                     "FIRE PUNCH"
                     },
                },
           "LUCARIO":
               {"TYPE": ("FIGHTING", "STEEL"),
                "MAX_HEALTH": 70,
                "HEALTH": 70,
                "ATTACK_POWER": 110,
                "SPEED": 90,
                "DEFENSE": 70,
                "ATTACKS":
                    {"QUICK ATTACK",
                     "METAL CLAW",
                     "CLOSE COMBAT",
                     "BODY SLAM"
                     },
                },
           "VOLCARONA":
               {"TYPE": ("BUG", "FIRE"),
                "MAX_HEALTH": 85,
                "HEALTH": 85,
                "ATTACK_POWER": 60,
                "SPEED": 100,
                "DEFENSE": 65,
                "ATTACKS":
                    {"FIERY DANCE",
                     "GUST",
                     "STRING SHOT",
                     "ICE BEAM"
                     },
                },
           "MIMIKYU":
               {"TYPE": ("GHOST", "FAIRY"),
                "MAX_HEALTH": 55,
                "HEALTH": 55,
                "ATTACK_POWER": 90,
                "SPEED": 96,
                "DEFENSE": 80,
                "ATTACKS":
                    {"SCRATCH",
                     "CHARM",
                     "SHADOW CLAW",
                     "HEX"
                     },
                },
           "SPRIGATITO":
               {"TYPE": "GRASS",
                "MAX_HEALTH": 76,
                "HEALTH": 76,
                "ATTACK_POWER": 110,
                "SPEED": 123,
                "DEFENSE": 70,
                "ATTACKS":
                    {"BITE",
                     "TAIL WHIP",
                     "MAGICAL LEAF",
                     "SCRATCH"
                     },
                },
           "ALTARIA":
               {"TYPE": ("DRAGON", "FLYING"),
                "MAX_HEALTH": 75,
                "HEALTH": 75,
                "ATTACK_POWER": 70,
                "SPEED": 80,
                "DEFENSE": 90,
                "ATTACKS":
                    {"DISARMING VOICE",
                     "GROWL",
                     "PLUCK",
                     "DRAGON BREATH"
                     },
                },
           "FROAKIE":
               {"TYPE": ("WATER", "DARK"),
                "MAX_HEALTH": 72,
                "HEALTH": 72,
                "ATTACK_POWER": 95,
                "SPEED": 122,
                "DEFENSE": 67,
                "ATTACKS":
                    {"WATER PULSE",
                     "NIGHT SLASH",
                     "LICK",
                     "ICE BEAM"
                     },
                },
           }

# tipos

tipos = {"NORMAL":
             {  "NORMAL": 1,
                "FIRE": 1,
                "WATER": 1,
                "ELECTRIC": 1,
                "GRASS": 1,
                "ICE": 1,
                "FIGHTING": 1,
                "POISON": 1,
                "GROUND": 1,
                "FLYING": 1,
                "PSYCHIC": 1,
                "BUG": 1,
                "ROCK": 0.5,
                "GHOST": 0,
                "DRAGON": 1,
                "DARK": 1,
                "STEEL": 0.5,
                "FAIRY": 1,
             },
        "FIRE":
             { "NORMAL": 1,
                "FIRE": 0.5,
                "WATER": 0.5,
                "ELECTRIC": 1,
                "GRASS": 2,
                "ICE": 2,
                "FIGHTING": 1,
                "POISON": 1,
                "GROUND": 1,
                "FLYING": 1,
                "PSYCHIC": 1,
                "BUG": 2,
                "ROCK": 0.5,
                "GHOST": 1,
                "DRAGON": 0.5,
                "DARK": 1,
                "STEEL": 2,
                "FAIRY": 1,
            },
        "WATER":
             {"NORMAL": 1,
                "FIRE": 2,
                "WATER": 0.5,
                "ELECTRIC": 1,
                "GRASS": 0.5,
                "ICE": 1,
                "FIGHTING": 1,
                "POISON": 1,
                "GROUND": 2,
                "FLYING": 1,
                "PSYCHIC": 1,
                "BUG": 1,
                "ROCK": 2,
                "GHOST": 1,
                "DRAGON": 0.5,
                "DARK": 1,
                "STEEL": 1,
                "FAIRY": 1,
                },
        "ELECTRIC":
            {"NORMAL": 1,
            "FIRE": 1,
            "WATER": 2,
            "ELECTRIC": 0.5,
            "GRASS": 0.5,
            "ICE": 1,
            "FIGHTING": 1,
            "POISON": 1,
            "GROUND": 0,
            "FLYING": 2,
            "PSYCHIC": 1,
            "BUG": 1,
            "ROCK": 1,
            "GHOST": 1,
            "DRAGON": 0.5,
            "DARK": 1,
            "STEEL": 1,
            "FAIRY": 1,
            },
        "GRASS":
            {"NORMAL": 1,
            "FIRE": 0.5,
            "WATER": 2,
            "ELECTRIC": 0,
            "GRASS": 0.5,
            "ICE": 1,
            "FIGHTING": 1,
            "POISON": 0.5,
            "GROUND": 2,
            "FLYING": 0.5,
            "PSYCHIC": 1,
            "BUG": 0.5,
            "ROCK": 2,
            "GHOST": 1,
            "DRAGON": 0.5,
            "DARK": 1,
            "STEEL": 0.5,
            "FAIRY": 1,
            },
        "ICE":
            {"NORMAL": 1,
            "FIRE": 0.5,
            "WATER": 0.5,
            "ELECTRIC":1,
            "GRASS": 2,
            "ICE": 0.5,
            "FIGHTING": 1,
            "POISON": 1,
            "GROUND": 2,
            "FLYING": 2,
            "PSYCHIC": 1,
            "BUG": 1,
            "ROCK": 1,
            "GHOST": 1,
            "DRAGON": 2,
            "DARK": 1,
            "STEEL": 0.5,
            "FAIRY": 1,
            },
        "FIGHTING":
            {"NORMAL": 2,
            "FIRE": 1,
            "WATER": 1,
            "ELECTRIC": 1,
            "GRASS": 1,
            "ICE": 2,
            "FIGHTING": 1,
            "POISON": 0.5,
            "GROUND": 1,
            "FLYING": 0.5,
            "PSYCHIC": 0.5,
            "BUG": 0.5,
            "ROCK": 2,
            "GHOST": 0,
            "DRAGON": 1,
            "DARK": 2,
            "STEEL": 2,
            "FAIRY": 0.5,
            },
        "POISON":
            {"NORMAL": 1,
            "FIRE": 1,
            "WATER": 1,
            "ELECTRIC": 1,
            "GRASS": 2,
            "ICE": 1,
            "FIGHTING": 1,
            "POISON":0.5,
            "GROUND": 0.5,
            "FLYING": 1,
            "PSYCHIC": 1,
            "BUG": 1,
            "ROCK": 0.5,
            "GHOST": 0.5,
            "DRAGON": 1,
            "DARK": 1,
            "STEEL": 0,
            "FAIRY": 2,
            },
        "GROUND":
            {"NORMAL": 1,
            "FIRE": 2,
            "WATER": 1,
            "ELECTRIC": 2,
            "GRASS": 0.5,
            "ICE": 1,
            "FIGHTING": 1,
            "POISON": 2,
            "GROUND": 1,
            "FLYING": 0,
            "PSYCHIC": 1,
            "BUG": 0.5,
            "ROCK": 2,
            "GHOST": 1,
            "DRAGON": 1,
            "DARK": 1,
            "STEEL": 2,
            "FAIRY": 1,
            },
        "FLYING":
            {"NORMAL": 1,
            "FIRE": 1,
            "WATER": 1,
            "ELECTRIC": 0.5,
            "GRASS": 2,
            "ICE": 1,
            "FIGHTING": 2,
            "POISON": 1,
            "GROUND": 1,
            "FLYING": 1,
            "PSYCHIC": 1,
            "BUG": 2,
            "ROCK": 0.5,
            "GHOST": 1,
            "DRAGON": 1,
            "DARK": 1,
            "STEEL": 0.5,
            "FAIRY": 1,
            },
        "PSYCHIC":
            {"NORMAL": 1,
            "FIRE": 1,
            "WATER": 1,
            "ELECTRIC": 1,
            "GRASS": 1,
            "ICE": 1,
            "FIGHTING": 2,
            "POISON": 2,
            "GROUND": 1,
            "FLYING": 1,
            "PSYCHIC": 0.5,
            "BUG": 1,
            "ROCK": 1,
            "GHOST": 1,
            "DRAGON": 1,
            "DARK": 0,
            "STEEL": 0.5,
            "FAIRY": 1,
            },
        "BUG":
            {"NORMAL": 1,
            "FIRE": 0.5,
            "WATER": 1,
            "ELECTRIC": 1,
            "GRASS": 2,
            "ICE": 1,
            "FIGHTING": 0.5,
            "POISON": 0.5,
            "GROUND": 1,
            "FLYING":0.5,
            "PSYCHIC": 2,
            "BUG": 1,
            "ROCK": 1,
            "GHOST": 0.5,
            "DRAGON": 1,
            "DARK": 2,
            "STEEL": 0.5,
            "FAIRY": 0.5,
            },
        "ROCK":
            {"NORMAL": 1,
            "FIRE": 2,
            "WATER": 1,
            "ELECTRIC": 1,
            "GRASS": 1,
            "ICE": 2,
            "FIGHTING": 0.5,
            "POISON": 1,
            "GROUND": 0.5,
            "FLYING": 2,
            "PSYCHIC": 1,
            "BUG": 2,
            "ROCK": 1,
            "GHOST": 1,
            "DRAGON": 1,
            "DARK": 1,
            "STEEL": 0.5,
            "FAIRY": 1,
            },
        "GHOST":
            {"NORMAL": 0,
            "FIRE": 1,
            "WATER": 1,
            "ELECTRIC": 1,
            "GRASS": 1,
            "ICE": 1,
            "FIGHTING": 1,
            "POISON": 1,
            "GROUND": 1,
            "FLYING": 1,
            "PSYCHIC": 2,
            "BUG": 1,
            "ROCK": 1,
            "GHOST": 2,
            "DRAGON": 1,
            "DARK": 0.5,
            "STEEL": 1,
            "FAIRY": 1,
            },
        "DRAGON":
            {"NORMAL": 1,
            "FIRE": 1,
            "WATER": 1,
            "ELECTRIC": 1,
            "GRASS": 1,
            "ICE": 1,
            "FIGHTING": 1,
            "POISON": 1,
            "GROUND": 1,
            "FLYING": 1,
            "PSYCHIC": 1,
            "BUG": 1,
            "ROCK": 1,
            "GHOST": 1,
            "DRAGON": 2,
            "DARK": 1,
            "STEEL": 0.5,
            "FAIRY": 0,
            },
        "DARK":
            {"NORMAL": 1,
            "FIRE": 1,
            "WATER": 1,
            "ELECTRIC": 1,
            "GRASS": 1,
            "ICE": 1,
            "FIGHTING": 0.5,
            "POISON": 1,
            "GROUND": 1,
            "FLYING": 1,
            "PSYCHIC": 2,
            "BUG": 1,
            "ROCK": 1,
            "GHOST": 2,
            "DRAGON": 1,
            "DARK": 0.5,
            "STEEL": 1,
            "FAIRY": 0.5,
            },
        "STEEL":
            {"NORMAL": 1,
            "FIRE": 0.5,
            "WATER": 0.5,
            "ELECTRIC": 0.5,
            "GRASS": 1,
            "ICE": 2,
            "FIGHTING": 1,
            "POISON": 1,
            "GROUND": 1,
            "FLYING": 1,
            "PSYCHIC": 1,
            "BUG": 1,
            "ROCK": 2,
            "GHOST": 1,
            "DRAGON": 1,
            "DARK": 1,
            "STEEL": 0.5,
            "FAIRY": 2,
            },
        "FAIRY":
            {"NORMAL": 1,
            "FIRE": 0.5,
            "WATER": 1,
            "ELECTRIC": 1,
            "GRASS": 1,
            "ICE": 1,
            "FIGHTING": 2,
            "POISON": 0.5,
            "GROUND": 1,
            "FLYING": 1,
            "PSYCHIC": 1,
            "BUG": 1,
            "ROCK": 1,
            "GHOST": 1,
            "DRAGON": 2,
            "DARK": 2,
            "STEEL": 0.5,
            "FAIRY": 1,
            },

}