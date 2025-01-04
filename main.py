from foodfacts.main import FoodFact
from foodfacts.display_facts import DisplayFacts
from foodfacts.openfoodfact_adapter import OpenfoodfactAdapter


app = FoodFact(OpenfoodfactAdapter(), DisplayFacts())
app.ask_and_display_data()