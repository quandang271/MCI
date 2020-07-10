def fizz_buzz(n):
    if(n%3==0 and n%5==0):
        print("FizzBuzz")
    elif(n%3==0):
        print("Fizz")
    elif(n%5==0):
        print("Buzz")
    else: print(-1)

fizz_buzz(15)
fizz_buzz(6)
fizz_buzz(10)
fizz_buzz(11)