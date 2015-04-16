class Man:
	def __init__ (self,health=100,mana=100):
		self.health=health
		self.mana=mana

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

    def take_mana(self,mana_points):
    	if self.mana is 100:
    		return False

    	self.mana+=mana_points

    def take_healing(self,healing_points):
    	if self.health<0:
    		return False
    	if self.health is 100:
    		return 
    	self.health+=healing_points
    	return True


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

   
    		








