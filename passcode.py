import random
chars = "1qaz2wsx3edc4rfv5tgb6yhn7ujm8ik,9ol.0p;/-['=]!QAZ@WSX#EDC$RFV%TGB^YHN&UJM*IK<(OL>)P:?_{+}|\""
length = int(input("Enter the length of the password: "))
password = ""
for a in range(length):
  password += random.choice(chars)

print(password)
