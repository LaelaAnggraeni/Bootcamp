# On start
print("Welcome ")
print("Options: login | logout")
while True:
    option = input("> ")
    if option == "login":
        login()
    elif option == "logout":
        break
    else:
        print(option + " is not an option")

# On logout
print("bye bye")
time.sleep(1)