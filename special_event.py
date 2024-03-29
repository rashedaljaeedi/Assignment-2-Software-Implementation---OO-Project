from exhibition import Exhibition  # Importing the Exhibition class from exhibition module

class SpecialEvent(Exhibition):
    def __init__(self, title, duration, location, purpose):
        super().__init__(title, duration, location)  # Calling the constructor of the superclass Exhibition
        self.purpose = purpose  # Attribute to hold the purpose of the special event

    # Method to represent SpecialEvent object as a string
    def __str__(self):
        return f"\n the  {self.title}  and the event takes place at  {self.duration}, and it located at {self.location} and the {self.purpose} for kids with cancer"

    # Getter for purpose
    def get_purpose(self):
        return self.purpose

    # Setter for purpose
    def set_purpose(self, purpose):
        self.purpose = purpose
