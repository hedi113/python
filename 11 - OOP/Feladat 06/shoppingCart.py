from bread import Bread
from chocolate import Chocolate
from donut import Donut
from milk import Milk
from yoghurt import Yoghurt

class ShoppingCart: 

    def __init__(self, bread: Bread, chocolate: Chocolate, donut: Donut, milk: Milk, yoghurt: Yoghurt) -> None:
        self.bread = bread
        self.chocolate = chocolate
        self.donut = donut
        self.milk = milk
        self.yoghurt = yoghurt
    
    def __str__(self) -> str:
        return f"A kosár tartalma:\n\nKenyér: {self.bread}\nCsokoládé: {self.chocolate}\nFánk: {self.donut}\nTej: {self.milk}\nJoghurt: {self.yoghurt}"
