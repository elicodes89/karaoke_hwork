import unittest

from src.song import Song
from src.room import Room


class TestSong(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song("Love", "Romantic")
        self.song_2 = Song("Geology Rocks", "Rock")
        # self.song_3 = Song("Sublime", "Pop")
        self.room = Room("The Divorce Force")


    def test_song_has_name(self):
        self.assertEqual("Love", self.song_1.name)


    def test_song_has_genre(self):
        self.assertEqual("Rock", self.song_2.genre)