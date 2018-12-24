import validation as val
def entering():
    number = input("Enter number:")
    answer = input("Want to exit ?('yes',something else)")
    if(not val.int_valid(number)):
        print("Enter sommething that more 'intrative' =)")
        return entering()
    else:
        if(answer == "yes" or answer == "Yes"):
            return number
        return number+"/"+entering()



numbers_string = entering()
numbers_list = numbers_string.split("/")
numbers_list.reverse()
result = ""
for i in numbers_list:
    result += i +" "
print(result)

