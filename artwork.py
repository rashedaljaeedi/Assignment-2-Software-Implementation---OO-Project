class Artwork:
    # Constructor method for the Artwork class
    def __init__(self, title, artist, date_of_creation, historical_significance, location):
        # Initialize attributes with provided values
        self.__title = title  # Title of the artwork
        self.__artist = artist  # Artist who created the artwork
        self.__date_of_creation = date_of_creation  # Date when the artwork was created
        self.__historical_significance = historical_significance  # Historical significance of the artwork
        self.__location = location  # Location where the artwork is currently located
        self.exhibitions = []
    # Getter for title
    def get_title(self):
        return self.__title  # Returns the title of the artwork

    # Setter for title
    def set_title(self, title):
        self.__title = title  # Sets the title of the artwork to the provided value

    # Getter for artist
    def get_artist(self):
        return self.__artist  # Returns the artist of the artwork

    # Setter for artist
    def set_artist(self, artist):
        self.__artist = artist  # Sets the artist of the artwork to the provided value

    # Getter for date_of_creation
    def get_date_of_creation(self):
        return self.__date_of_creation  # Returns the date of creation of the artwork

    # Setter for date_of_creation
    def set_date_of_creation(self, date_of_creation):
        self.__date_of_creation = date_of_creation  # Sets the date of creation of the artwork to the provided value

    # Getter for historical_significance
    def get_historical_significance(self):
        return self.__historical_significance  # Returns the historical significance of the artwork

    # Setter for historical_significance
    def set_historical_significance(self, historical_significance):
        self.__historical_significance = historical_significance  # Sets the historical significance of the artwork to the provided value

    # Getter for location
    def get_location(self):
        return self.__location  # Returns the location of the artwork

    # Setter for location
    def set_location(self, location):
        self.__location = location  # Sets the location of the artwork to the provided value

    def add_exhibition(self, exhibition):
        self.exhibitions.append(exhibition)
        
    # String representation of the Artwork object
    def __str__(self):
        return f"\nArtwork: {self.title} by {self.artist}, created on {self.date_of_creation}, located in {self.location}"
