# https://adventofcode.com/2020/day/4
f1 = open("adventlist4.txt", "r")
passport_str = f1.read()
my_passport = passport_str.split("\n\n")
# created an array of the required passport information
required_info = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
# setting the invalid counter to 0
invalid_counter = 0
for i in range(0, len(my_passport)):
    # replacing new lines with spaces and then eliminated leading and trailing spaces with strip function
    my_passport[i] = my_passport[i].replace("\n", ' ').strip()
    passport_details = my_passport[i].split(" ")
    # creating a empty array of passport info
    passport_info = []
    for j in range(0, len(passport_details)):
        # taking the first part of the of passport details; in this case the passport info
        passport_info.append(passport_details[j].split(":")[0])
    # Check if this passport is not valid
    for k in range(0, len(required_info)):
        if required_info[k] not in passport_info:
            invalid_counter += 1
            break
    # delete list after every for loop to start over
    del passport_details
    del passport_info
print(invalid_counter)
print(len(my_passport))
print(len(my_passport)-invalid_counter)
