# create a Pokemon
class OnePunch: 
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.hp = 100
        self.maxHp = 100

#   ⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀
#⠀⠀⠀⣴⠿⠏⠀⠀⠀⠀⠀⠀⢳⡀⠀⡏⠀⠀⠀⠀⠀⢷
#⠀⠀⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀⠀⠀ ⡇
#⠀⠀⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿⠀⣸⠀⠀OK⠀ ⡇
#⠀⠀⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀⣿⠀⢹⠀⠀⠀⠀⠀ ⡇
#⠀⠀⠙⢿⣯⠄⠀⠀⠀⢀⡀⠀⠀⡿⠀⠀⡇⠀⠀⠀⠀⡼
#⠀⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀⠀⠘⠤⣄⣠⠞⠀
#⠀⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀
#⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀
#⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀⠀⣄⢸⠀⠀⠀⠀⠀⠀
#⣿⣿⣧⣀⣿.........⣀⣰⣏⣘⣆⣀⠀⠀

    def __str__(self):
        return f"{self.name}: ({self.type}, {self.hp})"

    # Feed to increase health
    def feed(self):
        if self.hp < self.maxHp:
            self.hp += 1
            print(f"{self.name} now has {self.hp} HP.")
        else:
            print(f"{self.name} is full. *burp*")

    # Make them battle and decide a winner
    def battle(self, opponent):
        print(f"Battle! {self.name} vs. {opponent.name}!")
        result = self.typewheel(self.type, opponent.type)
        # depending on results, have effects
        if result == "lost":
            self.hp -= 10
            print(f"{self.name} now has {self.hp} HP.")
        if result == "won":
            self.hp += 10
            print(f"{self.name} now has {self.hp} HP.")
        print(f"{self.name} has {result} against {opponent.name}!")

    @staticmethod
    def typewheel(type1, type2):
        results = {0: "lost", 1: "won", -1: "tied"}
        # mapping between type and result conditions
        game_map = {"punch": 0, "sword": 1, "psychic": 2}
        # win-lose matric
        winlose = [
            [-1, 1, 0], # punch v. punch = tie, punch v. sword = 1, punch vs. psychic = 0
            [0, -1, 1], # sword
            [1, 0, -1], # psychic
        ]
        #declare winner 
        result = winlose[game_map[type1]][game_map[type2]] # Find result condition based on types
        return results[result]


# Take a look at it

