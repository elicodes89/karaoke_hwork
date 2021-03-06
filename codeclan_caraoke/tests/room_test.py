import unittest

from src.room import Room
from src.song import Song
from src.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("The Divorce Force" , 90)
        self.guest = Guest("Ross Geller" , 100 , "Unagi")
        self.guest_2 = Guest("Rachel Green", 80 , "Smelly Cat")
        self.song = Song("Geology Rocks" , "Rock")

    def test_room_has_name(self):
        self.assertEqual("The Divorce Force", self.room.name)


    def test_songs_queue_starts_at_0(self):
        self.assertEqual(0, self.room.get_songs_queue())
    
    def test_guests_list_starts_at_0(self):
        self.assertEqual(0, self.room.get_guests_list())

    def test_if_checked_in_guest(self):
        self.room.checkin_guest(self.guest)
        self.assertEqual(1, len(self.room.guests_list))

    def test_if_checked_out_guest(self):
        self.room.checkin_guest(self.guest)
        self.room.guests_list.pop()
        self.assertEqual(0, len(self.room.guests_list))

    def test_if_added_song_to_room(self):
        self.room.add_song_to_room(self.song)
        self.assertEqual(1, len(self.room.songs_queue))

    def test_if_checked_in_second_guest(self):
        self.room.checkin_guest(self.guest)
        self.assertEqual(1, len(self.room.guests_list))

    def test_favourite_song_is_in_room_playlist(self):
        self.guest.favourite_song_is_in_room_playlist(self.guest)
        self.assertEqual("Unagi", self.guest.fav_song)
