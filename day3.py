#conditionals
name = input("what is your name: ");
age = int(input("what is your current age?"));
if age <= 13:
    print(f"Hi {name}, you are {age} years old & you are a child.");
elif age<= 20:
    print(f"Hi {name}, you are {age} years old & you are a teenager.");
elif age <= 65:
    print(f"Hi {name}, you are {age} years old & you are an adult.");
else:
    print(f"Hi {name}, you are {age} years old & you are a senior.");