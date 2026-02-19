# Design a class as described below:
# - class: User
# instance variable: name(String)
# constructor: parameter: none, task: initialize variable to "Default"
# Example:
# Input: None
# Output: Default

class User:
    def __init__(self):
        self.name = "Default"
    
    def display(self):
        print(self.name)
    
    def SetName(self,name):
        self.name = name
    
user = User()
user.display()
user.SetName("KeenKiz")
user.display()

Johnny = User()

studentList = [user, Johnny]
for student in studentList:
    student.display()
    student.SetName("Student")