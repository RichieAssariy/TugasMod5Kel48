from userService import userService

print("System Login Kelompok 48!\n")
email = input("Email: ")
password = input("Password: ")
get_class = userService(email,password)
get_class.login()
get_class.borrow()