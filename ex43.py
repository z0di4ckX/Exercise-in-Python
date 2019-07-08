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
            current_scene = self.scene_map.next_scene(next_scene_name)

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
        print("The Gothon's fo Plante Percal #25 have invaded your ship and destroyed")
        print("your entire crew. You are the last surviving member and your last")
        print("mission is to get the neutron destruct bomb from the Weapons Armory,")
        print("put it in the bridge, and blow the ship up after getting into an")
        print("escape pod.")
        print("\n")
        print("You're running  down the central corridor to the Weapons Armory when")
        print("a Gothon's jumps out, red scaly skin, dark grimy teeth, and evil clown costume")
        print("flowing around his hate filled body. He's blocking the door to the")
        print("Armory and about to pull a weapon to blast you.")

        action = input()

        if action == "shoot!":
            print("Quick on the draw you yank out your blaster and fire it at the Gothon's")
            print("His clown costume is flowing and moving around his body, which throws")
            print("off your aim. Your laser hits his costume but misses him entirely. This")
            print("completely ruins his brand new costume his mother bought him, which")
            print("make him fly into a rage and blast you repeatedly in the face until")
            print("you are dead. The he eats you.")
            return("death")

        elif action == "dodge!":
            print("Like a world class boxer you dodge, weave, slip and slide right")
            print("as the Gothon's blaster cranks a laser past your head.")
            print("In the middle of you artful dodge your foot slips and you")
            print("bang your head on the metal wall and pass out.")
            print("You wake up shortly after only to die as the Gothon stomps on")
            print("your head and eats you.")
            return("death")
        
        elif action == "tell a joke":
            print("Lucky for you they made you learn Gothon insults in the academy.")
            print("You tell the one Gothon joke you know:")
            print("Lbhe zbguer vf fb sng, jura fu fvg nebhaq gur ubhfr, fur fvgf nebhaq gur ubhff.")
            print("The Gothon stops, tries not to laugh, then busts out laughing and can't move.")
            print("While he's laughing you run up and shoot him square in the head")
            print("putting him down, the jump throungh the Weapon Armory door.")
            return('laser_weapon_armory')
        
        else:
            print("DOES NOT COMPUTE!")
            print('central_corridor')

class LaserWeaponArmory(Scence):
    def enter(self):
        print("You do a dive roll into the Weapon Armory, crouch and scan the room")
        print("for more Gothons that might be hiding. It's dead quiet, too quiet.")
        print("You stand up and run to the far side of the room and find the")
        print("neutron bomb in its container. There's a keypad lock on the box")
        print("and you need the code to get the bomb out. If you get the code")
        print("worng 10 time then the lock closes forever and you can't")
        print("get the bomb. The code is 3 digits.")
        code = "%d%d%d" % (randint(1, 9), randint(1, 9), randint(1, 9))
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZZZEDDDDD!")
            guesses += 1
            guess = input("[keypad]> ")

            if guess == code:
                print("")

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