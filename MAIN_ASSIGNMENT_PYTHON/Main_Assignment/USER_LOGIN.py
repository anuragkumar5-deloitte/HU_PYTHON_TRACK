from BOOK_TICKET import Movie


class User_Login(Movie):
    def __init__(self):
        super().__init__()

    def user_login(self):
        while True:
            print("******Welcome User1******* ")
            print("Which movie do you want to watch?")
            print("1. Movie 1")
            print("2. Movie 2")
            print("3. Lorem")
            print("4. Logout")
            movie_no = int(input("Enter your choice...\n"))
            if movie_no == 3:
                self.lorem()
            elif movie_no == 4:
                return "Logged out..."
            elif movie_no == 1 or movie_no == 2:
                print(movie_no)

    def lorem(self):
        lorem_data = open('lorem_data.csv')
        print(lorem_data.read())
        obj = Movie()
        obj.menu()
