import time

print("Temp Cal ver 1.5")

end = False
while end == False:
    quit = input("To quit this program, enter 'Q', or press any key to continue\n")
    
    if quit == "Q".casefold():
        end = True
        print("Terminating Program...")
        time.sleep(0.5)
        print("Program Terminated")
        break
    
    else:
        print("Continuing to Program...")
        time.sleep(0.5)
        unit = input("What is your starting unit? Celsius(C), Fahrenheit(F) or Kelvin (K)? \n")
        temp = float(input("Enter the temperature \n"))
        
        #variables
        #fahrenheit to celsius
        celsius = (temp - 32) * 5/9 
        
        #celsius to fahrenheit
        fahrenheit = (temp * 1.8) + 32
        
        #kelvin to celsius
        kelvin1 = temp - 273.15
        
        #kelvin to fahrenheit
        kelvin2 = (temp * 1.8) - 459.67
        
        F = celsius
        C = fahrenheit
        K1 = kelvin1
        K2 = kelvin2
        
        #celsius to kelvin
        CK = celsius + 273.15
        
        #fahrenheit to kelvin
        FK = (fahrenheit + 459.67) * 5/9
        
        #loops
        if unit == "C".casefold():
            convert = input("What do you want to convert to? Kelvin (K) or Fahrenheit (F)? \n")
            if convert == "F".casefold():
                print(f"{temp:.2f}° Celsius is {C:.2f}° Fahrenheit \n")
            elif convert == "K".casefold():
                print(f"{temp:.2f}° Celsius is {CK:.2f}° Kelvin \n")
            else:
                print("Cannot make that conversion")
                
        elif unit == "F".casefold():
            convert = input("What do you want to convert to? Celsius (C) or Kelvin (K) \n")
            if convert == "C".casefold():
                print(f"{temp:.2f}° Fahrenheit is {F:.2f}° Celsius")
            elif convert == "K".casefold():
                print(f"{temp:.2f}° Fahrenheit is {FK:.2f}° Celsius")
            else:
                print("Cannot make that conversion")
                
        elif unit == "K".casefold():
            convert = input("What do you want to convert to? Fahrenheit (F) or Celsius (C)? \n")
            if convert == "C".casefold():
                print(f"{temp:.2f}° Kelvin is {K1:.2f}° Celsius")
            elif convert == "F".casefold():
                print(f"{temp:.2f}° Kelvin is {K2:.2f}° Fahrenheit")
            else:
                print("Cannot make that conversion")
                
        else:
            print(f"Currently Unsupported unit of measurement '{unit}'")