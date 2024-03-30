from exhibition import Exhibition  # Importing the Exhibition class from exhibition module

class Tour(Exhibition):
    def __init__(self, title, duration, location, guide):
        super().__init__(title, duration, location)  # Calling the constructor of the superclass Exhibition
        self.__guide = guide  # Attribute to hold the name of the tour guide
        
    # Getter for guide
    def get_guide(self):
        return self.__guide

    # Setter for guide
    def set_guide(self, guide):
        self.__guide = guide

    # Method to represent Tour object as a string
    def __str__(self):
        return f"\n {self.__title} by {self.__guide}, duration of the tour on {self.__duration}, located in {self.__location}"



    

