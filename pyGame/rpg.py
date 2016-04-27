"""RPG TEST GAME."""
from random import randint


class Character:
    """Character Class."""

    def __init__(self):
        """Initialize."""
        self.name = ""
        self.health = 1
        self.health_max = 1

    def do_damage(self, enemy):
        """deal damage to enemy."""
        damage = min(
            max(randint(0, self.health) - randint(0, enemy.health), 0), enemy.health)
        enemy.health = enemy.health - damage
        if damage == 0:
            print("%s evades %s's attack.") % (enemy.name, self.name)
        else:
            print("%s hurts %s!") % (self.name, enemy.name)
        return enemy.health <= 0


class Enemy(Character):
    """deal damage to enemy."""

    def __init__(self, player):
        Character.__init__(self)
        self.name = 'a goblin'
        self.health = randint(1, player.health)


class Player(Character):
    """deal damage to enemy."""

    def __init__(self):
        Character.__init__(self)
        self.state = 'normal'
        self.health = 10
        self.health_max = 10

    def quit(self):
        print("%s can't find the way back home, and dies. \n R.I.P." % self.name)
        self.health = 0

    def help(self):
        print(Commands.keys())

    def status(self):
        print("%s's health: %s/%d" % (self.name, self.health, self.health_max))

    def tired(self):
        print("%s feels tired." % (self.name))
        self.health = max(1, self.health - 1)

    def rest(self):
        print("%s rests." % (self.name))
        if randint(0, 1):
            self.enemy = Enemy(self)
            print("%s is rudely awakened by %s!" % (self.name, self.enemy.name))
            self.state = 'fight'
            self.enemy_attacks()
        else:
            if self.health < self.health_max:
                self.health = self.health + 1
            else:
                print("%s slept too much." % self.name)
                self.health = self.health - 1

    def explore(self):
        if self.state is not 'normal':
            print("%s is too busy right now!" % self.name)
            self.enemy_attacks()
        else:
            print("%s explores a twisty passage" % self.name)
            if randint(0, 1):
                self.enemy = Enemy(self)
                print("%s encounters %s!" % (self.name, self.enemy.name))
                self.state = 'fight'
            else:
                if randint(0, 1):
                    self.tired()

    def flee(self):
        if self.state is not 'fight':
            print("%s rund in circles for a while" % self.name)
            self.tired()
        else:
            if randint(1, self.health + 5) > randint(1, self.enemy.health):
                print("%s flees from %s" % (self.name, self.enemy.name))
                self.enemy = None
                self.state = 'normal'
            else:
                print("%s couldn't escape from %s!" % self.name, self.enemy.name)

    def attack(self):
        if self.state is not 'fight':
            ("%s swats the air, without notable results" % self.name)
            self.tired()
        else:
            ("%s executes %s!" % (self.name, self.enemy.name))
            self.enemy = None
            self.state = 'normal'
            if randint(0, self.health) < 10:
                self.health = self.health + 1
                self.health_max = self.health_max + 1
                ("%s feels stronger!" % self.name)
            else:
                self.enemy_attacks()

    def enemy_attacks(self):
        if self.enemy.do_damage(self):
            print("%s was killed by %s! RIP" % (self.name, self.enemy.name))

Commands = {'quit': Player.quit,
            'help': Player.help,
            'status': Player.status,
            'rest': Player.rest,
            'explore': Player.explore,
            'flee': Player.flee,
            'attack': Player.attack,
            }

p = Player()
p.name = input("What is your character's name? ")
print("(type help to get a list of actions)\n")
print("%s enters a dark cave, searching for adventure." % p.name)

while(p.health > 0):
    line = input("> ")
    args = line.split()
    if len(args) > 0:
        commandFound = False
    for c in Commands.keys():
        if args[0] == c[:len(args[0])]:
            Commands[c](p)
            commandFound = True
            break
    if not commandFound:
        print("%s doesn't understand the suggestion." % p.name)
