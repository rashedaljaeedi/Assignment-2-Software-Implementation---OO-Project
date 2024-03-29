class Visitor:
    def __init__(self, name, age, contact, category):  # Constructor to initialize Visitor objects
        self.name = name  # Assigning name attribute
        self.age = age  # Assigning age attribute
        self.contact = contact  # Assigning contact attribute
        self.category = category  # Assigning category attribute, representing the type of visitor
        self.tickets = []  # Initializing empty list to store tickets purchased by the visitor

        # Getter for name
    def get_name(self):
        return self.name

        # Setter for name
    def set_name(self, name):
        self.name = name

        # Getter for age
    def get_age(self):
        return self.age

        # Setter for age
    def set_age(self, age):
        self.age = age

        # Getter for contact
    def get_contact(self):
        return self.contact

        # Setter for contact
    def set_contact(self, contact):
         self.contact = contact

        # Getter for category
    def get_category(self):
        return self.category

        # Setter for category
    def set_category(self, category):
        self.category = category

        # Getter for tickets
    def get_tickets(self):
        return self.tickets

        # Setter for tickets
    def set_tickets(self, tickets):
         self.tickets = tickets

    def purchase_ticket(self, ticket):  # Method to purchase a ticket for an event
        self.tickets.append(ticket)  # Adding the purchased ticket to the list of tickets
        return f"Ticket purchased for {ticket.event_details}."  # Returning a confirmation message with event details

    def __str__(self):  # Method to represent Visitor object as a string
        return f"Visitor: {self.name}, Age: {self.age}, Contact: {self.contact}, Category: {self.category}"  # Formatting string representation
