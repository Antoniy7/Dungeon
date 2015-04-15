class Hero:
	def __init__ (self,name="Baron",title="Dragonslayer",health=100,mana=100,mana_regeneration_rate=2):
		self.name=name
		self.title=title
		self.health=health
		self.mana=mana
		self.mana_regeneration_rate=mana_regeneration_rate
		self.weapon=weapon
		self.spell=spell

	def known_as(self):
		 message="{hero_name} {hero_title}"
        return message.format(self.name, self.title)
    

    def is_alive(self):
    	if self.health<=0 :
    		return False
    	else :
    		return True

    def get_health(self):
    	return self.health
    
    def get_mana(self):
    	return self.mana

    def can_cast():
    	if self.mana>0:
    		return True
    	else :
    		return False

    def take_damage(self,damage_points):
    	self.health-=damage_points
    	if self.health<0:
    		self.health=0

    def take_healing(self,healing_points):
    	if self.health<0:
    		return False
    	if self.health is 100:
    		return 
    	self.health+=healing_points
    	return True

    def take_mana(self,mana_points):
    	if self.mana is 100:
    		return False
    	if hero_move() is True:
    		self.mana += self.mana_regeneration_rate

    	self.mana+=mana_points

    def equip(self,weapon):
    	self.weapon=weapon

    def learn(self,spell):
    	self.spell=spell

    def attack(self,dmg):
    	if dmg is "magic":
    		








