import random

DEBUG = True


def throw_dice():
    rand = random.randint(1,6)
    if DEBUG: print("Throwing dice: %s" % rand)
    return rand


class Player():
    name = ''
    money = 0
    def __init__(self, name, money = 10000):
        self.name = name
        self.money = money
    
    def __repr__(self):
        return self.name

class Sheet():
    name = ''
    cost = 0
    owner = None

    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
    
    def __repr__(self):
        return self.name


def map():
    ret = []
    ret.append(Sheet('Start', 0))
    ret.append(Sheet('Parkveien', 1000))
    ret.append(Sheet('Kirkeveien', 2000))
    ret.append(Sheet('Nedre slottsgate', 3000))
    ret.append(Sheet('Øvre slottsgate', 4000))
    ret.append(Sheet('Kirkeveien', 5000))
    
    return ret

def players():
    players = []
    players.append(Player('Arvid'))
    players.append(Player('Daniel'))
    return players


def play(map, players):
    
    keep_going = True
    while keep_going:
        for p in players:
            input("Player %s's turn!" % p)
            pos = map[throw_dice()-1]
            print("Hit position %s" % pos)
            if pos.owner:
                print("%s is owned by %s" %(pos.name,pos.owner))
            else:
                purchase = input("%s is available! Would you like to purchase?" % (pos))
                if purchase.lower() == 'y':
                    pos.owner = p
                    print("Successfully purchased %s for %s kr" % (pos.name,pos.cost))
                
map = map()
players = players()
play(map,players)