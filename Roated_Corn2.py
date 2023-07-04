Total_Scores = 0
for student in range(20):
    grade = int(input('enter grade'))
    Total_Scores += grade
average = Total_Scores//20
print("""********************************************************************************
                Aso Rock Secondary School, Abuja Nigeria                       
********************************************************************************
Class: SSS3""")
print('Number Of Student in class: 20')
print('Total Scores:', Total_Scores)
print('Average Score:', average,)
print('********************************************************************************')
