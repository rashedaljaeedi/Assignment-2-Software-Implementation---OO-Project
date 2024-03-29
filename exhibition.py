class Exhibition:
    def __init__(self, title, duration, location):  # Constructor to initialize Exhibition objects
        self.title = title  # Assigning title attribute
        self.duration = duration  # Assigning duration attribute
        self.location = location  # Assigning location attribute
        self.artworks = []  # Initializing empty list to store artworks associated with the exhibition


    # Getter for title
    def get_title(self):
        return self.title

    # Setter for title
    def set_title(self, title):
        self.title = title

    # Getter for duration
    def get_duration(self):
        return self.duration

    # Setter for duration
    def set_duration(self, duration):
        self.duration = duration

    # Getter for location
    def get_location(self):
        return self.location

    # Setter for location
    def set_location(self, location):
        self.location = location

    # Getter for artworks
    def get_artworks(self):
        return self.artworks

    # Setter for artworks
    def set_artworks(self, artworks):
        self.artworks = artworks

    # Method to add an artwork to the exhibition
    def add_artwork(self, artwork):
        self.artworks.append(artwork)  # Appending artwork to the list of artworks

    # Method to represent Exhibition object as a string
    def __str__(self):
        return f"\n the  {self.title} added and the duration: {self.duration},and it located at  {self.location}"

