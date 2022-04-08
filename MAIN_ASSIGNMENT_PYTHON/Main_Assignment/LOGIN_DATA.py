import csv
from ADMIN_LOGIN import Admin_Login
from USER_LOGIN import User_Login
from BOOK_TICKET import Movie


class Login(Admin_Login, User_Login, Movie):
    def __init__(self):
        super().__init__()
        self.user_id = ""
        self.password = ""
        self.pass_word = ""
        self.name = ""
        self.email = ""
        self.phone = ""
        self.age = ""
        self.val = []

    def details(self):
        self.user_id = input("Enter user id...\n")
        self.password = input("Enter your password...\n")

    def write_data(self, file_name, y):
        print("Entering login data into csv file...")
        # opening the login_data file
        with open(file_name, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(y)
        f.close()
        self.val = []

    def register_new_user(self):
        self.name = input("Enter your name\n")
        self.val.append(self.name)
        self.pass_word = input("Enter tour password\n")
        self.val.append(self.pass_word)
        self.email = input("Enter your email\n")
        self.val.append(self.email)
        self.phone = input("Enter your phone\n")
        self.val.append(self.phone)
        self.age = input("Enter your age\n")
        self.val.append(self.age)
        file_name = 'register_data.csv'
        self.write_data(file_name, self.val)
        self.val = []
        self.val.append(self.name)
        self.val.append(self.pass_word)
        file_name = 'login_data.csv'
        self.write_data(file_name, self.val)
        self.val = []

    def main_menu(self):
        while True:
            print("******Welcome to BookMyShow*******")
            print("1. Login")
            print("2. Register New Account")
            print("3. Exit")
            x = int(input("Enter your choice..."))
            if x == 1:
                self.login()
            elif x == 2:
                print("****Create new Account*****")
                self.register_new_user()
            elif x == 3:
                return "Thanks...!!!"
            else:
                print("Invalid Input...!!!")

    def extract_password(self, file_name):
        p = []
        with open(file_name) as file_obj:
            reader_obj = csv.reader(file_obj)
            for row in reader_obj:
                p = row
        return p[1]

    def login(self):
        self.details()
        if self.user_id == 'Admin':
            file_name = 'admin_data.csv'
            if self.extract_password(file_name) == self.password:
                print('\n', Admin_Login.admin_login(self))
            else:
                return "Invalid Input...!!!"
        else:
            print('\n', User_Login.user_login(self))


obj = Login()
obj.main_menu()
