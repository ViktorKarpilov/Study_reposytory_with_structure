
def translation():
    input_minutes = int(input("Enter pleas minutes: "))
    hours = input_minutes//60
    result_hours = hours - (hours//24)*24
    result_minutes = input_minutes - hours*60
    result = str(result_hours) +"Hours and "+str(result_minutes) +"Minutes"
    print(result)
try:
    translation()
except:
    print("Something wrong")
    translation()
    

