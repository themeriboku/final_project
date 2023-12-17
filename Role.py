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
    def accept_invitation(self):
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
    def accept_invitaion(self):
        pass

    def view(self):
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
