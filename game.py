import extra
import random

class player:
    def __init__(self, name, food, energy, health, distance, score):
        self.name = name
        self.food = food
        self.energy = energy
        self.health = health
        self.distance = distance
        self.score = score

    def death(self):
        print("You died on your travels.")
        print("Your score: ", self.score)

    def travel(self):
        pass

class event:
    def __init__(self, name,
            desc, descSuccess, descFail,
            food, fCost, fFail,
            energy, eCost, eFail,
            health, hCost, hFail,
            dist, distFail,
            variance, eventChance, chance):
        self.name = name

        self.desc = desc
        self.descSuccess = descSuccess
        self.descFail = descFail

        self.food = food
        self.fCost = fCost
        self.fFail = fFail

        self.energy = energy
        self.eCost = eCost
        self.eFail = eFail

        self.health = health
        self.hCost = hCost
        self.hFail = hFail

        self.dist = dist
        self.distFail = distFail

        self.variance = 1+variance
        self.eventChance = eventChance
        self.chance = chance

    def choose(self, choice, player):
        print("Choice")
        if choice == True: #and random.random() > self.eventChance:
            print(self.descSuccess)
            player.food += self.food*randrangeFloat(-self.variance, self.variance, 0.1)
            player.energy += self.energy*randrangeFloat(-self.variance, self.variance, 0.1)
            player.health = 0

def randrangeFloat(start, stop, step):
    return random.randint(0, int((stop - start) / step)) * step + start

def newGame(fMod, eMod, hMod):
    name = input("What's your name? ")
    global player1
    player1 = player(
            name,
            random.randint(10,15)*fMod,
            random.randint(10,15)*eMod,
            random.randint(10,15)*hMod,
            random.randint(100,110),
            0)
    day()

def day():
    print("\n"*100)
    print("It's the middle of the night, and as you drove through the forest, your car stops. It won't start up anymore. It's cold and rainy outside.")
    print("\n")
    print("Your Health: ",player1.health)
    print("Your Food: ", player1.food)
    print("Your Energy: ", player1.energy)
    print("You look at the map... you have", player1.distance, "km to travel.")
    print("\n")
    print("Your check what's in your car...")
