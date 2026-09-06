#Functions
def age_classification(age ):
        if age <= 13:
            return "Child";
        elif age <= 20:
            return "Teenager";
        elif age <= 65:
            return "Adult";
        else:
            return "Senior";
ages = []
count = 0;
entries = int(input("How many entries: "))
while count < entries:
    ages.append(int(input("What is the age? ")))
    count += 1;
#print ("\n".join(result))
child = 0
teenager = 0
adult = 0
senior = 0
for age in ages:
    category = age_classification(age)
    if category == "Child":
        child = child + 1
    elif category == "Teenager":
        teenager = teenager + 1
    elif category == "Adult":
        adult += 1
    else:
        senior += 1
print (f"Child: {child}, Teenager: {teenager}, Adult: {adult}, Senior: {senior}")
