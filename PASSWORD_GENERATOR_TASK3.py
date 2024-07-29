import random
available_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
password_length = int(input("Enter the size of the password that you want to generate : "))
password = ""

for i in range (password_length):
    password+= random.choice(available_characters)
print (password)