#program to check if a number is prime or not
num1=int(input("Enter a number: "))
count=0
if num1<=1:
    print(num1, "not a prime number!")
elif num1>1:
    #checking factors now starting the loop from 2 till the number
    for i in range(2,num1):
        if (num1%i)==0:
            #factor is found, increase count
            count=count+1
            break
            #breaking out of loop
    #if a factor is found, count will be more than1
    if count>=1:
        print(num1,"is not prime!")
    else:
        print(num1, "is prime!")


