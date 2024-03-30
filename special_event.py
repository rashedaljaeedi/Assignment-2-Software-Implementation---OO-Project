from exhibition import Exhibition  # Importing the Exhibition class from exhibition module

class SpecialEvent(Exhibition):
    def __init__(self, title, duration, location, purpose):
        super().__init__(title, duration, location)  # Calling the constructor of the superclass Exhibition
        self.__purpose = purpose  # Attribute to hold the purpose of the special event

    # Getter for purpose
    def get_purpose(self):
        return self.__purpose

    # Setter for purpose
    def set_purpose(self, purpose):
        self.__purpose = purpose

    # Method to represent SpecialEvent object as a string
    def __str__(self):
        return f"\n the  {self.__title}  and the event takes place at  {self.__duration}, and it located at {self.__location} and the {self.__purpose} for kids with cancer"

    
