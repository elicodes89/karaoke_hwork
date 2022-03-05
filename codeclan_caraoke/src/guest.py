class Guest:

    def __init__(self, name, wallet, fav_song):
        self.name = name
        self.wallet = wallet
        self.fav_song = fav_song
        self.room_playlist = []

    def enough_money_to_pay_entry_fee(self, price):
        return self.wallet >= price.fee

    def not_enough_money_to_pay_entry_fee(self, price):
        return self.wallet <= price.fee

    def favourite_song_is_in_room_playlist(self, song):
        if song in self.room_playlist:
            return "Let's sing!"
        else: 
            return "Oh, no :("
    
