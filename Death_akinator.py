import time, random
from tkinter import messagebox

print("Akinator", "Attention: This program causes physiological problems if you use this improperly")

time.sleep(2)

print("Welcome to Death Akinator...")
time.sleep(1)

print("I will know when you will die...")
date = input("Please enter your birthyear: ")
date = int(date)

today = time.localtime()[0]
age = today-date

if age == 0:
	death = 80
elif age > 0 and age < 14:
	death = random.randint(60, 70)
elif age > 13 and age < 20:
	death = random.randint(50, 60)
elif age > 29 and age < 38:
	death = random.randint(30, 35)
elif age > 37 and age < 54:
	death = random.randint(20, 22)
elif age > 53 and age < 88:
	death = random.randint(10, 20)
elif age > 87 and age < 120:
	death = "Tomorrow"
elif age >= 120:
	death = "You died"

if age > 89 and age < 120:
	death = "Tomorrow"
elif age >= 120:
	death = "You died"

print("You will die in the year...")
time.sleep(0.5)
print("Uhm..")
time.sleep(1)
if death == "Tomorrow" or death == "You died":
	print(death)
else:
	print(today+death)
