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