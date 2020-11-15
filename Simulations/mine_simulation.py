import random
from enum import Enum
import statistics as stat

ores  = {
    "Aether": 1,
    "Diamond": 2,
    "Platinum": 3,
    "Gold": 4,
    "Silver": 5,
    "Iron": 6,
    "Copper": 7,
    "Stone": 8
}
# Gay bullshit
population = []
for key in ores:
    population.append(ores[key])
print(population)




# ores = ['Aether', 'Diamond', 'Platinum', 'Gold', 'Silver', 'Copper', 'Iron']
class MineUser:
    def __init__(self, user, ag, c, pt, ae, fe, au, cu, stone, level):
        self.user = user
        self.aether_amnt = ae
        self.aether_val = 1400
        self.aether_rate = 1

        self.diamond_amnt = c
        self.diamond_val = 600
        self.diamond_rate = 1

        self.platinum_amnt = pt
        self.platinum_val = 300
        self.platinum_rate = 1

        self.gold_amnt = au
        self.gold_val = 100
        self.gold_rate = 1

        self.silver_amnt = ag
        self.silver_val = 20
        self.silver_rate = 1

        self.copper_amnt = cu
        self.copper_val = 3
        self.copper_rate = 1

        self.iron_amnt = fe
        self.iron_val = 5
        self.iron_rate = 1

        self.stone_amnt = stone
        self.stone_val = 1

        self.credits = 0
        self.level = level

    def mine1(self):
        # mine = random.random() * 100
        # if mine < 80:
        #     iron_gained = 1
        #     self.iron_amnt += iron_gained
        #     # self.iron_amnt += random.randint(1,4)
        #     self.credits += iron_gained * self.iron_val
        # else:
        #     stone_gained = random.randint(2,3)
        #     self.stone_amnt += stone_gained
        #     self.credits += stone_gained * self.stone_val
        self.stone_amnt += 1
        self.credits += 5

    #  WORKING MINE 2
    def mine2(self):
        lvl2 = [0, 0, 0, 0, 0.01 * self.silver_rate, 0.15 * self.iron_rate, 0.1 * self.copper_rate, 0.74]
        mine = random.choices(population, lvl2) # Returns number from 1-8
        if mine[0] == ores['Silver']:
            self.silver_amnt += 1
            self.credits += 1 * self.silver_val
        elif mine[0] == ores['Iron']:
            gain = random.random()
            if gain < 0.7:
                self.iron_amnt += 1
                self.credits += 1 * self.iron_val
            else:
                self.iron_amnt += 2
                self.credits += 2 * self.iron_val
        elif mine[0] == ores['Copper']:
            gain = random.random()
            if gain < 0.7:
                self.copper_amnt += 1
                self.credits += 1 * self.copper_val
            else:
                self.copper_amnt += 2
                self.credits += 2 * self.copper_val
        else:
            stone_gained = random.randint(1, 3)
            self.stone_amnt += stone_gained
            self.credits += stone_gained * self.stone_val

        #     if mine < 1 * self.silver_rate:
        #         silver_gain = 1
        #         self.silver_amnt += silver_gain
        #         self.credits += silver_gain * self.silver_val
        #     elif mine < 11:
        #         gain = random.random()
        #         if gain < 0.7:
        #             self.copper_amnt += 1
        #             self.credits += 1 * self.copper_val
        #         else:
        #             self.copper_amnt += 2
        #             self.credits += 2 * self.copper_val
        #     elif mine < 26:
        #         gain = random.random()
        #         if gain < 0.7:
        #             self.iron_amnt += 1
        #             self.credits += 1 * self.iron_val
        #         else:
        #             self.iron_amnt += 2
        #             self.credits += 2 * self.iron_val
        #     else:
        #         stone_gained = random.randint(1, 3)
        #         self.stone_amnt += stone_gained
        #         self.credits += stone_gained * self.stone_val


    def mine3(self):
        mine = random.random() * 100
        if mine < 1.25:
            silver_gain = 1
            self.silver_amnt += silver_gain
            self.credits += silver_gain * self.silver_val
        elif mine < 13.75:
            gain = random.random()
            if gain < 0.5:
                self.copper_amnt += 1
                self.credits += 1 * self.copper_val
            else:
                self.copper_amnt += 2
                self.credits += 2 * self.copper_val
        elif mine < 31.25:
            gain = random.random()
            if gain < 0.5:
                self.iron_amnt += 1
                self.credits += 1 * self.iron_val
            else:
                self.iron_amnt += 2
                self.credits += 2 * self.iron_val
        else:
            stone_gained = random.randint(1, 3)
            self.stone_amnt += stone_gained
            self.credits += stone_gained * self.stone_val

    def mine4(self):
        mine = random.random() * 100
        if mine < 1.5:
            silver_gain = random.randint(1,2)
            self.silver_amnt += silver_gain
            self.credits += silver_gain * self.silver_val
        elif mine < 16.5:
            gain = random.random()
            if gain < 0.35:
                self.copper_amnt += 1
                self.credits += 1 * self.copper_val
            elif gain < 0.75:
                self.copper_amnt += 2
                self.credits += 2 * self.copper_val
            else:
                self.copper_amnt += 3
                self.credits += 3 * self.copper_val
        elif mine < 36.5:
            gain = random.random()
            if gain < 0.35:
                self.iron_amnt += 1
                self.credits += 1 * self.iron_val
            elif gain < 0.75:
                self.iron_amnt += 2
                self.credits += 2 * self.iron_val
            else:
                self.iron_amnt += 3
                self.credits += 3 * self.iron_val
        else:
            stone_gained = random.randint(2, 3)
            self.stone_amnt += stone_gained
            self.credits += stone_gained * self.stone_val

    def mine5(self):
        """
        I MODIFIED THIS SO IT WILL WORK WITH THE ACTUAL DISCORD BOT! :D
        :return:
        """
        mine = random.random() * 100
        if mine < 5:
            silver_gain = 2
            self.silver_amnt += silver_gain
            self.credits += silver_gain * self.silver_val
        elif mine < 25:
            gain = random.random()
            if gain < 0.3:
                coppergain = 2
                self.copper_amnt += coppergain
                self.credits += 2 * self.copper_val
                return 'Copper', coppergain
            elif gain < 0.7:
                coppergain = 3
                self.copper_amnt += coppergain
                self.credits += 3 * self.copper_val
                return 'Copper', coppergain
            else:
                coppergain = 4
                self.copper_amnt += 4
                self.credits += 4 * self.copper_val
                return 'Copper', coppergain
        elif mine < 50:
            gain = random.random()
            if gain < 0.3:
                irongain = 2
                self.iron_amnt += irongain
                self.credits += 2 * self.iron_val
                return 'Iron', irongain
            elif gain < 0.7:
                irongain = 3
                self.iron_amnt += irongain
                self.credits += 3 * self.iron_val
                return 'Iron', irongain
            else:
                irongain = 4
                self.iron_amnt += irongain
                self.credits += 4 * self.iron_val
                return 'Iron', irongain

        else:
            stone_gained = random.randint(2, 4)
            self.stone_amnt += stone_gained
            self.credits += stone_gained * self.stone_val
            return 'Stone', stone_gained


    def mine6(self):
        mine = random.random() * 100
        if mine < 5.5:
            silver_gain = 2
            self.silver_amnt += silver_gain
            self.credits += silver_gain * self.silver_val
        elif mine < 32:
            gain = random.random()
            if gain < 0.3:
                self.iron_amnt += 2
                self.credits += 2 * self.iron_val
            elif gain < 0.7:
                self.iron_amnt += 3
                self.credits += 3 * self.iron_val
            else:
                self.iron_amnt += 4
                self.credits += 4 * self.iron_val
        elif mine < 53.5:
            gain = random.random()
            if gain < 0.3:
                self.copper_amnt += 2
                self.credits += 2 * self.copper_val
            elif gain < 0.7:
                self.copper_amnt += 3
                self.credits += 3 * self.copper_val
            else:
                self.copper_amnt += 4
                self.credits += 4 * self.copper_val
        # New gold feature
        elif mine < 54:
            self.gold_amnt += 1
            self.credits += 1 * self.gold_val
        else:
            stone_gained = random.randint(2, 4)
            self.stone_amnt += stone_gained
            self.credits += stone_gained * self.stone_val

    def mine7(self):
        mine = random.random() * 100
        if mine < 6:
            silver_gain = 2
            self.silver_amnt += silver_gain
            self.credits += silver_gain * self.silver_val
        elif mine < 34:
            gain = random.random()
            if gain < 0.25:
                self.iron_amnt += 2
                self.credits += 2 * self.iron_val
            elif gain < 0.75:
                self.iron_amnt += 3
                self.credits += 3 * self.iron_val
            else:
                self.iron_amnt += 4
                self.credits += 4 * self.iron_val
        elif mine < 57:
            gain = random.random()
            if gain < 0.25:
                self.copper_amnt += 2
                self.credits += 2 * self.copper_val
            elif gain < 0.75:
                self.copper_amnt += 3
                self.credits += 3 * self.copper_val
            else:
                self.copper_amnt += 4
                self.credits += 4 * self.copper_val
        # New gold feature
        elif mine < 57.75:
            self.gold_amnt += 1
            self.credits += 1 * self.gold_val
        else:
            stone_gained = random.randint(3, 4)
            self.stone_amnt += stone_gained
            self.credits += stone_gained * self.stone_val

    def mine8(self):
        mine = random.random() * 100
        if mine < 6.5:
            silver_gain = random.randint(2,3)
            self.silver_amnt += silver_gain
            self.credits += silver_gain * self.silver_val
        elif mine < 36:
            gain = random.random()
            if gain < 0.45:
                self.iron_amnt += 3
                self.credits += 3 * self.iron_val
            elif gain < 0.85:
                self.iron_amnt += 4
                self.credits += 4 * self.iron_val
            else:
                self.iron_amnt += 5
                self.credits += 5 * self.iron_val
        elif mine < 60.5:
            gain = random.random()
            if gain < 0.45:
                self.copper_amnt += 3
                self.credits += 3 * self.copper_val
            elif gain < 0.85:
                self.copper_amnt += 4
                self.credits += 4 * self.copper_val
            else:
                self.copper_amnt += 5
                self.credits += 5 * self.copper_val
        # New gold feature
        elif mine < 61.5:
            self.gold_amnt += 1
            self.credits += 1 * self.gold_val
        else:
            stone_gained = random.randint(3, 4)
            self.stone_amnt += stone_gained
            self.credits += stone_gained * self.stone_val

    def mine9(self):
        mine = random.random() * 100
        if mine < 7:
            silver_gain = random.randint(2,3)
            self.silver_amnt += silver_gain
            self.credits += silver_gain * self.silver_val
        elif mine < 38:
            gain = random.random()
            if gain < 0.4:
                self.iron_amnt += 3
                self.credits += 3 * self.iron_val
            elif gain < 0.8:
                self.iron_amnt += 4
                self.credits += 4 * self.iron_val
            else:
                self.iron_amnt += 5
                self.credits += 5 * self.iron_val
        elif mine < 64:
            gain = random.random()
            if gain < 0.4:
                self.copper_amnt += 3
                self.credits += 3 * self.copper_val
            elif gain < 0.8:
                self.copper_amnt += 4
                self.credits += 4 * self.copper_val
            else:
                self.copper_amnt += 5
                self.credits += 5 * self.copper_val
        # New gold feature
        elif mine < 65.5:
            gold_gain = 1
            self.gold_amnt += gold_gain
            self.credits += gold_gain * self.gold_val
        else:
            stone_gained = random.randint(3, 5)
            self.stone_amnt += stone_gained
            self.credits += stone_gained * self.stone_val

    def mine(self):
        if self.level == 1:
            self.mine1()
        elif self.level == 2:
            self.mine2()
        elif self.level == 3:
            self.mine3()
        elif self.level == 4:
            self.mine4()
        elif self.level == 5:
            ore, gain  = self.mine5()
            return ore, gain
        elif self.level == 6:
            self.mine6()
        elif self.level == 7:
            self.mine7()
        elif self.level == 8:
            self.mine8()
        elif self.level == 9:
            self.mine9()

def avg(lst):
    return sum(lst) / len(lst)

def minestats():
    print('Total Times mined: ', mined)
    print('Total rolls: ', mined/5)
    print('Aether:', miner.aether_amnt)
    print('Diamond:', miner.diamond_amnt)
    print('Platinum:', miner.platinum_amnt)
    print('Gold:', miner.gold_amnt)
    print('Silver:', miner.silver_amnt)
    print('Copper:', miner.copper_amnt)
    print('Iron:', miner.iron_amnt)
    print('Stone:', miner.stone_amnt)
    print('Credits:', miner.credits, '\n')


# miner = MineUser('peepee', 0, 0, 0, 0, 0, 0, 0, 0)

# for i in range(5):
#     mined = 0
#
#     while miner.credits < 5:
#         miner.mine1()
#         mined += 1
#     miner.credits = 0
#     # Lvl 2
#     while miner.credits < 150:
#         miner.mine2()
#         mined += 1
#     miner.credits = 0
#     # Lvl 3
#     while miner.credits < 350:
#         miner.mine3()
#         mined += 1
#     # Lvl 4
#     miner.credits = 0
#     while miner.credits < 500:
#         miner.mine4()
#         mined += 1
#     # Lvl 5
#     miner.credits = 0
#     while miner.credits < 1500:
#         miner.mine5()
#         mined += 1
#     # Lvl 6
#     miner.credits = 0
#     while miner.credits < 2250:
#         miner.mine6()
#         mined += 1
#     # Lvl 7
#     miner.credits = 0
#     while miner.credits < 3000:
#         miner.mine7()
#         mined += 1
#     # Lvl 8
#     miner.credits = 0
#     while miner.credits < 4500:
#         miner.mine8()
#         mined += 1
#     # Lvl 9
#     miner.credits = 0
#     while miner.credits < 6500:
#         miner.mine9()
#         mined += 1
#
#     minestats()
# Mean/Median Machine for Credits of miner
# minecreds = []
# for i in range(100):
#     for i in range(5):
#         miner.credits = 0
#         miner.mine2()
#         minecreds.append(miner.credits)
# print(avg(minecreds))
# print(stat.median(minecreds))

# Store level up credit amounts
level_up = [0, 5, 150, 350, 500, 1500, 2250, 3000, 4500, 6500]

# roll = input('Input anything to roll u cannot escape the roll')
# if 'roll' in globals():
#     output = random.random()
#     print(output)
#  WORKING MINE 2
# def mine2(self):
#     mine = random.random() * 100
#     if mine < 1 * self.silver_rate:
#         silver_gain = 1
#         self.silver_amnt += silver_gain
#         self.credits += silver_gain * self.silver_val
#     elif mine < 11:
#         gain = random.random()
#         if gain < 0.7:
#             self.copper_amnt += 1
#             self.credits += 1 * self.copper_val
#         else:
#             self.copper_amnt += 2
#             self.credits += 2 * self.copper_val
#     elif mine < 26:
#         gain = random.random()
#         if gain < 0.7:
#             self.iron_amnt += 1
#             self.credits += 1 * self.iron_val
#         else:
#             self.iron_amnt += 2
#             self.credits += 2 * self.iron_val
#     else:
#         stone_gained = random.randint(1, 3)
#         self.stone_amnt += stone_gained
#         self.credits += stone_gained * self.stone_val
