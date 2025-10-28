age = int(input("Enter your age: "))

if age < 13:
    print("You are a kid.")
elif age < 20:
    print("You are a teenager.")
elif age > 50:
    print("You are old.")
else:
    print("You are an adult")