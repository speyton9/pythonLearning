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
    
class Skater(Player):
    def __init__(self, player_name, number, age, position, team_name, city, mascot, goals, assists):
        super().__init__(player_name, number, age, position, team_name, city, mascot)
        self.goals= goals
        self.assists = assists

    def calc_points(self):
        return self.goals + self.assists
    
    def skater_info(self):
        return f"{self.player_name} plays {self.position} and has scored {self.goals} goals and {self.assists} assists for a total of {self.calc_points()}"
    
class Goalie(Player):
    def __init__(self, player_name, number, age, position, team_name, city, mascot, saves, shots):
        super().__init__(player_name, number, age, position, team_name, city, mascot)
        self.saves = saves
        self.shots = shots

    def save_pct(self):
        return self.saves / self.shots
    
    def goalie_info(self):
        return f"{self.player_name} is a {self.position} on the {self.city} {self.team_name} with a save percentage of {100 * round(self.save_pct(), 4)}%"

if __name__ == "__main__":
    test_team = Team("Flyers", "Philadelphia", 'Gritty')
    #test_player = Player("Giroux", 28, 36, "Center", "Flyers", "Philadelphia", 'Gritty')
    test_player = Player("Giroux", 28, 36, "Center", test_team.team_name, test_team.city, test_team.mascot)
    #test_skater = Skater("Giroux", 28, 36, "Center", "Flyers", "Philadelphia", 'Gritty', 30, 43)
    test_skater = Skater(test_player.player_name, test_player.number, test_player.age, test_player.position, test_team.team_name, test_team.city, test_team.mascot, 30, 43)
    test_goalie = Goalie("Errson", 32, 24, "Goalie", "Flyers", "Philadelphia", 'Gritty', 40, 43)
    #print(test_team.team_info())
    print(test_player.team_info())
    print(test_player.player_info())
    print(test_skater.skater_info())
    print(test_goalie.goalie_info())