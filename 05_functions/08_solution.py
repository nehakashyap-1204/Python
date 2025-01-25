def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(firstname = "neha", lastname = "kashyap")
print_kwargs(firstname = "neha")
print_kwargs(firstname = "neha", lastname = "kashyap", age = 22)

