import unittest

from src.guest import Guest
from src.room import Room

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Ross Geller" , 100 , "Unagi")
        self.guest_2 = Guest("Rachel Green", 80 , "Smelly Cat")
        self.room = Room("The Divorce Force", 90)

    def test_guest_has_name(self):
        self.assertEqual("Ross Geller" , self.guest.name)
    
    def test_guest_has_money(self):
        self.assertEqual(100, self.guest.wallet)

    def test_enough_money_to_pay_entry_fee(self):
        self.assertEqual(True, self.guest.enough_money_to_pay_entry_fee(self.room))

    def test_not_enough_money_to_pay_entry_fee(self):
        self.assertEqual(False, self.guest_2.enough_money_to_pay_entry_fee(self.room))

    

