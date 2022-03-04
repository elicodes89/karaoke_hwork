import unittest

from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song("Love", "Romantic")
        self.song_2 = Song("Hate", "Rock")
        # self.song_3 = Song("Sublime", "Pop")

    def test_song_has_name(self):
        self.assertEqual("Love", self.song_1.name)

    def test_song_has_genre(self):
        self.assertEqual("Rock", self.song_2.genre)

    # def test_songs_queue_starts_at_0(self):
    #     self.assertEqual(0, self.song.songsqueue())