#program will continue to run until end becomes True
end = False
while end == False:
    quit = input("To quit this program, enter 'Q', or press any key to continue\n")
    if quit == "Q".casefold():
        end = True
        print("Program Terminated")
        break
    else:
        temp = float(input("Enter the temperature \n"))
        unit = input("Celsius(C) or Fahrenheit(F)? \n")
        celsius = (temp - 32) * 5/9 
        # can also multiply by .5555(.56) if doing manually, or to keep consistency of decimals
        fahrenheit = (temp * 1.8) + 32
        F = celsius
        C = fahrenheit 
        if unit == "C".casefold():
            print(f"{temp}° Celsius is {C}° Fahrenheit")

        elif unit == "F".casefold():
            print(f"{temp}° Fahrenheit is {F}° Celsius")

        else:
            print(f"Unsupported unit of measurement '{unit}'")

#eventually add support for other units of measurements such as kelvin(?)