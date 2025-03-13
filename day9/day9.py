class Auction:
    def __init__(self):
        self.players = {}
        self.winner = None
        self.winner_bid = 0

    def start_program(self):
        print("Welcome to the secret auction program.")
        while True:
            self.add_player()
            command = input("Are there any other players? Type 'Yes' or 'No'.")
            if command == 'No':
                break
        self.find_winner()
        print(f"The winner is {self.winner} with a bid of {self.winner_bid}")

    def add_player(self):
        player = {}
        name = input("What is your name? ")
        bid = int(input("What is your bid? $"))
        self.players[name] = bid

    def find_winner(self):
        max_bidder = None
        max_bid = 0
        for name, bid in self.players.items():
            if bid > max_bid:
                max_bid = bid
                max_bidder = name
        self.winner = max_bidder
        self.winner_bid = max_bid

play = Auction()
play.start_program()




