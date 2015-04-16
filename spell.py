
import Weapon from weapon
import Man from man
class Spell(Weapon,Man):
    def __init__(self,name,damage,mana_cost,cast_range):
        super().__init__(None,name,damage)
        self.__mana_cost=mana_cost
        self.__cast_range=cast_range
    
    def get_spell_name(self):
        return str(self.name)

    def get_spell_damage(self):
        return int(self.damage)

    def get_spell_mana_cost(self):
        return int(self.mana_cost)




