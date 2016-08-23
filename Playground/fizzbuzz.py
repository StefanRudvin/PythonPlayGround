
def fizzbuzz(x,y,n):
    for number in range(0,n+1):
        if number % x == 0:
            if number %y == 0:
                print("fb", end=" ")
            else:
                print("f", end=" ")
        elif number % y == 0:
            print("b", end=" ")
        else:
            print(number, end=" ")

print(fizzbuzz(3,5,20), end="")

sum = 0

for number in range(1,1001):
    if number % number == 1:
        pass
    else:
        sum += number

print(sum)
