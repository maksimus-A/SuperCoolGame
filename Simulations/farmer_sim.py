"""
Gonna take some notes before I start
Farming: only vegetables
Initially: Choose 2:
    - Potatoes
    - Lettuce
    - Carrots
When you start farming, you will now have 10 intervals to do farm jobs. It's up to you what jobs to do, and hope for the best afterwards.
You can:
    Plant seeds  (Any 3)
    Choose field (1 fields for each crop)
    Will either:
        Blight (0.5x)
        Fertilize(1.5x)
        Normal Yield(1x)

"""
import random

farmorder = {
    'Carrot': ['Normal', 1],
    'Corn': ['Unlucky', 0.75],
    'Potatoes': ['Lucky', 1.25]
}

def mod10(number):
    return number % 10
class Farm_user:
    def __init__(self, user):
        self.cornseeds_planted = 0
        self.corn = 0
        self.cornvalue  = 0.25 # Credit value
        self.cornamount = 8
        self.cornmultiplier = 1

        self.carrotseeds_planted = 0
        self.carrots = 0
        self.carrotvalue = 0.35 # Credit value
        self.carrotamount = 6
        self.carrotmultiplier = 1

        self.potatoseeds_planted = 0
        self.potatoes = 0
        self.potatovalue = 0.5 # Credit value
        self.potatoamount = 4
        self.potatomultiplier = 1

        self.rotation = mod10(0)
        self.credits = 0
        self.user = user

    def random_sim_plant(self, times_to_sim=1): # plants 10 random seeds
        for i in range(times_to_sim):
            for i in range(3):
                farm_crop = random.randint(1,3)
                # farm = ['Carrots','Potatoes','Corn']
                # random.shuffle(farm)
                if farm_crop == 1: # Carrots
                    self.carrotseeds_planted += self.carrotamount
                    # self.credits += self.carrotamount * self.carrotvalue
                elif farm_crop == 2: # Potatoes
                    self.potatoseeds_planted += self.potatoamount
                    # self.credits += self.potatoamount * self.potatovalue
                elif farm_crop == 3: # Corn
                    self.cornseeds_planted += self.cornamount


    def randomize_luck(self):
        lucklist = []
        farmlist = ['Carrots', 'Corn', 'Potatoes']
        for value in farmorder:
            lucklist.append(farmorder[value])
        random.shuffle(lucklist)
        good_farmdic = {farmlist[i]: lucklist[i] for i in range(len(farmlist))}
        return good_farmdic

    def harvest(self):
        farms = self.randomize_luck()
        for crop in farms:
            if crop == 'Carrots':
                luck = farms.get(crop) # Get luck value from dictionary
                self.carrots += self.carrotseeds_planted * self.carrotmultiplier * luck[1] # Luck 1 is multiplier
                carrotcredgain = self.carrots * self.carrotvalue
                self.credits += carrotcredgain

            elif crop == 'Corn':
                luck = farms.get(crop)
                self.corn += self.cornseeds_planted * self.cornmultiplier * luck[1]
                corncredgain = self.corn * self.cornvalue
                self.credits += corncredgain

            elif crop == 'Potatoes':
                luck = farms.get(crop)
                self.potatoes += self.potatoseeds_planted * self.potatomultiplier * luck[1]
                potatocredgain = self.potatoes * self.potatovalue
                self.credits += potatocredgain
        print(luck[0], 'carrots: ', carrotcredgain, 'credits')
        print(luck[0], 'corn: ', corncredgain, 'credits')
        print(luck[0], 'potatoes:', potatocredgain, 'credits')
        print('Total credits:', self.credits, '\n')




for i in range(10):
    farm = Farm_user(i)
    print(farm.carrotseeds_planted)
    print(farm.credits)
    farm.random_sim_plant()
    farm.harvest()
    print('Carrot Seeds Planted:', farm.carrotseeds_planted)
    print('Corn Seeds Planted:', farm.cornseeds_planted)
    print('Potato Seeds Planted:', farm.potatoseeds_planted)
    # farm.cornseeds_planted = 0
    # farm.carrotseeds_planted = 0
    # farm.potatoseeds_planted = 0
    # farm.credits = 0
    # def harvest(self):




    # def farm(self, user, crop):
    #     if crop == 'potato':
    #         pass
