class Star_Cinema:
    __hall_list = []

    def entry_hall(self, hall):
        Star_Cinema.__hall_list.append(hall)

class Hall(Star_Cinema):
    __next_hall_number = 100

    def __init__(self, rows, cols):
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = Hall.__next_hall_number
        Hall.__next_hall_number += 1
        self.entry_hall(self)

    def entry_show(self, show_id, movie_name, time):
        self.__show_list.append((show_id, movie_name, time))
        self.__seats[show_id] = [[0] * self.__cols for _ in range(self.__rows)]

    def __is_valid_seat(self, row, col):
        return 0 <= row < self.__rows and 0 <= col < self.__cols

    def __is_seat_booked(self, seat_layout, row, col):
        return seat_layout[row][col] == 1

    def is_valid_show(self, show_id):
        return show_id in self.__seats

    def book_seats(self, show_id, seat_list):
        if not self.is_valid_show(show_id):
            print("\nInvalid Show ID. No show is running with that ID.\n")
            return

        seat_layout = self.__seats[show_id]
        print(f"\nBooking seats for Show ID {show_id}...\n")

        for row, col in seat_list:
            row -= 1
            col -= 1
            if not self.__is_valid_seat(row, col):
                print(f"Seat ({row + 1}, {col + 1}) is out of range. Please choose a valid seat.")
            elif self.__is_seat_booked(seat_layout, row, col):
                print(f"Seat ({row + 1}, {col + 1}) is already booked.")
            else:
                seat_layout[row][col] = 1
                print(f"Seat ({row + 1}, {col + 1}) successfully booked for Show ID {show_id}.")

    def view_show_list(self):
        if not self.__show_list:
            print("No shows available today.\n")
        else:
            print("\nToday's Shows:")
            for show_id, movie_name, time in self.__show_list:
                print(f"Movie: {movie_name} | Show ID: {show_id} | Time: {time}")
            print()

    def view_available_seats(self, show_id):
        if not self.is_valid_show(show_id):
            print("\nInvalid Show ID. No show is running with that ID.\n")
            return

        print(f"\nAvailable Seats for Show ID {show_id} (0 = available, 1 = booked):\n")
        for row in self.__seats[show_id]:
            print(" ".join(map(str, row)))
        print()


def run():
    menu = """
Welcome to Star Cinema!
Choose an option:
1. View Today's Shows
2. View Available Seats
3. Book Ticket
4. Exit
Enter choice: """
    
    while True:
        try:
            choice = int(input(menu))
            if choice == 1:
                hall_1.view_show_list()
            elif choice == 2:
                show_id = int(input("Enter the Show ID to view available seats: "))
                hall_1.view_available_seats(show_id)
            elif choice == 3:
                show_id = int(input("Enter the Show ID for booking: "))
                if not hall_1.is_valid_show(show_id):
                    print("Invalid Show ID! No show is running with that ID.\n")
                    continue

                num_tickets = int(input("Enter the number of tickets: "))
                seat_list = []
                for i in range(num_tickets):
                    row = int(input(f"Enter row for ticket {i + 1}: "))
                    col = int(input(f"Enter column for ticket {i + 1}: "))
                    seat_list.append((row, col))

                hall_1.book_seats(show_id, seat_list)
            elif choice == 4:
                print("Thank you for visiting Star Cinema! Goodbye!")
                break
            else:
                print("Please select a valid option.\n")
        except ValueError:
            print("Invalid input! Please enter a number.\n")

hall_1 = Hall(4, 4)
hall_1.entry_show(1021, 'Inception', '5pm')
hall_1.entry_show(3045, 'The Matrix', '8pm')
hall_1.entry_show(1122, 'Interstellar', '1pm')
hall_1.entry_show(2211, 'Jurassic Park', '11am')
hall_1.entry_show(3344, 'The Godfather', '4pm')
hall_1.entry_show(4455, 'Forrest Gump', '7pm')
hall_1.entry_show(5566, 'Titanic', '9pm')

run()