class Player:
    def __init__(self, name, number, position):
        self.name = name
        self.number = number
        self.position = position

    def action(self):
        return None
    
class Goalie(Player):
    def __init__(self, name, number, position, team):
        self.team = team
        super().__init__(name, number, position)

    def action(self):
        return self.team
    
class Skater(Player):
    def __init__(self, name, number, position, speed):
        super().__init__(name, number, position)
        self.speed = speed

    def action(self):
        return self.speed
    
    def get_details(person):
        print(person.action)


if __name__ == "__main__":
    starting_goalie = ("Bob", 35, "G", "Panthers")
    starting_skater = ("Giroux", 28, "C", "Fast as hell")

    get_details(starting_goalie)

