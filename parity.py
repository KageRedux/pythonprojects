import time

#check if number is even or odd
def parity():
    n = int(input("n: "))
    if n % 2 == 0:
        print("even")
    else:
        print("odd")
        
end = False
while end == False:
    #runs program until told to quit
    quit = input("Enter 'Q' to quit this program, or press any key to continue \n")
    
    if quit == "Q".casefold():
       end = True
       print("Program is being terminated...")
       time.sleep(.5)
       print("Program Terminated.")
       break
    
    else:
        print("Continuing to program...")
        time.sleep(.5)
        parity()