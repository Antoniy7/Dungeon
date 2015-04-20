class Man:

    def __init__(self, health=100, mana=100):
        self.__health = health
        self.__mana = mana
        self.HEALTH_MIN = 0
        self.HEALTH_MAX = 100
        self.MANA_MIN = 0
        self.MANA_MAX = 100

    def is_alive(self):
        return self.__health > self.HEALTH_MIN

    def get_health(self):
        return self.__health

    def get_mana(self):
        return self.__mana

    def can_cast(self):
        return self.mana > self.MANA_MIN

    def take_mana(self, mana_points):
        if self.__mana + mana_points >= self.MANA_MAX:
            self.__mana = self.MANA_MAX
        else:
            self.__mana += mana_points

    def take_healing(self, healing_points):
        if self.__health + healing_points >= self.HEALTH_MAX:
            self.__health = self.HEALTH_MAX
        else:
            self.__health += healing_points
