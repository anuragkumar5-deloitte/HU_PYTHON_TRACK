class Admin_Login:
    def __init__(self):
        self.title = ""
        self.genre = ""
        self.length = ""
        self.cast = ""
        self.director = ""
        self.rating = ""
        self.language = ""
        self.timing = []
        self.shows = 0
        self.first_show = ""
        self.interval_time = ""
        self.gap = ""
        self.capacity = 0
        self.val1 = []

    def admin_login(self):
        while True:
            print("1.	Admin Login:")
            print("******Welcome Admin*******")
            print("1. Add New Movie Info")
            print("2. Edit Movie Info")
            print("3. Delete Movies")
            print("4.Logout")
            x = int(input("Enter your choice..."))
            if x == 1:
                self.add_movie_info()
            elif x == 2:
                self.update_movie_info()
            elif x == 3:
                self.delete_movie()
            elif x == 4:
                return "Thanks"
            else:
                print("Invalid Input...")

    def add_movie_info(self):
        print("******Welcome Admin*******")
        self.title = input("Enter title\n")
        self.val1.append(self.title)
        self.genre = input("Enter genre\n")
        self.val1.append(self.genre)
        self.length = input("Enter length of movie\n")
        self.val1.append(self.length)
        self.cast = input("Enter cast\n")
        self.val1.append(self.cast)
        self.director = input()
        self.rating = ""
        self.language = ""
        self.timing = []
        self.shows = 0
        self.first_show = ""
        self.interval_time = ""
        self.gap = ""
        self.capacity = 0

    def update_movie_info(self):
        pass

    def delete_movie(self):
        pass
