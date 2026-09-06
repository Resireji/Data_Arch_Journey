#Lists
ages = [];
total_no_ages = int(input("How many total ages do you want to enter? "));
count = 0;
while(count < total_no_ages):
    age = int(input("What is your age?"));
    ages.append(age);
    count += 1;
print("You have entered", len(ages), "ages.")
ages_in_order = sorted(ages);
print("Youngest: " ,ages_in_order[0], " ; Oldest: ", ages_in_order[-1]);
print("Ages in order: ", ages_in_order);
print("Original list: ", ages);
age_seeking = int(input("What age are you looking for? "));
found = False;
for check in ages:
    if check == age_seeking:
        found = True
        break
if found:
        print(f"{age_seeking} is present in the list");
else:
        print(f"{age_seeking} is not present in the list");
ages.pop(0);
print(ages);