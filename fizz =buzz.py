def fizzbuzz(num):
    for i in range(1,int(num)):
        if ((i%3)==0)and((i%5)==0):
            print("fizzbuzz")
        elif (i%3)==0:
            print("fizz")
        elif (i%5)==0:
            print("buzz")
        else:
            print(i)
print("pick a number")
number = input()
fizzbuzz(number)
