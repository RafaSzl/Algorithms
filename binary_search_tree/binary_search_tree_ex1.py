"""
 As a senior backend engineer at Jovian, you are tasked with developing a fast in-memory data structure to manage
 profile information (username, name and email) for 100 million users.
 It should allow the following operations to be performed efficiently:

1. Insert the profile information for a new user.
2. Find the profile information of a user, given their username
3. Update the profile information of a user, given their usrname
4. List all the users of the platform, sorted by username
You can assume that usernames are unique.

Along the way, we will also solve several other questions related to binary trees and binary search trees
that are often asked in coding interviews and assessments.

Problem:
We need to create a data structure which can store 100 million records and perform insertion,
search, update and list operations efficiently.

Input:
The key inputs to our data structure are user profiles, which contain the username, name and email of a user.

A Python class would be a great way to represent the information for a user. A class is a blueprint for
creating objects. Everything in Python is an object belonging to some class.

"""


class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
        print('User created')

    # self here is reffering to the actual object (instance) that gets created
    def introduce(self, guest_name):
        print("Hi {}, I'm {}. Contact me at {}".format(guest_name, self.name, self.email))


user2 = User('przemek', 'Przemek Jaki', 'przemo@buziaczek.com')
user2.introduce('David')

# The print statement and str() built-in function uses __str__ to display the string representation of the object
# while the repr() built-in function uses __repr__ to display the object.


# We can also express our desired data structure as a Python class UserDatabase with four methods:
# insert, find, update and list_all.
class UserDatabase:
    def __init__(self):
        self.list_of_users = []

    def insert(self, user):
        if len(self.list_of_users) == 0:
            print(self.list_of_users)
            self.list_of_users.append(user)

        elif user in self.list_of_users:
            print('This name already exists in the list of users')
        else:
            self.list_of_users.append(user)
    # print(list_of_users)

    def find(self, username):
        for user in self.list_of_users:
            if user.username == username:
                return user  # , print('Username: ' + user.username + ', Name: ' + user.name + ', Email: ' + user.email)
        print('Object is not in users list')

    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email
        print('Username: ' + target.username + ', Name: ' + target.name + ', Email: ' + target.email)

    def list_all(self):
        return print(self.list_of_users)


# Example user input
aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')

users = [aakash, biraj, hemanth, jadhesh, siddhant, sonaksh, vishal]

# print(aakash.__dict__['username'])

# i forgot to create an instance of a class!!!
database = UserDatabase()
for i in users:
    database.insert(i)

print()
print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
print()

database.find('sonaksh')

database.update(User(username='siddhant', name='Siddhant U', email='siddhantu@example.com'))
# database.list_all()
#
#
#
# for i in range(len(users)):
#     print(database.list_of_users[i].__dict__['name'])

# print(database.list_of_users[6].__dict__['name'])

# We store the User instances in a list sorted by usernames
# Insert: Loop through the list and add the new user at a position that keeps the list sorted
# Find: Loop through the list and find the user object with the username matching the query
# Update: Loop through the list, find the user instance matching the query and update the details
# List: Return the list of user object

