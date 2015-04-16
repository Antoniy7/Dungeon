import Weapon from weapon
import Man from man
class Spell(Weapon,Man):
    def __init__(self,name,damage,mana_cost,cast_range):
        super().__init__(None,name,damage)
        self.__mana_cost=mana_cost
        self.__cast_range=cast_range

    def mana_cost(self):
        if self.mana > mana_cost:
            return False

        else self.mana-=mana_cost

    def cast_range(self):
        
