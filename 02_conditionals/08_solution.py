password = "g1232123b"

if len(password) <= 6:
    print("Password is weak.")
elif len(password) >= 7 and len(password) <= 10:
    print("Password is medium.")
elif len(password) >= 10:
    print("Password is strong.") 



