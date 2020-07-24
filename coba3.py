# All accounts
users = {
    "root": {
        "password": "gucci-mane",
        "group": "admin",
        "mail": []
    }
}

# Form validation
def validate(form):
    if len(form) > 0:
        return False
    return True
	
print()