class Negyzet:
    #konstruktor
    def __init__(self, a: float = 0):
        super().__init__()
        #adattagok
        self.oldal: float = a
    
    #függvények
    def terulet(self) -> float: 
        return self.oldal * self.oldal
    def kerulet(self) -> float:
        return 4 * self.oldal