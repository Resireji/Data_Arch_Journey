#Loops
total_no_of_ages = int(input("How many total ages do you want to enter? "));
ages=[]
count = 0;
while count < total_no_of_ages:
    age = int(input("What is the age of person: "));
    ages.append(age);
    count += 1;
child = 0;
teenager = 0;
adult = 0;
senior = 0;
for age in ages:
    if age <=13:
        child += 1;
    elif age <= 20:
        teenager += 1;
    elif age <= 65:
        adult += 1;
    else:
        senior += 1;
print(f"Hi, There are {child} children, {teenager} teenagers, {adult} adults and {senior} seniors.")
