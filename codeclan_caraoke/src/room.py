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

    def checkin_guest(self, Ross):
        self.guests_list.append(Ross)

    def checkout_guest(self, Ross):
        self.guests_list.pop(Ross)
    
    def add_song_to_room(self, song):
        self.songs_queue.append(song)

    def checkin_guest(self, Rachel):
        self.guests_list.append(Rachel)