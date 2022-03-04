import unittest

from src.room import Room
from src.song import Song
from src.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Rock Room")

    def test_room_has_name(self):
        self.assertEqual("Rock Room", self.room.name)


    def test_songs_queue_starts_at_0(self):
        self.assertEqual(0, self.room.get_songs_queue())
    
    def test_guests_list_starts_at_0(self):
        self.assertEqual(0, self.room.get_guests_list())

    #check in guests and check out guests from rooms
    #add songs to rooms

    # def test_check_in_guest(self):
