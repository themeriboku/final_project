# import database module
import csv, os


from database import Database, Table, persons, login



# define a funcion called initializing

my_db = Database()

table1 = Table('login', login)
table2 = Table('persons', persons)

my_db.insert(table1)
my_db.insert(table2)
my_table1 = my_db.search('login')
my_table2 = my_db.search('persons')

def initializing():
# here are things to do in this function:

    # create an object to read all csv files that will serve as a persistent state for this program
    person = []
    with open('persons.csv', mode='r') as file:
        rows = csv.DictReader(file)
        for r in rows:
            person.append(r)
    print(person)

    login = []
    with open('login.csv', mode='r') as file:
        rows = csv.DictReader(file)
        for r in rows:
            login.append(r)
    print(login)

    # create all the corresponding tables for those csv file
    # see the guide how many tables are needed
    # add all these tables to the database


# define a funcion called login

def login():
    username = str(input('please enter username: '))
    password = str(input('please enter password: '))

    user_filter = table1.filter(lambda x: x['username'] == username and x['password'] == password)
        #     user = user_filter.select(['ID', 'role'])
        #
        #     if user is not None and user != []:
        #         # print(user.select(['ID', 'role']))
        #         print(user)
        #         # Return the first entry if found
    else:
        return None
    if user_filter.filter(lambda x: x['role'] == 'admin'):
        user_role = Admin



    




# here are things to do in this function:
   # add code that performs a login task
        # ask a user for a username and password
        # returns [ID, role] if valid, otherwise returning None

# define a function called exit
def exit():
    pass

# here are things to do in this function:
   # write out all the tables that have been modified to the corresponding csv files
   # By now, you know how to read in a csv file and transform it into a list of dictionaries. For this project, you also need to know how to do the reverse, i.e., writing out to a csv file given a list of dictionaries. See the link below for a tutorial on how to do this:

   # https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python


# make calls to the initializing and login functions defined above






initializing()
val = login()

# based on the return value for login, activate the code that performs activities according to the role defined for that person_id

# if val[1] = 'admin':
    # see and do admin related activities
# elif val[1] = 'student':
    # see and do student related activities
# elif val[1] = 'member':
    # see and do member related activities
# elif val[1] = 'lead':
    # see and do lead related activities
# elif val[1] = 'faculty':
    # see and do faculty related activities
# elif val[1] = 'advisor':
    # see and do advisor related activities

# once everyhthing is done, make a call to the exit function
exit()
