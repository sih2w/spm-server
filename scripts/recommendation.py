from typing import List
from scripts.history import History
from scripts.choices import WeightedKeys, ChoiceFunctions
from scripts.song import Song, SongFunctions


class RecommendationFunctions:
    @staticmethod
    def GetSongChance(history: History, song: Song):
        chance = 0.50
        songId = SongFunctions.GetSongId(song)

        if songId in history["Disliked"]:
            chance = 0.10
        else:
            if songId in history["Previous"]:
                chance -= 0.20

            if songId in history["Liked"]:
                chance += 0.10

            if songId in history["Favorite"]:
                chance += 0.20

            if songId in history["Skipped"] and songId in history["Finished"]:
                finishedCount = history["Finished"][songId]
                skippedCount = history["Skipped"][songId]
                percentFinished = finishedCount / (finishedCount + skippedCount)
                chance += (0.10 * percentFinished)

        chance = max(0.00, min(chance, 1.00))

        return chance

    @staticmethod
    def GetSongChances(history: History, songs: List[Song]):
        songChances: WeightedKeys = {
            "Keys": [],
            "Chances": [],
        }

        for song in songs:
            chance = RecommendationFunctions.GetSongChance(history, song)
            songChances["Keys"].append(song)
            songChances["Chances"].append(chance)
        songChances["Chances"] = ChoiceFunctions.Normalize(songChances["Chances"])

        return songChances