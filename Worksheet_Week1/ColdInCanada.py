"""
Defines a function ColdInCanada()

Takes the inputs and performs the conversions to determine if it is under or over the cold threshold.
"""
def ColdInCanada():
    # Asks what the threshold is to be considered cold in Canada (celcius).
    C_Threshold = int(input("What is the threshold for cold in celcius?: "))
    # Asks what the temperature is today in Farenheit.
    F_Today = eval(input("What is the temperature in Farenheit today?: "))
    # Takes the Farenheit input and converts it to cecius in a new variable.
    C_Today = (F_Today -32) * 5 / 9
    # Creates the condition where if today's converted temperature in celcius is less that or equal to the threshold
    if C_Today <= C_Threshold:
        print("It is cold in Canada today.")
    # If the condition is not met it is not cold in Canada today.
    else:
        print("It is not cold in Canada today.")
ColdInCanada()