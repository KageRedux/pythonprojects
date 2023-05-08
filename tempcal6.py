import time

def main():
    print("Temp Cal ver 1.6")
    end = False
    while not end:
        quit = input("To quit this program, enter 'Q', or press 'Enter' to continue\n")
        if quit.lower() == "q":
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
            convert_temp(unit, temp)

def c_to_f(celsius):
    fahrenheit = (celsius * 1.8) + 32 
    return fahrenheit

def c_to_k(celsius):
    kelvin = celsius + 273.15
    return kelvin

def f_to_c(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9 
    return celsius

def f_to_k(fahrenheit):
    kelvin = (fahrenheit + 459.67) * 5/9 
    return kelvin

def k_to_c(kelvin):
    celsius = kelvin - 273.15 
    return celsius

def k_to_f(kelvin):
    fahrenheit = (kelvin * 1.8) - 459.67 
    return fahrenheit

def convert_temp(unit, temp):
    unit = unit.lower()
    if unit == "c":
        convert = input("What do you want to convert to? Kelvin (K) or Fahrenheit (F)? \n").lower()
        if convert == "f":
            fahrenheit = c_to_f(temp)
            print(f"{temp:.2f}° Celsius is {fahrenheit:.2f}° Fahrenheit \n")
        elif convert == "k":
            kelvin = c_to_k(temp)
            print(f"{temp:.2f}° Celsius is {kelvin:.2f}° Kelvin \n")
        else:
            print("Cannot make that conversion")
    elif unit == "f":
        convert = input("What do you want to convert to? Celsius (C) or Kelvin (K)? \n").lower()
        if convert == "c":
            celsius = f_to_c(temp)
            print(f"{temp:.2f}° Fahrenheit is {celsius:.2f}° Celsius")
        elif convert == "k":
            kelvin = f_to_k(temp)
            print(f"{temp:.2f}° Fahrenheit is {kelvin:.2f}° Kelvin")
        else:
            print("Cannot make that conversion")
    elif unit == "k":
        convert = input("What do you want to convert to? Fahrenheit (F) or Celsius (C)? \n").lower()
        if convert == "c":
            celsius = k_to_c(temp)
            print(f"{temp:.2f}° Kelvin is {celsius:.2f}° Celsius")
        elif convert == "f":
            fahrenheit = k_to_f(temp)
            print(f"{temp:.2f}° Kelvin is {fahrenheit:.2f}° Fahrenheit")
        else:
            print("Cannot make that conversion")
    else:
        print(f"Currently Unsupported unit of measurement '{unit.upper()}'")

if __name__ == "__main__":
    main()