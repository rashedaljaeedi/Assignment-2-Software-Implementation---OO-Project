class Exhibition:
    def __init__(self, title, duration, location):  # Constructor to initialize Exhibition objects
        # Initialize attributes with provided values
        self.__title = title  # Assigning title attribute
        self.__duration = duration  # Assigning duration attribute
        self.__location = location  # Assigning location attribute
        self.__artworks = []  # Initializing empty list to store artworks associated with the exhibition


    # Getter for title
    def get_title(self):
        return self.__title

    # Setter for title
    def set_title(self, title):
        self.__title = title

    # Getter for duration
    def get_duration(self):
        return self.__duration

    # Setter for duration
    def set_duration(self, duration):
        self.__duration = duration

    # Getter for location
    def get_location(self):
        return self.__location

    # Setter for location
    def set_location(self, location):
        self.__location = location

    # Getter for artworks
    def get_artworks(self):
        return self.__artworks

    # Setter for artworks
    def set_artworks(self, artworks):
        self.__artworks = artworks

    # Method to add an artwork to the exhibition
    def add_artwork(self, artwork):
        self.artworks.append(artwork)  # Appending artwork to the list of artworks


    # Method to represent Exhibition object as a string
    def __str__(self):
        return f"\n the  {self.__title} added and the duration: {self.__duration},and it located at  {self.__location}"

