
from database import Database, Table, Project, login, persons, Invitation

db = Database()
info_project = Table('Project', Project)
info_invitation = Table('Invitations', Invitation)
info_login = Table('login', login)
info_person = Table('persons', persons)

db.insert(info_person)
db.insert(info_login)
db.insert(info_invitation)
db.insert(info_project)

class User:

    def __init__(self, username, password, id, role):
        self.__username = username
        self.__password = password
        self.__id = id
        self.__role = role


class Admin(User):
    def update(self):
        pass


class Student(User):
    def see_invitation(self):

        see = info_invitation.filter(lambda x: ['username'] == self.__username and ['invitation'] == 'invited')
        see.select(['invitation'])
        if see[0] == {'invitation': 'invited'}:
            print("Yes, you are invited")
        else:
            print("No, you are not invited")

    def accept_invitation(self):
        see = info_invitation.filter(lambda x: ['username'] == self.__username and ['invitation'] == 'invited')


    def deny_invitation(self):
        pass

    def become_lead(self):
        pass

class Lead(User):

    def project_create(self):
        pass

    def member_scout(self):
        pass

    def advisor_scout(self):
        pass

    def add_member(self):
        pass

    def modify_projects(self):
        pass

    def submit_project(self):
        pass
class Member(User):

    def modify_projects(self):
        pass


class Faculty(User):

    def see_invitation(self):
        username = input("Input your username to see invitation: ")
        see = info_invitation.filter(lambda x: ['username'] == username and ['invitation'] == 'invited')
        see.select(['invitation'])
        if see[0] == {'invitation': 'invited'}:
            print("Yes you are invited")
        else:
            print("No you are not invited")

    def accept_invitaion(self):
        pass

    def deny_invitation(self):
        pass

    def view_project(self):
        pass

    def evaluate(self):
        pass


class Advisor(User):

    def approve_project(self):
        pass

    def view(self):
        pass

    def evaluate_project(self):
        pass
