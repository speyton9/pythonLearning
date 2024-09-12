class Team:
    def __init__(self, team_name, city, mascot):
        self.team_name = team_name
        self.city = city
        self.mascot = mascot

    def team_info(self):
        return f"The {self.city} {self.team_name} mascot is named {self.mascot}"

if __name__ == "__main__":
    test_team = Team("Flyers", "Philadelphia", 'Gritty')
    print(test_team.team_info())
