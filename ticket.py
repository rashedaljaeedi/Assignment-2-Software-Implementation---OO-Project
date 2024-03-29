class Ticket:
    def __init__(self, ticket_type, event_details, visitor, group=False):  # Constructor to initialize Ticket objects
        self.ticket_type = ticket_type  # Assigning ticket_type attribute
        self.event_details = event_details  # Assigning event_details attribute
        self.visitor = visitor  # Assigning visitor attribute, representing the visitor associated with the ticket
        self.group = group  # Assigning group attribute, indicating whether the ticket is for a group
        self.price = self.calculate_price()  # Calculating the price attribute using the calculate_price method

        # Getter for ticket_type
    def get_ticket_type(self):
        return self.ticket_type

        # Setter for ticket_type
    def set_ticket_type(self, ticket_type):
        self.ticket_type = ticket_type

        # Getter for event_details
    def get_event_details(self):
        return self.event_details

        # Setter for event_details
    def set_event_details(self, event_details):
        self.event_details = event_details

        # Getter for visitor
    def get_visitor(self):
        return self.visitor

        # Setter for visitor
    def set_visitor(self, visitor):
        self.visitor = visitor

        # Getter for group
    def get_group(self):
        return self.group

        # Setter for group
    def set_group(self, group):
        self.group = group

        # Getter for price
    def get_price(self):
        return self.price

        # Setter for price
    def set_price(self, price):
        self.price = price

    def calculate_price(self):  # Method to calculate the price of the ticket
        base_price = 63  # Base price in AED
        vat_rate = 0.05  # VAT rate

        # Free ticket for children, teachers, students, and seniors
        if self.visitor.age < 18 or self.visitor.age >= 60 or self.visitor.category in ["teacher", "student"]:
            return 0  # Return 0 price for eligible visitors

        # 50% discount for groups
        elif self.group >= 1:
            if self.ticket_type == "SpecialEvent":
                return (self.event_details.price * 0.5 * self.group) * (1 + vat_rate)  # Calculate price with discount for special events for the group
            else:
                return (base_price * 0.5 * self.group) * (1 + vat_rate)  # Calculate price with discount for regular events for the group

        # Individual ticket prices for special events
        elif self.ticket_type == "SpecialEvent":
            return self.event_details.price * (1 + vat_rate)  # Calculate price without discount for special events

        # Regular price for adults
        else:
            return base_price * (1 + vat_rate)  # Calculate price without discount for regular events

    def __str__(self):  # Method to represent Ticket object as a string
        return f"Ticket: {self.ticket_type}, Event: {self.event_details}, Visitor: {self.visitor.name}, Price: {self.price}"  # Formatting string representation
