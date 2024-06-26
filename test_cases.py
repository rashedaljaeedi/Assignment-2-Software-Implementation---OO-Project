# Importing necessary classes from respective modules
from artwork import Artwork
from exhibition import Exhibition
from special_event import SpecialEvent
from tour import Tour
from visitor import Visitor
from ticket import Ticket

# Test function to create and print details of a Visitor object
def test_Visitor():
    # Creating a Visitor object with name, age, contact, and category
    visitor = Visitor("Rashed", 30, "0509182913", "adult")
    # Printing details of the Visitor object
    print(visitor)

# Test function to create and print details of an Artwork object
def test_add_artwork():
    # Creating an Artwork object with title, artist, date, description, and location
    artwork = Artwork("Mona Lisa", "Leonardo da Vinci", "1503–1506", "Renaissance masterpiece", "Permanent Galleries")
    # Printing details of the Artwork object
    print(artwork)

# Test function to create and print details of an Exhibition object
def test_new_exhibition():
    # Creating an Exhibition object with title, duration, and location
    exhibition = Exhibition("Picasso Exhibition", "March 1 - April 30, 2024", "Exhibition Hall 1")
    # Printing details of the Exhibition object
    print(exhibition)

# Test function to create and print details of a SpecialEvent object
def test_new_special_event():
    # Creating a SpecialEvent object with title, duration, location, and purpose
    special_event = SpecialEvent("Charity Concert", "April 1, 2024", "Outdoor Space", "Fundraising")
    # Printing details of the SpecialEvent object
    print(f"\n new added Special Event ", special_event)

# Test function to create and print details of a Tour object
def test_new_tour():
    # Creating a Tour object with title, duration, location, and guide
    tour = Tour("Historical Art Tour", "March 30 - April 30, 2024", "Permanent Galleries", "Ahmed Smith")
    # Printing details of the Tour object
    print(tour)

# Test function to create and print ticket details for various scenarios
def test_calculate_ticket_price():
    # Creating a Visitor object for an adult visitor
    adult_visitor = Visitor("james andrew", 30, "050567421", "adult")
    # Creating a Ticket object for the adult visitor
    adult_ticket = Ticket("Exhibition", "Picasso Exhibition", adult_visitor)
    # Printing details of the visitor, exhibition, ticket price, and receipt
    print(
        f"\nVisitor: {adult_visitor.name}, Age: {adult_visitor.age}, Contact: {adult_visitor.contact}, Category: {adult_visitor.category} ")
    print(f"Receipt for: {adult_visitor.name} paid price {adult_ticket.price} AED for {adult_ticket.event_details}")

    # Creating a Visitor object for a child visitor
    child_visitor = Visitor("ahmed zayed", 10, "0509872345", "child")
    # Creating a Ticket object for the child visitor
    child_ticket = Ticket("Exhibition", "Picasso Exhibition", child_visitor)
    # Printing details of the visitor, exhibition, ticket price, and receipt
    print(
        f"\nVisitor: {child_visitor.name}, Age: {child_visitor.age}, Contact: {child_visitor.contact}, Category: {child_visitor.category} ")
    print(f"Receipt for: {child_visitor.name} paid price {child_ticket.price} AED for {child_ticket.event_details}")

   # Test for a senior visitor
   # Creating a Visitor object for a senior visitor
   senior_visitor = Visitor("Alice", 65, "alice@example.com", "senior")
   # Creating a Ticket object for the senior visitor
   senior_ticket = Ticket("Exhibition", "Picasso Exhibition", senior_visitor)
   # Print visitor details, exhibition, ticket price, and receipt
   print(
       f"\nVisitor: {senior_visitor.name}, Age: {senior_visitor.age}, Contact: {senior_visitor.contact},Category: {senior_visitor.category} ")
   print(
       f"Receipt for: {senior_visitor.name} paid price {senior_ticket.price} AED for {senior_ticket.event_details}")

   # Test for a teacher visitor
   # Creating a Visitor object for a teacher visitor
   teacher_visitor = Visitor("Abdullah", 40, "abdullah@example.com", "teacher")
   # Creating a Visitor object for a teacher visitor
   teacher_ticket = Ticket("Exhibition", "Picasso Exhibition", teacher_visitor)
   # Print visitor details, exhibition, ticket price, and receipt
   print(
       f"\nVisitor: {teacher_visitor.name}, Age: {teacher_visitor.age}, Contact: {teacher_visitor.contact}, Category: {teacher_visitor.category} ")
   print(
       f"Receipt for: {teacher_visitor.name} paid price {teacher_ticket.price} AED for {teacher_ticket.event_details}")

   # Test for a student visitor
   # Creating a Visitor object for a student visitor
   student_visitor = Visitor("mayed", 20, "mayed@example.com", "student")
   # Creating a Visitor object for a student visitor
   student_ticket = Ticket("Exhibition", "Picasso Exhibition", student_visitor)
   # Print visitor details, exhibition, ticket price, and receipt
   print(
       f"\nVisitor: {student_visitor.name}, Age: {student_visitor.age}, Contact: {student_visitor.contact}, Category: {student_visitor.category} ")
   print(
       f"Receipt for: {student_visitor.name} paid price {student_ticket.price} AED for {student_ticket.event_details}")

    # Creating a SpecialEvent object for a charity concert
    special_event = SpecialEvent("Charity Concert", "April 1, 2024", "Outdoor Space", "Fundraising for cancer")
    # Setting individual ticket price for the special event
    special_event.price = 100
    # Creating a Ticket object for the special event
    special_event_ticket = Ticket("SpecialEvent", special_event, adult_visitor)
    # Printing details of the visitor, ticket price, and receipt for the special event
    print(
        f"\nVisitor: {adult_visitor.name}, Age: {adult_visitor.age}, Contact: {adult_visitor.contact}, Category: {adult_visitor.category} ")
    print(
        f"Receipt for: {adult_visitor.name} paid price {special_event_ticket.price} AED for {special_event.title}")

    # Creating a group leader Visitor object for a tour
    group_leader = Visitor("west Smith", 19, "0509129234", "adult")
    # Defining group size for the tour
    group_size = 20
    # Creating a Ticket object for the tour group
    group_ticket = Ticket("SpecialEvent", special_event, group_leader, group_size)
    # Printing details of the group leader, event, ticket price, and receipt for the tour
    print(
        f"\nVisitor: {group_leader.name}, Age: {group_leader.age}, Contact: {group_leader.contact}, Category: group")
    print(f"Event: {special_event.title}, Date: {special_event.duration}, Location: {special_event.location}")
    print(f"Ticket Price: {group_ticket.price} AED")
    print(
        f"Receipt for: {group_leader.name} paid price for the full group {group_ticket.price} AED for {special_event.title}")


# Main entry point to run the test functions
if __name__ == "__main__":
    # Running each test function to verify functionality
    test_Visitor()
    test_add_artwork()
    test_new_exhibition()
    test_new_special_event()
    test_new_tour()
    test_calculate_ticket_price()
