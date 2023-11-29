import random
chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()"
length = int(input("Enter the length of the password: "))
password = ""
for a in range(length):
  password += random.choice(chars)

print(password)