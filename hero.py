import Weapon from weapon
import Man from man
import Spell from spell

class Hero(Man,Weapon):
     def __init__ (self,health,mana,name="Baron",title="Dragonslayer",mana_regeneration_rate=2,take_healing):
        super().__init__(None,health,mana)
        self.mana_regeneration_rate=mana_regeneration_rate
        self.name=name
        self.title=title
        self.weapon=None
        self.spell=None


    def has_weapon(self):
        return self.equipped_weapon

    def equip(self,weapon):
        self.weapon=weapon

    def learn(self,spell):
        self.spell=spell

    def attack(self, by="None"):
        if by == "weapon":
            return self.weapon.get_weapon_name()
        if by == "magic":
            if self.mana < self.spell.get_spell_damage():
                raise Exception("ERROR")
            else:
                self.mana -= self.get_spell_damage()
                return self.spell.get_spell_damage()


    def attack(self,attacking_object,weapon):
        if weapon.name is "weapon":
            return weapon.damage

        if weapon.name is "magic":
            return weapon.damage_points
        



    def take_mana(self,mana_points):
        super().take_mana(None,health,mana)
        if hero_move() is True:
            self.mana += self.mana_regeneration_rate


    def known_as(self):
         message="{hero_name} {hero_title}"
        return message.format(self.name, self.title)
    
    
    def take_damage(self,damage_points):
        self.health-=damage_points
        if self.health<0:
            self.health=0

    def learn(self,spell):
        self.spell=spell

    def take_healing(self,healing_points):
        if self.health<0:
            return False
        if self.health is 100:
            return 
        self.health+=healing_points
        return True

   
            








