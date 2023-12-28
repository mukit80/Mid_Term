class Star_Cinema:
    __hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        cls.__hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.__seats = {}
        self.__show_list = []
        self.__initialize_seats()

    def __initialize_seats(self):
        for i in range(1, self.__rows + 1):
            self.__seats[i] = ['0'] * self.__cols

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.__show_list.append(show_info)
        self.__seats[id] = [['0'] * self.__cols for _ in range(self.__rows)]

    def book_seats(self, id, seats_to_book):
        if id not in self.__seats:
            print("Invalid show ID.")
            return

        for row, col in seats_to_book:
            if row <= 0 or row > self.__rows or col <= 0 or col > self.__cols:
                print("Invalid seat selection.")
                continue

            if self.__seats[id][row - 1][col - 1] == '1':
                print(f"Seat at row {row}, col {col} is already booked.")
            else:
                self.__seats[id][row - 1][col - 1] = '1'
                print(f"Seat at row {row}, col {col} has been booked.")

    def view_show_list(self):
        print("All Shows Today:")
        for idx, show in enumerate(self.__show_list, 1):
            print(f"{idx}. Movie name: {show[1]} ID: {show[0]}")

    def view_available_seats(self, id):
        if id not in self.__seats:
            print("Invalid show ID.")
            return

        print(f"Available seats for show ID {id}:")
        for row in range(self.__rows):
            for col in range(self.__cols):
                if self.__seats[id][row][col] == 'A':
                    print(f"Row {row + 1}, Col {col + 1}")
        print("End of available seats.")

    def show_matrix(self, id):
        if id not in self.__seats:
            print("Invalid show ID.")
            return

        print(f"Seat matrix for show ID {id}:")
        for row in range(self.__rows):
            for col in range(self.__cols):
                print(self.__seats[id][row][col], end=" ")
            print()
        print("End of seat matrix.")

    def menu(self):
        while True:
            print("\nOptions:")
            print("1. View all shows today")
            print("2. View available seats for a show")
            print("3. Book tickets for a show")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.view_show_list()
            elif choice == "2":
                show_id = int(input("Enter the show ID: "))
                self.view_available_seats(show_id)
                self.show_matrix(show_id)
            elif choice == "3":
                show_id = int(input("Enter the show ID: "))
                num_seats = int(input("Enter the number of seats to book: "))
                seats_to_book = []
                for _ in range(num_seats):
                    row = int(input("Enter the row number for seat: "))
                    col = int(input("Enter the col number for seat: "))
                    seats_to_book.append((row, col))
                self.book_seats(show_id, seats_to_book)
                self.show_matrix(show_id)
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    hall1 = Hall(rows=7, cols=7, hall_no=1)
    hall1.entry_show(100, "Jawan", "10:00 AM")
    hall1.entry_show(200, "Superman", "2:00 PM")
    hall1.menu()
