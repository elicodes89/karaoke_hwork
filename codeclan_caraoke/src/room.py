class Room:

    def __init__(self, name):
        self.name = name
        self.songs_queue = []
        self.guests_list = []

    def get_songs_queue(self):
        
        return len(self.songs_queue)

    def get_guests_list(self):
        return len(self.guests_list)
