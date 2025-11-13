from choices import WeightedKeys
from scripts.choices import ChoiceFunctions
import random


class UserFunctions:
    @staticmethod
    def GetActionChances() -> WeightedKeys:
        actionChances: WeightedKeys = {
            "Keys": ["Skip", "Like", "Dislike", "Favorite"],
            "Chances": [random.random(), random.random(), random.random(), random.random()],
        }
        actionChances["Chances"] = ChoiceFunctions.Normalize(actionChances["Chances"])
        return actionChances