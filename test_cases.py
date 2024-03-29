

import unittest  # Importing the unittest module
from artwork import Artwork  # Importing the Artwork class
from exhibition import Exhibition  # Importing the Exhibition class
from special_event import SpecialEvent  # Importing the SpecialEvent class
from tour import Tour  # Importing the Tour class
from visitor import Visitor  # Importing the Visitor class
from ticket import Ticket  # Importing the Ticket class


class TestMuseumSystem(unittest.TestCase):

    def test_Visitor(self):
        # Instantiate a Visitor object with name, age, contact, and category
        visitor = Visitor("Rashed", 30, "0509182913", "adult")
        # Print the details of the Visitor object
        print(visitor)

    def test_add_artwork(self):
        # Instantiate an Artwork object with title, artist, date, description, and location
        artwork = Artwork("Mona Lisa", "Leonardo da Vinci", "1503–1506", "Renaissance masterpiece",
                          "Permanent Galleries")
        # Print the details of the Artwork object
        print(artwork)

    def test_new_exhibition(self):
        # Instantiate an Exhibition object with title, duration, and location
        exhibition = Exhibition("Picasso Exhibition", "March 1 - April 30, 2024", "Exhibition Hall 1")
        # Print the details of the Exhibition object
        print(exhibition)

    def test_new_special_event(self):
        # Instantiate a SpecialEvent object with title, duration, location, and purpose
        special_event = SpecialEvent("Charity Concert", "April 1, 2024", "Outdoor Space", "Fundraising")
        # Print the details of the SpecialEvent object
        print(f"\n new added Special Event ", special_event)

    def test_new_tour(self):
        # Instantiate a Tour object with title, duration, location, and guide
        tour = Tour("Historical Art Tour", "March 1 - April 30, 2024", "Permanent Galleries", "Ahmed Smith")
        # Print the details of the Tour object
        print(tour)

    def test_calculate_ticket_price(self):
        # Test for an adult visitor
        adult_visitor = Visitor("John Doe", 30, "john@example.com", "adult")
        adult_ticket = Ticket("Exhibition", "Picasso Exhibition", adult_visitor)
        # Print visitor details, exhibition, ticket price, and receipt
        print(
            f"\nVisitor: {adult_visitor.name}, Age: {adult_visitor.age}, Contact: {adult_visitor.contact}, Category: {adult_visitor.category} ")
        print(f"Receipt for: {adult_visitor.name} paid price {adult_ticket.price} AED for {adult_ticket.event_details}")

        # Test for a child visitor
        child_visitor = Visitor("Jane Doe", 10, "jane@example.com", "child")
        child_ticket = Ticket("Exhibition", "Picasso Exhibition", child_visitor)
        # Print visitor details, exhibition, ticket price, and receipt
        print(
            f"\nVisitor: {child_visitor.name}, Age: {child_visitor.age}, Contact: {child_visitor.contact}, Category: {child_visitor.category} ")
        print(f"Receipt for: {child_visitor.name} paid price {child_ticket.price} AED for {child_ticket.event_details}")

        # Test for a senior visitor
        senior_visitor = Visitor("Alice", 65, "alice@example.com", "senior")
        senior_ticket = Ticket("Exhibition", "Picasso Exhibition", senior_visitor)
        # Print visitor details, exhibition, ticket price, and receipt
        print(
            f"\nVisitor: {senior_visitor.name}, Age: {senior_visitor.age}, Contact: {senior_visitor.contact},Category: {senior_visitor.category} ")
        print(
            f"Receipt for: {senior_visitor.name} paid price {senior_ticket.price} AED for {senior_ticket.event_details}")

        # Test for a teacher visitor
        teacher_visitor = Visitor("Bob", 40, "bob@example.com", "teacher")
        teacher_ticket = Ticket("Exhibition", "Picasso Exhibition", teacher_visitor)
        # Print visitor details, exhibition, ticket price, and receipt
        print(
            f"\nVisitor: {teacher_visitor.name}, Age: {teacher_visitor.age}, Contact: {teacher_visitor.contact}, Category: {teacher_visitor.category} ")
        print(
            f"Receipt for: {teacher_visitor.name} paid price {teacher_ticket.price} AED for {teacher_ticket.event_details}")

        # Test for a student visitor
        student_visitor = Visitor("Charlie", 20, "charlie@example.com", "student")
        student_ticket = Ticket("Exhibition", "Picasso Exhibition", student_visitor)
        # Print visitor details, exhibition, ticket price, and receipt
        print(
            f"\nVisitor: {student_visitor.name}, Age: {student_visitor.age}, Contact: {student_visitor.contact}, Category: {student_visitor.category} ")
        print(
            f"Receipt for: {student_visitor.name} paid price {student_ticket.price} AED for {student_ticket.event_details}")

        # Test for a special event ticket
        special_event = SpecialEvent("Charity Concert", "April 1, 2024", "Outdoor Space", "Fundraising")
        special_event.price = 100  # Individual ticket price for the special event
        special_event_ticket = Ticket("SpecialEvent", special_event, adult_visitor)
        # Print visitor details, exhibition, ticket price, and receipt
        print(
            f"\nVisitor: {adult_visitor.name}, Age: {adult_visitor.age}, Contact: {adult_visitor.contact}, Category: {adult_visitor.category} ")
        print(
            f"Receipt for: {adult_visitor.name} paid price {special_event_ticket.price} AED for {special_event.title}")

        # Assuming the Visitor and EventDetails classes are defined and instantiated correctly
        group_leader = Visitor("Alice Smith", 28, "0509129234", "adult")
        group = 20  # A tour group of 20 visitors

        # Assuming special_event is an instance of EventDetails
        group_ticket = Ticket("SpecialEvent", special_event, group_leader, group)

        # Print visitor details, event details, ticket price, and receipt
        print(
            f"\nVisitor: {group_leader.name}, Age: {group_leader.age}, Contact: {group_leader.contact}, Category: group")
        print(f"Event: {special_event.title}, Date: {special_event.duration}, Location: {special_event.location}")
        print(f"Ticket Price: {group_ticket.price} AED")
        print(
            f"Receipt for: {group_leader.name} paid price for the full group {group_ticket.price} AED for {special_event.title}")


if __name__ == "__main__":
    unittest.main()  # Running the test cases
