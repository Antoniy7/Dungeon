class Enemy:

    def __init__(self, health=100, mana=100, damage=20):
        self.__maxHealth = health
        self.__health = health
        self.__maxMana = mana
        self.__mana = mana
        self.__damage = damage

        def is_alive(self):
            return self.__health > 0

        def can_cast(self):
            return self.__mana > 0

        def get_health(self):
            return self.__health

        def get_mana(self):
            return self.__mana

        def take_healing(self, points):
            if self.__health + points > self.__maxHealth:
                self.__healt = self.__maxHealth
            else:
                self.__healt += points

        def take_mana(self, points):
            if self.__mana + points > self.__maxMana:
                self.mana = self.__maxMana

        def attack():
