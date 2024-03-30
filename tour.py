from exhibition import Exhibition  # Importing the Exhibition class from exhibition module

class Tour(Exhibition):
    def __init__(self, title, duration, location, guide):
        super().__init__(title, duration, location)  # Calling the constructor of the superclass Exhibition
        self.guide = guide  # Attribute to hold the name of the tour guide

    # Method to represent Tour object as a string
    def __str__(self):
        return f"\n {self.title} by {self.guide}, duration of the tour on {self.duration}, located in {self.location}"

    # Getter for guide
    def get_guide(self):
        return self.guide

    # Setter for guide
    def set_guide(self, guide):
        self.guide = guide

