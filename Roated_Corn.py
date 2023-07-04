Total_Scores = 0
Counter = 0
grade = int(input('enter grade or -25 to end: '))
while grade != -25:
    if grade != 25:
        Total_Scores += grade
        Counter += 1
    grade = int(input('enter grade or -25 to end: '))
if Counter != 0:
    average = Total_Scores//Counter
    print("""********************************************************************************
                Aso Rock Secondary School, Abuja Nigeria                       
********************************************************************************
Class: SSS3""")
    print('Number Of Student in class:', Counter)
    print('Total Scores:', Total_Scores)
    print('Average Score: ', average,)
    print('********************************************************************************')
