from typing import List, TypeVar, TypedDict
from numpy.random import Generator

T = TypeVar("T")


class WeightedKeys(TypedDict):
    Keys: List[T]
    Chances: List[float]


class ChoiceFunctions:
    @staticmethod
    def GetKey(weightedKeys: WeightedKeys, generator: Generator):
        return generator.choice(a=weightedKeys["Keys"], p=weightedKeys["Chances"])

    @staticmethod
    def Normalize(chances: List[float]):
        totalSum = sum(chances)
        return [x / totalSum for x in chances]