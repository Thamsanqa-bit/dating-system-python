import csv 

def mainMenu():
    print('---Welcome To Dating System---')

    while True:
        print('''
        ******Main Menu ******
        Find The LOve Of Your Life
        1. Register
        2. Login
        3. Quit
        ''')

        x = input('Enter Choice: ')
        if int(x) == 1:
            register()
            break
        elif int(x) == 2:
            login()
            break
        elif int(x) == 3:
            print('Goodbye')
            break

def register():
    with open('dating.txt', 'a') as f:
        writer = csv.writer(f)

        print('register')
        print('Please register name and Lastname')

        firstname = input('Name: ')
        lastname = input('Lastname: ')
        username = firstname + lastname[0] + '-member'
        print(f'Your generated username is {username}')

        password = input('Enter Password: ')
        gender = input('Whats your sex [select M/F]: ')
        email = input('Enter email: ')
        dob = input('whats your dob dd/mm/yy ')
        beliefs = input('Whats your religion: ')

        strenghtslist = ['patience', 'lazy', 'creative', 'efficient', 'leadership', 'laidback']
        print(strenghtslist)

        strength = input('Select one of your top strength \nfrom the list: ')

        writer.writerow([username, password,firstname, lastname, gender, email, dob, beliefs, strength])

        print('Savings data... You registered!')


def login():
    print('login')
    notLoggedIn = True 
    if notLoggedIn == True:
        while notLoggedIn == True:
            with open('dating.txt', 'r') as fo:
                username = input('Enter username: ')
                password = input('Enter Password: ')
                reader = csv.reader(fo)
                for row in reader:
                    for field in row:
                        if field == username and row[1] == password:
                            notLoggedIn = False
                        else:
                            break
                if notLoggedIn == True:
                    print('Try Again')
                else:
                    print('Access granted, lets begin dating')
                    profile(username)
                
def profile(username):
    print()
    print()
    print()
    print(f'Username{username}')
    print('----Welcome To Your Profile----')

    with open('dating.txt', newline="") as f:
        reader = list(csv.reader(f))
        temporarylist = enumerate(reader)

        for idx, row in temporarylist:
            for field in row:
                if field == username:
                    username_index = idx
                    print('Username_index', username_index)
                    wavedcount = int(reader[username_index][9])

    print('Waved at:', wavedcount)
    waved = int(input('How many potential soulmates have you waved at today? '))
    wavedcount=wavedcount+waved
    print('Waved at updated updated count:', wavedcount)

    temporarylist = []
    updatedlist = []

    with open('dating.txt', newline="") as f:
        reader = list(csv.reader(f))
        temporarylist=reader # storing a copy of a file contents
        for row in reader:
            for field in row:
                if field == username:
                    updatedlist.append(row)
                    updatedlist[0][9] = int(updatedlist[0][9]) + waved
        updatecontactcount(updatedlist, temporarylist) # calling a subroutine


def updatecontactcount(updatedlist, temporarylist):
    # editing a value ina  file
    for index, row in enumerate(temporarylist):
        for field in row:
            if field == updatedlist[0]:
                temporarylist[index] = updatedlist # replacing old record with updated record

    with open('dating.txt', 'w', newline="") as f:
        Writer = csv.writer(f)
        Writer.writerows(temporarylist)
        print('File has been updated')
        print('People you have waved at:', updatedlist[0][9])
    print('....whats next?')
    choice = input('Press S to search or M for match magic: ')
    if choice == 's' or choice == 'S':
        search()
    elif choice == 'm' or choice == 'M':
        matchmaker()

    # if choice == 'S' or choice == 's':
    #     search()
    # elif choice == 'M' or choice == 'm':
    #     matchmaker()
    

def search():
    print('SEARCH MENU--')
    print('''
    1- Search by gender
    2- Search date
    3- search by keyword
    4- Return to Main Menu
    ''')

    choice = input('What would you like to do? ')
    if int(choice) == 1:
        gender()
    elif int(choice) == 2:
        date()
    elif int(choice) == 3:
        keyword()
    elif int(choice) == 4:
        mainMenu()



def keyword():
    print('----keyword search---')
    wordfound = False
    while wordfound == False:
        with open('dating.txt', 'r') as f:
            keyword = input('Enter keyword: ')
            reader = csv.reader(f)
            for row in reader:
                for field in row:
                    if field ==keyword:
                        print(row)
                        wordfound == True

def matchmaker():
    print('---MATCHING MAKING MAGIC---')
    wordfound = False
    while wordfound == False:
        with open('dating.txt', 'r') as f:
            keystrengths = input(' Enter one of your key strengths: ')
            print()
            print()
            print('Potential --true love --matches')
            reader = csv.reader(f)
            for row in reader:
                if row[9] != keystrengths:
                    print(row)

def gender():
    print('====== Search For Gender=====')
    print('Narrow down the search ')
    with open('dating.txt', 'r') as f:
        gender = input('Enter gender you are looking for: ')
        reader = csv.reader(f)
        for row in reader:
            for field in row:
                if field == gender:
                    print(row)

        
    
def date():
    print('--date---')

mainMenu()

