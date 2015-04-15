class Hero:
	def __init__ (self,name="Baron",title="Dragonslayer",health=100,mana=100,mana_regeneration_rate=2):
		self.name=name
		self.title=title
		self.health=health
		self.mana=mana
		self.mana_regeneration_rate=mana_regeneration_rate

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
    	if mana>0:
    		return True
    	else :
    		return False

    
