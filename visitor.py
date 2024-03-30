class Visitor:
    def __init__(self, name, age, contact, category):  # Constructor to initialize Visitor objects
        self.__name = name  # Assigning name attribute
        self.__age = age  # Assigning age attribute
        self.__contact = contact  # Assigning contact attribute
        self.__category = category  # Assigning category attribute, representing the type of visitor
        self.__tickets = []  # Initializing empty list to store tickets purchased by the visitor

        # Getter for name
    def get_name(self):
        return self.__name

        # Setter for name
    def set_name(self, name):
        self.__name = name

        # Getter for age
    def get_age(self):
        return self.__age

        # Setter for age
    def set_age(self, age):
        self.__age = age

        # Getter for contact
    def get_contact(self):
        return self.__contact

        # Setter for contact
    def set_contact(self, contact):
         self.__contact = contact

        # Getter for category
    def get_category(self):
        return self.__category

        # Setter for category
    def set_category(self, category):
        self.__category = category

        # Getter for tickets
    def get_tickets(self):
        return self.__tickets

        # Setter for tickets
    def set_tickets(self, tickets):
         self.__tickets = tickets
        
    def purchase_ticket(self, ticket):
        self.__tickets.append(ticket)
        ticket.set_visitor(self)



    def __str__(self):  # Method to represent Visitor object as a string
        return f"Visitor: {self.__name}, Age: {self.__age}, Contact: {self.__contact}, Category: {self.__category}"  # Formatting string representation
