name = input("Please enter your name. ")
age = input("Now please enter you age. ")

username = name + age
print ("Your username has been created and is", username, ".")

password = input("Now please create a password. ")

file = open("Login.txt","a")

print ("Your login details have been saved. ")