import re
pause = input()
pattern_int = r"^[-\d]\d*$"
user_input=''
result_int = 0

while (not re.match(pattern_int,user_input)):
	user_input = input("Enter integer 1:")
result_int += int(user_input)
user_input=''

while (not re.match(pattern_int,user_input)):
	user_input = input("Enter integer 2:")
result_int += int(user_input)
user_input=''

while (not re.match(pattern_int,user_input)):
	user_input = input("Enter integer 3:")
result_int += int(user_input)

  
print(result_int)
