
import Man from man

class Hero(Man):
     def __init__ (self,name="Baron",title="Dragonslayer",mana_regeneration_rate=2):
        super().__init__(None,health,mana)
        self.mana_regeneration_rate=mana_regeneration_rate
        self.name=name
        self.title=title

    
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

   
            








