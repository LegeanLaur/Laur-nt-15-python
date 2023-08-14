import time

users = {
    'LimbaRomana' : 'Romana1',
    'Matematica': 'Matematica1',
    'LimbaEngleza': 'Engleza1'
}

def login_system():
 for _ in range (4):
    username = input("Username: ")
    password = input("Password: ")

    if username in users and users [username] == password:
        print("Login succesful!")
        return True
    else:
        print("Login failed!")
 print("Too many tries!")
 time.sleep(240)
 return False
def ToDo_List():
    logged_in = False
    while not logged_in:
        logged_in = login_system()
ToDo_List()

