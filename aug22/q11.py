exam_str_date = '(11,12,2014)'


def date(date1):
    dd = ''
    for x in range(len(date1)):
        if date1[x] != "," and date1[x] != ')' and date1[x] != '(':
            dd += date1[x]
        if date1[x] == ',':
            dd += '/'
    print(dd)


date(exam_str_date)
