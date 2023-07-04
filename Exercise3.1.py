passes = 0
failures = 0
unwantedScores = 0
gradeCounter = 1
while gradeCounter < 11:
    grade = int(input("Enter 1 for pass and 2 for failures: "))
    if grade == 1:
        passes += 1
        gradeCounter = gradeCounter + 1
    elif grade == 2:
        failures += 1
        gradeCounter = gradeCounter + 1
    else: unwantedScores += 1
print("Number of passes: ", passes, "Number of failures: ", failures)
