class User():
    def __init__(self,f_name,l_name,phone,address):
        self.f_name = f_name
        self.l_name = l_name
        self.phone = phone
        self.address = address
        self.login_attempt = 0
    def describe_user(self):
        print('First Name: ',self.f_name.title(),'\nLast Name: ',self.l_name.title(),
              '\nPhone: ',self.phone,'\nAddress: ',self.address)
    def greet_user(self):
        full_name = self.f_name+' '+self.l_name
        print('\nHello! ',full_name,' welcome to our portal.\n' )

    def increment_login_attempt(self,increment_login):
        self.login_attempt +=increment_login
    def reset_login_attempt(self):
        self.login_attempt = 0