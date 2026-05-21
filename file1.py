# 1) Ask the student if they had a medical cause and store the answer in `medical_cause`.

# (Also clean the input so it becomes either 'Y' or 'N'.)

# 2) If `medical_cause` is 'Y':

# - Print that the student is allowed to attend the exam.

# 3) Otherwise (medical_cause is 'N'):

# a) Ask for the student’s attendance percentage and store it in `atten`.

# b) If `atten` is 75 or more:

# - Print "Allowed"

# c) Else:

# - Print "Not allowed"
medical_cause = input(
    "Do you have a medical condition(answer with y/n): ").lower().strip()[0:1]
if medical_cause == "y":
    print("You are allowed to take the exam")
else:
    atten = int(input("Please enter your attendence percentage: "))
    if atten >= 75:
        print("You are allowed to take the exam")
    else:
        print("Not allowed")
