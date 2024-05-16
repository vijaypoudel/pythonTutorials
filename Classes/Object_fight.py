import random
import math

class Warrior:
    def __init__(self, name="Warrior" , health = "0" , attk_max ="0" , block_max="0"):
        self.name = name
        self.health = health
        self.attk_max= attk_max
        self.block_max = block_max

    def attack(self):
        attk_amt = self.attk_max * (random.random() + 0.5)
        return attk_amt

    def block(self):
        block_amt = self.block_max * (random.random() + 0.5)
        return block_amt

class Battle:
    def start_fight(self, warrior1 , warrior2):
        while True:
            if self.get_attack_result(warrior1,warrior2) == "Game Over":
                break
            if self.get_attack_result(warrior2, warrior1) == "Game Over":
                break

    def get_attack_result(self, warrior1, warrior2):
        warrior_a_attk_amt = warriorA.attack()
        warrior_b_attk_amt = warriorB.attack()
        damage_2_warrior_b = math.ceil(warrior_a_attk_amt - warrior_b_block_amt)
        warriorB.health = warriorB.health - damage_2_warrior_b

        print("{} attacks {} and deals {} damage".format(warriorA.name, warriorB.name, damage_2_warrior_b))
