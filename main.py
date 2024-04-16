#!/usr/bin/env python3

from game import Game

class Main:
    def __init__(self):
        self.game: Game = Game()
        
    def main(self):
        self.game.main()

if __name__ == "__main__":
    print("Loading game...")
    main: Main = Main()
    main.main()
