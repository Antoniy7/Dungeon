import Hero from hero

class Dungeon:

    def __init__(self, filename):
        self.list=[]
        self.current_x=None
        self.current_y=None
        with open(filename, "r") as in_file:
            lines = in_file.read().splitlines()
            self.dungeon_map = []
            for line in lines:
                self.dungeon_map.append(list(line))

    def print_map(self):
        for line in self.list:
            print (''.join(line))

    def spawn(self, hero):
        if not (isinstance(hero, Hero)):
            raise Exception("Not A Hero")

        for i in range (0, len(self.list)):
            for j in range (0, len(self.list[i])):
                if self.list[i][j]=="S":
                    self.list[i][j]="H"
                    self.current_x = i
                    self.current_y = j
 
    return True

        


