
def farenheit_to_celcius():

    #Fahrenheit --> Celsius --> Kelvin

    #instructions 
    print("Welcome! You can use this calculator to convert Fahrenheit to Celsius.")
    print("This calculator takes it a step further and converts your Celsius output into Kelvin")

    #setting the variable fahrenheit to input so the user can enter a value in terminal
    #and set the value for the variable fahrenheit
    fahrenheit = int(input("Please enter you Fehrenheit value here: "))

    #The variable "celsius_conversion", holds the conversion factor 
    celsius_conversion = ((fahrenheit - 32) * 5/9)
    #The variable "celsius_result" will store the value returned from "celsius_conversion"
    #This value can be used when caluculating Celsius to Kelvin
    celsius_result = celsius_conversion 

    #Lastly, we print out a sttring and the value stored in "celsius_result"
    print("You Fahrenheit value converted to Celsius is: ", celsius_result)

    #Now we repeat this process to convert Celsius to Kelvin
    kelvin1 = celsius_result + 273.15
    print("Your Celsius output converted to Kelvin is:  ", kelvin1)

#Now repeat the steps for Celcius to Fahrenheit
def celcius_to_fahrenheit():

    #Celsius --> Fahrenheight --> Kelvin
    print("Welcome! You can use this calculator to convert Celsius to Fahrenheit.")
    print("This calculator takes it a step further and converts your Fahrenheit output into Kelvin")
    celsius = int(input("Please enter you Celsius value here: "))
    fahrenheit_conversion = ((celsius * 9/5) + 32)
    fahrenheit_result = fahrenheit_conversion

    print("You Celsius value converted to Fahrenheit is: ", fahrenheit_result)

    kelvin2 = ((fahrenheit_result  - 32) * 5/9) + 273.15
    print("Your Fahrenheit output converted to Kelvin is:  ", kelvin2)


#Created an if statement to give the user options as to what calculator they want to use
print("1: Fahrenheit to Celsius")
print("2: Celsius to Fahrenheit")
inp = int(input("Hi there! Which calculator will you be using today?: "))

#If they choose option 1...
if inp == 1:
    # run the code in farenheit_to_celcius() function
    inp = "Fahrenheit to Celsius"
    farenheit_to_celcius()
# But if they choose option 2...
elif inp == 2:
    # run the code in celcius_to_fahrenheit() function
    inp = "Celsius to Fahrenheit"
    celcius_to_fahrenheit()
# If they type a random int, it will print "Invalid input!"
else:
    print("Invalid input!")
