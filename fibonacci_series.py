while True:

    n = int(input("Enter the length of the Fibonacci series: "))

    # define the first two numbers in the series
    a, b = 0, 1
    count=0
    while True:
        # check if the lenth is valid
        if n<=0:
            print("Enter positive integer!!!")
            
        # if there is only 1, return "a"
        elif n==1:
            print("Fibonnaci series upto ",n,":",a)
            
        #loop to generate the series up to n
        else:
            print("Fibonacci sequence:")
        while count < n:
            print(a)
            nth = a + b
            # update values
            a = b
            b = nth
            count += 1  
        break      
    
   