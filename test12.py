Name = input("Enter the name of the student: ")
Famili = input("Enter the famili of the student: ")
score1 = float(input("Enter the score of a course: "))
score2 = float(input("Enter the score of a course: "))
score3 = float(input("Enter the score of a course: "))
status = ""
Avg = (score1 + score2 + score3) / 3 
if Avg >= 17 :
    status = "greate"
if 12<=Avg<17 :
    status = "normal"
if Avg <12 :
    status = "fail"
print(f"{Name} {Famili} is a student with educational status {status}.")