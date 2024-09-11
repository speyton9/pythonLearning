class Player:
    def __init__(self, name, number, position):
        self.name = name
        self.number = number
        self.postion = position

    def action(self):
        return f"{self.name} is a {self.postion} whose number is {self.number}"

if __name__ == "__main__":
    test_player = Player("Steven", 9, "D")
    print(test_player.action())