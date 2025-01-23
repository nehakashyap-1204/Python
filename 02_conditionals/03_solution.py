score = 50

if score >= 101:
    print("Please verify your grade again")
    exit()

if score >= 90 and score <= 100:
    grade = "A"
elif score >= 80 and score <= 89:
    grade = "B"
elif score >= 70 and score <= 79:
    grade = "C"
elif score >= 60 and score <= 69:
    grade = "D"
else: grade = "E"

print("Grade :" ,grade)