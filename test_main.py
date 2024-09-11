class Player:
    def __init__(self, name, number, position):
        self.name = name
        self.number = number
        self.postion = position

    def action(self):
        return f"{self.name} is a {self.postion} whose number is {self.number}"
    
class Goalie(Player):
    def __init__(self, name, number, position, team):
        super().__init__(name, number, position)
        self.team = team

    def goalie_action(self):
        return f"{self.name} is a {self.postion} who is number {self.number} on {self.team}"

if __name__ == "__main__":
    test_player = Player("Steven", 9, "D")
    print(test_player.action())
    test_goalie = Goalie("Nick", 48, "G", "Flyers")
    print(test_goalie.goalie_action())