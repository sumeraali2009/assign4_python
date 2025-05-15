def main():
    # Prompt user to enter temperature in Fahrenheit
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    
    # Convert to Celsius using the formula
    celsius = (fahrenheit - 32) * 5.0 / 9.0

    # Display the result
    print(f"The temperature in Celsius is {celsius:.2f}°C")

# Call main when script is run
if __name__ == '__main__':
    main()
