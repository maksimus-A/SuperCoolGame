import random
import math

class Farm_user:
    def __init__(self):
        self.bonusyields = {
            'Unlucky': 0.5,
            'Normal': 1,
            'Lucky': 1.5,
            'Lucky+': 2,
            'Lucky++': 5
        }
        self.cornrates = [15, 25, 55, 4, 1]
        self.basecornyield = 2
        self.cornseeds = 0
        self.cornfield  = 'Normal'
        self.corn = 0

        self.carrotrates = [25, 40, 30, 2.5, 0.5]
        self.basecarrotyield = 4
        self.carrotseeds = 0
        self.carrotfield = 'Normal'
        self.carrots = 0

        self.potatorates = [55, 30, 12, 1.85, 0.15]
        self.basepotatoyield = 8
        self.potatoseeds = 0
        self.potatofield = 'Normal'
        self.potatoes = 0


        self.rolls = 0

        # self.bonusyields = [0.5, 1, 1.5, 2, 5]
        self.credits = 0
        self.lvl = 2

    def random_sim_plant(self, times_to_sim=1): # plants 3 random seeds
        for i in range(times_to_sim):
            for i in range(3):
                farm_crop = random.randint(1,3)
                # farm = ['Carrots','Potatoes','Corn']
                # random.shuffle(farm)
                if farm_crop == 1: # Carrots
                    self.carrotseeds += 1
                    # self.credits += self.carrotamount * self.carrotvalue
                elif farm_crop == 2: # Potatoes
                    self.potatoseeds += 1
                    # self.credits += self.potatoamount * self.potatovalue
                elif farm_crop == 3: # Corn
                    self.cornseeds += 1

    def structured_sim_plant(self, times_to_sim=1, cornseeds=1, carrotseeds=1, potatoseeds=1): # Plants 1 seed in each
        assert cornseeds + carrotseeds + potatoseeds == 3, 'Must plant 3 seeds'
        for i in range(times_to_sim):
            self.potatoseeds += potatoseeds
            self.cornseeds += cornseeds
            self.carrotseeds += carrotseeds
        print('Planted', self.cornseeds, 'cornseeds')
        print('Planted', self.carrotseeds, 'carrotseeds')
        print('Planted', self.potatoseeds, 'potatoseeds')

    def randomize_field_luck(self):
        """
        It would be nice for this to return numbers,
        but it's returning 'Lucky' 'normal' etc
        :return:
        """
        luck = list(self.bonusyields.keys())
        multiplier = list(self.bonusyields.values())
        cornluck = random.choices(luck, self.cornrates)
        # print('\nCorn:', cornluck[0])
        carrotluck = random.choices(luck, self.carrotrates)
        # print('Carrots:', carrotluck[0])
        potatoluck = random.choices(luck, self.potatorates)
        # print('Potatoes:', potatoluck[0])
        return cornluck[0], carrotluck[0], potatoluck[0]

    def harvest(self):
        cornluck, carrotluck, potatoluck = self.randomize_field_luck()
        # ((0.1*(A23-1))*G5)+G5 A23 = self.lvl, G5 = self.basecornyield
        cornyield = math.floor((((0.12 * (self.lvl-1)) * self.basecornyield) + self.basecornyield)) * self.cornseeds
        carrotyield = math.floor((((0.1 * (self.lvl-1)) * self.basecarrotyield) + self.basecarrotyield)) * self.carrotseeds
        potatoyield = math.floor((((0.08 * (self.lvl-1)) * self.basepotatoyield) + self.basepotatoyield)) * self.potatoseeds
        # print(cornyield, carrotyield, potatoyield)
        for key in self.bonusyields.keys():
            if key == cornluck:
                # print('Cornluck:', self.bonusyields[key])
                cornmult = self.bonusyields[key]
            if key == carrotluck:
                # print('Carrotluck:', self.bonusyields[key])
                carrotmult = self.bonusyields[key]
            if key == potatoluck:
                # print('Potatoluck:', self.bonusyields[key])
                potatomult = self.bonusyields[key]
        cornyield = math.floor(cornyield * cornmult)
        carrotyield = math.floor(carrotyield * carrotmult)
        potatoyield = math.floor(potatoyield * potatomult)
        # print(cornyield, carrotyield, potatoyield)
        self.corn = cornyield
        self.carrots = carrotyield
        self.potatoes = potatoyield
        # print('Total corn:', self.corn)
        # print('Total carrots:', self.carrots)
        # print('Total potatoes:', self.potatoes)
        # (((1.5*(A23-1))*H23)+H23, 0) A23 IS self.lvl, H23 = self.*crop*
        self.credits += round(((1.5 * (self.lvl-1))*self.corn)+self.corn) # Corn gain
        self.credits += round(((1.2 * (self.lvl - 1)) * self.carrots) + self.carrots) # Carrot gain
        self.credits += round(((0.8 * (self.lvl - 1)) * self.potatoes) + self.potatoes) # Potato gain
        # print('Total credit gain:', self.credits)

level_up = [0, 5, 150, 350, 500, 1500, 2250, 3000, 4500, 6500]
totalrolls = 0
lvl = 1
for credits in level_up:
    farm = Farm_user()
    farm.lvl = lvl
    print('Rolls:', farm.rolls)
    farm.rolls = 0
    while farm.credits < credits:
        farm.cornseeds = 0
        farm.carrotseeds = 0
        farm.potatoseeds = 0
        farm.random_sim_plant()
        farm.harvest()
        farm.rolls += 1
    print('Rolls:', farm.rolls)
    totalrolls += farm.rolls
    print('Total rolls:', totalrolls)
    lvl += 1