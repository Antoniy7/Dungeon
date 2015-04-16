class Man:

    def __init__(self, health=100, mana=100):
        self.__health = health
        self.__maxHealth = 100
        self.__maxMana = 100
        self.__mana = mana

    def is_alive(self):
        return self.__health > 0

    def get_health(self):
        return self.__health

    def get_mana(self):
        return self.__mana

    def can_cast(self):
        return self.__mana > 0

    def take_healing(self, points):
        if (self.__health + points) > self.__maxHealth:
            self.__health = self.__maxHealth
        else:
            self.__health += points

    def take_mana(self, points):
        if self.__mana + points > self.__maxMana:
            self.mana = self.__maxMana
        else:
            self.__mana += points
