
#import Man from man
#import Hero from hero

class Weapon(Man):
    def __init__(self,name,damage):
        #super().__init__(None,name,title,health,mana,mana_regeneration_rate)
        #self.weapon_damage=weapon_damage
        #self.weapon_name=weapon_name
        self.name=name
        self.damage=damage

    def get_weapon_name(self):
        return str(self.weapon_name)

    def get_weapon_damage(self):
        return int(self.weapon_damage)

