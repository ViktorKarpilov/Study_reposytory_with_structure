from my_library import validation

numbers = validation.list_int_valid()
def Recursivly_sum_tusk1(massive,num=0):
    if(len(massive)>1):
        return Recursivly_sum_tusk1(massive,massive.pop()+num)
    else:
        return num + massive.pop()

def For_sum_tusk1(massive):
    res = 0
    for i in massive:
        res +=i
    return res

def While_sum_tusk1(massive):
    res = 0
    while(len(massive)>0):
        res += massive.pop()
    return res
# def Recursivly_sum_tusk2(massive):
#     res = 0
#     for i in massive:
#         if(len(i))

print(Recursivly_sum_tusk1(numbers))

