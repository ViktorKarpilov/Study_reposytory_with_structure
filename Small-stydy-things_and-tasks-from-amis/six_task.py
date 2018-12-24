def distribution(number):
    return number//2 + number%2
first = int(input("Enter numbers in first groop"))
second = int(input("Enter numbers in second groop"))
third = int(input("Enter numbers in third groop"))
print("For first groop we neeed:"+str(distribution(first)))
print("For second groop we neeed:"+str(distribution(second)))
print("For third groop we neeed:"+str(distribution(third)))
