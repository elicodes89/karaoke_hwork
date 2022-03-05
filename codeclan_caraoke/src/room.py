class Room:

    def __init__(self, name, fee):
        self.name = name
        self.fee = fee
        self.songs_queue = []
        self.guests_list = []
        


    def get_songs_queue(self):
        return len(self.songs_queue)

    def get_guests_list(self):
        return len(self.guests_list)

    def checkin_guest(self, guest):
        self.guests_list.append(guest)

    def checkout_guest(self, guest):
        self.guests_list.pop(guest)
    
    def add_song_to_room(self, song):
        self.songs_queue.append(song)


