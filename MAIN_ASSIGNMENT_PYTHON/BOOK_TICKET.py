class Movie:
    def __init__(self):
        self.time = {"1": "10.00-1.00", "2": "1.10-4.10", "3": "4.20-7.20", "4": "7.30-10.30"}
        self.x = 10
        self.booked_seat = 0
        self.price_of_ticket = 0
        self.total_cost = 0
        self.row = 0
        self.seats = 0
        self.total_seat = 0
        self.booked_ticket_person = []
        self.seats_chart = {}
        self.user_rating = ""

    def menu(self):
        while True:
            print('1. Timing of movies')
            print('2. Show the seats')
            print('3. Buy tickets')
            print('4. Show booked tickets User Info')
            print('5. Give user rating')
            print('0. Exit')
            inp = int(input('Select Option...'))
            if inp == 1:
                self.timing_of_movie()
            elif inp == 2:
                self.show_seat()
            elif inp == 3:
                self.buy_ticket()
            elif inp == 4:
                self.booked_ticket()
            elif inp == 5:
                self.user_rating = input("Give your rating...")
                print("Thank you for the feedback...!!!")
            elif inp == 0:
                return "Successfully quit...!!!"

    def book_seat(self):
        self.row = int(input('Enter no. of Row...\n'))
        self.seats = int(input('Enter no. of seats in a Row...\n'))
        self.total_seat = self.row * self.seats
        self.booked_ticket_person = [[None for j in range(self.seats)] for i in range(self.row)]

    def chart_maker(self):
        for i in range(self.row):
            seats_in_row = {}
            for j in range(self.seats):
                seats_in_row[str(j + 1)] = 'S'
            self.seats_chart[str(i)] = seats_in_row

    def find_percentage(self):
        percentage = (self.booked_seat / self.total_seat) * 100
        return percentage

    def timing_of_movie(self):
        for key, value in self.time.items():
            print(key, '\t', value)
        t = input("Select your time...")
        z = self.time[t]
        print("Successful...!!!, Enjoy movie at " + z)

    def show_seat(self):
        self.book_seat()
        self.chart_maker()
        if self.seats < 10:
            for seat in range(self.seats):
                print(seat, end='  ')
            print(self.seats)
        else:
            for seat in range(10):
                print(seat, end='  ')
            for seat in range(10, self.seats):
                print(seat, end=' ')
            print(self.seats)
        if self.seats < 10:
            for num in self.seats_chart.keys():
                print(int(num) + 1, end='  ')
                for no in self.seats_chart[num].values():
                    print(no, end='  ')
                print()
        else:
            count_num = 0
            for num in self.seats_chart.keys():
                if int(list(self.seats_chart.keys())[count_num]) < 9:
                    print(int(num) + 1, end='  ')
                else:
                    print(int(num) + 1, end=' ')
                count_key = 0
                for no in self.seats_chart[num].values():
                    if int(list(self.seats_chart[num].keys())[count_key]) <= 10:
                        print(no, end='  ')
                    else:
                        print(no, end='  ')
                    count_key += 1
                count_num += 1
                print()
        print('Vacant Seats = ', self.total_seat - self.booked_seat, '\n')

    def buy_ticket(self):
        row_number = int(input('Enter Row Number - \n'))
        column_number = int(input('Enter Column Number - \n'))
        if row_number in range(1, self.row + 1) and column_number in range(1, self.seats + 1):
            if self.seats_chart[str(row_number - 1)][str(column_number)] == 'S':
                if self.row * self.seats <= 60:
                    self.price_of_ticket = 10
                elif row_number <= int(self.row / 2):
                    self.price_of_ticket = 10
                else:
                    self.price_of_ticket = 8
                print('Price of ticket...', '$', self.price_of_ticket)
                confirm = input('yes to confirm booking and no to cancel booking...')
                person_detail = {}
                if confirm == 'yes':
                    person_detail['Name'] = input('Enter Name - ')
                    person_detail['Gender'] = input('Enter Gender - ')
                    person_detail['Age'] = input('Enter Age - ')
                    person_detail['Phone_No'] = input('Enter Phone number - ')
                    person_detail['Ticket_prize'] = self.price_of_ticket
                    self.seats_chart[str(row_number - 1)][str(column_number)] = 'B'
                    self.booked_seat += 1
                    self.total_cost += self.price_of_ticket
                elif confirm == 'no':
                    return "Cancelled booking...!!!"
                self.booked_ticket_person[row_number - 1][column_number - 1] = person_detail
                print('Booked Successfully')
            else:
                print('This seat is already booked by some one...')
        else:
            print('\n***  Invalid Input  ***\n')

    def booked_ticket(self):
        enter_row = int(input('Enter Row number\n'))
        enter_column = int(input('Enter Column number\n'))
        if enter_row in range(1, self.row + 1) and enter_column in range(1, self.seats + 1):
            if self.seats_chart[str(enter_row - 1)][str(enter_column)] == 'B':
                person = self.booked_ticket_person[enter_row - 1][enter_column - 1]
                print('Name...', person['Name'])
                print('Gender...', person['Gender'])
                print('Age...', person['Age'])
                print('Phone number...', person['Phone_No'])
                print('Ticket Prize...', '$', person['Ticket_prize'])
            else:
                print()
                print('---**---  Vacant seat  ---**---')
        else:
            print()
            print('***  Invalid Input  ***')
            print()
