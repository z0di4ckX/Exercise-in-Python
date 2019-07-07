from sys import exit
from random import randint

class Scence(object):
    def enter(self):
        print("This scene is not yet configured. Subclass it and implement enter().")
        exit(1)

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map
    def play(self):
        current_scene = self.scene_map.opening_scene()
        while True:
            print("\n---------")
            next_scene_name = current_scene.enter()

class Death(Scence):
    quips = [
            "You died. You kinda suck at this.",
            "Your mom would be proud... if she were smarter.",
            "Such a luser.",
            "I have a small pupp that's better at this."
        ]
    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scence):
    def enter(self):
        print("The Gothons fo Plante Percal #25 have invaded your ship and destroyed")
        print("your entire crew. You are the last surviving member and your last")
        print("mission is to get the neutron destruct bomb from the Weapons Armory,")
        print("put it in the bridge, and blow the ship up after getting into an")
        print("escape pod.")
        print("\n")
        print("You're running  down the central corridor to the Weapons Armory when")
        print("a Gothons jumps out, red scaly skin, dark grimy teeth, and evil clown costume")
        print("flowing around his hate filled body. He's blocking the door to the")
        print("Armory and about to pull a weapon to blast you.")

        action = input()

        if action == "shoot!":
            print("Quick on the draw you yank out your blaster and fire it at the Gothons")

class LaserWeaponArmory(Scence):
    def enter(self):
        pass

class TheBridge(Scence):
    def enter(self):
        pass

class EscapePod(Scence):
    def enter(self):
        pass

class Map(object):
    def __init__(self, strat_scene):
        pass
    def next_scene(self, scene_name):
        pass
    def opening_scene(self):
        pass

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()