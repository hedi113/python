from bread import Bread
from chocolate import Chocolate
from donut import Donut
from milk import Milk
from yoghurt import Yoghurt
from shoppingCart import ShoppingCart

itemBread: Bread = Bread("2023.05.27", 1, 2, "Varga Pékség")
itemChocolate: Chocolate = Chocolate("2024.01.03", 100, 1, "tibi")
itemDonut: Donut = Donut("2023.06.01", 50, 2, "Lidl Pékség")
itemMilk: Milk = Milk("2023.05.30", 1, 3, "Mizo")
itemYoghurt: Yoghurt = Yoghurt("2023.05.30", 500, 1, "Pilos")

shoppingCart: ShoppingCart = ShoppingCart(itemBread, itemChocolate, itemDonut, itemMilk, itemYoghurt)

print(shoppingCart)