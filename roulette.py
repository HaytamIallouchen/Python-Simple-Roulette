import random
class roulette:
    bets = []

    def rouletteGame(self, chips):
        jackpot = random.randint(1, 36)
        while chips > 0:
            bet = input("Op welke nummers wil je inzetten?")
            if bet == "STOP":
                self.check(jackpot, chips)
                self.score(jackpot, chips)
                self.bets.clear()
            else:
                try:
                    type(bet) == int
                    if 1 <= int(bet) <= 36:
                        self.bets.append(int(bet))
                        chips = chips - 1
                        print(self.bets)
                    else:
                        print("Voer opnieuw een getal tussen de 1 en 36")
                        self.rouletteGame(chips)
                except:
                    print("Voer opnieuw een getal tussen de 1 en 36")
                    self.rouletteGame(chips)
        self.check(jackpot, chips)
        self.score(jackpot, chips)

    def check(self, jackpot, chips):
        if jackpot in self.bets:
            print("+35 chips")
            chips = chips + 35
            self.score(jackpot, chips)
            self.rouletteGame(chips)
        else:
            print("-", len(self.bets), "chips")
            if  chips == 0:
                self.score(jackpot, chips)
                print("GAME OVER")
                exit()
    
    def score (jackpot, chips):
        print("rien ne va plus")
        print("De uitkomst is", jackpot)
        print("Je hebt", chips, "chips")
        
roulette().rouletteGame(10)
