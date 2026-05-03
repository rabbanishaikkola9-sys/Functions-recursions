# a=20
# b=30
# c=10
# avg=(a+b+c)/3
# print(avg)
# a=20
# b=32
# c=13
# avg=(a+b+c)/3
# print(avg)
# a=21
# b=20
# c=89
# avg=(a+b+c)/3
# print(avg)
# The above is manual way
# Using functions
# a=int(input("Enter the number"))
# b=int(input("Enter the number"))
# c=int(input("Enter the number"))
def avg():
    a=int(input("Enter the number"))
    b=int(input("Enter the number"))
    c=int(input("Enter the number"))
    average=(a+b+c)/3
    print(average)


avg()