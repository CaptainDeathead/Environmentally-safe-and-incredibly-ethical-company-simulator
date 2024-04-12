from game import Game

class Main:
    def __init__(self):
        self.game: Game = Game()
        
    def main(self):
        self.game.main()

if __name__ == "__main__":
    main: Main = Main()
    main.main()
