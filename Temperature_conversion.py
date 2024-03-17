# ask the user for a temperature with units c or F. your program should convert the temprature to the other unit. the  conversation are F = 9/5*c + 32 and c = 5/9*(F-32)

def celsius_to_fahrenheit(celsius):
    fahrenheit = (9/5) * celsius + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (5/9) * (fahrenheit - 32)
    return celsius

def main():
    temperature = input("Enter the temperature value: ")
    unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ")

    if unit.upper() == 'C':
        celsius = float(temperature)
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {fahrenheit}°F")
    elif unit.upper() == 'F':
        fahrenheit = float(temperature)
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is equal to {celsius}°C")
    else:
        print("Invalid unit. Please enter either 'C' or 'F'.")

if __name__ == "__main__":
    main()



