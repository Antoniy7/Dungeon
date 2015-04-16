from weapon import Weapon
from man import Man


class Spell(Weapon, Man):

    def __init__(self, name, damage, mana_cost, cast_range):
        Weapon.__init__(self, name, damage)
        self.__mana_cost = mana_cost
        self.__cast_range = cast_range

    def get_name(self):
        return self.__mana

    def get_cast_range(self):
        return self.__cast_range
