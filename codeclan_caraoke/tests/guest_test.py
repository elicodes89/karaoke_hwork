import unittest

from src.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Ross Geller" , 100)

    def test_guest_has_name(self):
        self.assertEqual("Ross Geller" , self.guest.name)
    
    def test_guest_has_money(self):
        self.assertEqual(100, self.guest.wallet)

