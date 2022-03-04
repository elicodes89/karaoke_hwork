import unittest

from src.room import Room

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Rock Room")

    def test_songs_queue_starts_at_0(self):
        self.assertEqual(0, self.room.get_songs_queue())