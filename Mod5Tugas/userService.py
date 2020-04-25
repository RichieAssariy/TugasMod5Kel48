class userService(object):
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.data = {
            "richiekelompok48@gmail.com" : {
                "email"     : "richiekelompok48@gmail.com",
                "password"  : "12345",
                "role"      : "superadmin"
            },
            "abamkelompok48@gmail.com" : {
                "email"     : "abamkelompok48@gmail.com",
                "password"  : "12345",
                "role"      : "user"
            },
            "adad" : {
                "email"     : "adad",
                "password"  : "12345",
                "role"      : "user"
            }
        }
        self.history = {
            "richiekelompok48@gmail.com" : {
                "peminjaman_buku" : {'Fisika Dasar', 'Dasar Komputer dan Pemrograman'} ,
                "tanggal_pinjam" : "25-04-2020"
                },
            "abamkelompok48@gmail.com" : {
                "peminjaman_buku": {'Kalkulus', 'Dasar Komputer dan Pemrograman', 'Konsep Jaringan Komputer'},
                "tanggal_pinjam" : "25-04-2020",
                }
            }
    def login(self):
        get_data = self.checkCredentials()
        if get_data:
            print("\nWelcome ",get_data['role'])
            print("Logged it as user email: ",get_data['email'],"\n")
        else:
            print("\nInvalid Login!\n")

    def checkCredentials(self):
        for value in self.data:
            if value == self.email:
                get_data_user = self.data[value]
                if self.password == get_data_user['password']:
                    return get_data_user
                else:
                    return False

    def checkBorrowed(self):
        for value2 in self.history:
            if value2 == self.email:
                print(value2,"meminjam buku: \n")
                get_history_user = self.history[value2]
                return get_history_user
            else:
                print('pengguna tidak meminjam buku')
                return False
    def borrow(self):
        get_history = self.checkBorrowed()
        if get_history:
            for con in get_history['peminjaman_buku']:
                print(con,"\n")
            print("Tanggal Peminjaman : ",get_history['tanggal_pinjam'])

