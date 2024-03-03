import json 
from random import shuffle
class season:
    def __init__(self) -> None:
        self.seasons = ["spring", "summer", "autumn", "winter"]
        self.seasons_dict = {"spring": (8, "imagspring"), "summer": (8, "imagsummer"), "autumn": (7, "imagautumn"), "winter": (6, "imagwinter")}
        self.current_season = 0
        self.remaining_time = self.seasons_dict[self.seasons[self.current_season]][0]

    def changeSeason(self):
        self.current_season += 1
        self.remaining_time = self.seasons_dict[self.seasons[self.current_season]][0]
    
    def getRemainingTime(self):
        return self.remaining_time
    
    def updateRemainingTime(self, diff):
        self.remaining_time -= diff


class deck:
    def __init__(self) -> None:
        self.load()
        self.card_order = list(range(len(self.cards)))
        self.pointer = 0

    def load(self):
        self.cards = json.load(open("cards/cards.jsonl"))
        self.monsters = json.load(open("cards/monsters.jsonl"))
        self.shapes = json.load(open("cards/shapes.jsonl"))

    def shuffle(self):
        shuffle(self.card_order)
    
    def addMonster(self):
        pass

    def drawCard(self):
        card = self.cardfile[self.pointer]
        shape = self.shapes[card["shape"]]
        pointer += 1
        return card, shape
    
    def newSeason(self):
        self.addMonster()
        self.shuffle()
        self.pointer = 0

    
if __name__=="__main__":
    mydeck=deck()
    mydeck.shuffle()
    print("finish")
    

