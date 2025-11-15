from scripts.song import Song, SongFunctions
from typing import TypedDict, Dict, List, Literal


class History(TypedDict):
    Liked: Dict[str, bool]
    Disliked: Dict[str, bool]
    Favorite: Dict[str, bool]
    Skipped: Dict[str, int]
    Finished: Dict[str, int]
    Previous: List[str]


class HistoryFunctions:
    @staticmethod
    def UpdatePrevious(history: History, song: Song):
        history["Previous"].insert(0, SongFunctions.GetSongId(song))
        if len(history["Previous"]) > 3:
            history["Previous"].pop()

    @staticmethod
    def Increment(history: History, category: Literal["Skipped", "Finished"], song: Song):
        song_id = SongFunctions.GetSongId(song)
        if not song_id in history[category]:
            history[category][song_id] = 0
        history[category][song_id] += 1

    @staticmethod
    def Create():
        return {
            "Liked": {},
            "Disliked": {},
            "Favorite": {},
            "Skipped": {},
            "Finished": {},
            "Previous": [],
        }