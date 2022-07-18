from datetime import datetime as dt
from time import sleep

class User():
    def __init__(self, first, last, email):
        self.first_name = first.title()
        self.last_name = last.title()
        self.email = email
        self.created_on = dt.utcnow()

    def change_first(self):
        holder = self.first_name
        print(f'Your current first name is listed as {self.first_name}')
        self.first_name = input('\nWhat would you like to change your first name to?: ').title()
        print(f'Successs, you have changed your first name from {holder} to {self.first_name}')

    def change_last(self):
        holder = self.last_name
        print(f'Your current Last Name is listed as {self.last_name}')
        self.last_name = input('\nWhat would you like to change your last name to?: ').title()
        print(f'Successs, you changed your last name from {holder} to {self.last_name}')

    def __str__(self):
        return f'<User | {self.email}>'

    def __repr__(self):
        return f'<User | {self.email}>'

    def __hash__(self):
        return hash(self.email)

    def __eq__(self, __o):                                                         
        return self.created_on == __o.created_on
    
    def __lt__(self, __o):
        return self.created_on < __o.created_on

    def __gt__(self, __o):
        return self.created_on > __o.created_on

    def __le__(self, __o):
        return self.created_on <= __o.created_on

    def __ge__(self, __o):
        return self.created_on >= __o.created_on 
    

class Employee(User):
    def __init__(self, first, last, email, address, sec_level, department):
        super().__init__(first, last, email)
        self.address = address
        self.sec_level = sec_level
        self.department = department.title()

    @property
    def id(self):
        return self.first_name + '.' + self.last_name + '.' + self.department
    
    def change_dep(self):
        holder = self.department
        print(f'You currently work int the {self.department} department')
        self.department = input('\nWhat department would you like to transfer to?: ').title()
        print(f'Successs, you have been switched from the {holder} department to the {self.department} department')

class Customer(User):
    def __init__(self, first, last, email, shipping_address, billing_address):
        super().__init__(first, last, email)
        self.shipping_address = shipping_address
        self.billing_address = billing_address
        self.purchase_history = []

    @property
    def id(self):
        return self.email + '.' + self.shipping_address
    
    def change_billing(self):
        holder = self.billing_address
        print(f"Your current billing address is listed as: {self.billing_address}")
        self.billing_address = input('\nWhat would you like to change your billing address to?: ')
        print(f'Successs, you have change your billing address from{holder} to {self.billing_address}')
    
    def change_shipping(self):
        holder = self.shipping_address
        print(f"Your current shipping address is listed as: {self.shipping_address}")
        self.shipping_address = input('\nWhat would you like to change your shipping address to?: ')
        print(f'Successs, you have change your shipping address from{holder} to {self.shipping_address}')



    
dylan = Employee('Dylan', 'Katina', 'dylan@iscool.com', '123 Fun St.', 10, 'Tomato Tossing' )
sleep(.3)
jackson = Employee('Jackson', 'Katina', 'jackson@isdumb.com', '147 Dumb St.', 0, 'Lunch Launching' )
sleep(.3)
grace = Employee('Grace', 'Jarret', 'grace@lovesdylan.com', '123 Fun St.', 5, 'Milk Mopping' )
sleep(.3)
paul = Customer('Paul', 'Revere', 'RedCoats@coming.com', '457 N End ave.', '458 N End ave.' )
sleep(.3)
jiggly = Customer('Jiggly', 'Boo', 'JBoo@coming4you.net', '4 Jello Dr.', '2319 Secrect Stash Dr.' )
sleep(.3)
rhia = Customer('Rhia', 'Jarret-Katina', 'rhia@lovesdylan.com', '123 Fun St.', '259 Stinky Dr.')

e_group = sorted([dylan, jackson, rhia, grace, paul, jiggly], reverse=True)

print(e_group)

