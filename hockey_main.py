class Team:
    def __init__(self, team_name, city, mascot):
        self.team_name = team_name
        self.city = city
        self.mascot = mascot

    def team_info(self):
        return f"The {self.city} {self.team_name} mascot is named {self.mascot}"
    
class Player(Team):
    def __init__(self, player_name, number, age, position, team_name, city, mascot):
        super().__init__(team_name, city, mascot)
        self.player_name = player_name
        self.number = number
        self.age = age
        self.position = position

    def player_info(self):
        return f"{self.player_name} is a {self.age} year old {self.position} and wears #{self.number} on the {self.city} {self.team_name}"

if __name__ == "__main__":
    test_team = Team("Flyers", "Philadelphia", 'Gritty')
    #print(test_team.team_info())
    test_player = Player("Giroux", 28, 36, "Center", "Flyers", "Philadelphia", 'Gritty')
    print(test_player.player_info())
    print(test_player.team_info())