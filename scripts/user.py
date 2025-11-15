from choices import WeightedKeys
from scripts.choices import ChoiceFunctions
import random


class UserFunctions:
    @staticmethod
    def GetActionChances() -> WeightedKeys:
        action_chances: WeightedKeys = {
            "Keys": ["Skip", "Like", "Dislike", "Favorite"],
            "Chances": [random.random(), random.random(), random.random(), random.random()],
        }
        action_chances["Chances"] = ChoiceFunctions.Normalize(action_chances["Chances"])
        return action_chances