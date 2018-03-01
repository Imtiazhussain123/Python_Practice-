from User import User
class Admin(User):
    def __init__(self,f_name,l_name,phone,address):
        super().__init__(f_name,l_name,phone,address)
        self.privilages = Privileges()

class Privileges():
    def __init__(self):
        self.privilages = []

    def show_privileges(self):
        print("Have the following privillages:")
        x= 0
        for privilage in self.privilages:
            x +=1;
            print(x,'-',privilage)
