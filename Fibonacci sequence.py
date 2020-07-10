number = int(input("Enter a number: ")) #The code will run until the sequence becomes larger than the inputted value

fib1 = 0
fib2 = 1

while fib2 < number:
    a = fib1 + fib2
    fib1 = fib2
    fib2 = a
    print(fib1)
    
