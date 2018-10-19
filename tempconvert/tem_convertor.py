#!/usr/bin/python

ans = input("Enter the temperature you want to convert and which type to convert to.\nExample:'-273K to C'(K for Kelvin C for Celsius F for fahrenheit\n>>")
while True:
    if ans.lower() == "q":
        break
    given_temp = ans.split("to")[0][0:-1]
    print(given_temp)
    temp_type = given_temp[-1]
    if given_temp[0] == "-":
        temp = - int(given_temp[1:-1])
    elif given_temp[0] == "+":
        temp = - int(given_tem[1:-1])
    else:
        temp = int(given_temp[0:-1])
    
    print("Temp:",temp)
    print("Given temp type:",temp_type)
    convert_type = ans.lstrip(" ")[-1] 
    print("convert_type",convert_type)
    if temp_type == "K" and convert_type == "C":
        new_temp = temp - 273.15
    
    elif temp_type == "C" and convert_type == "K":
        new_temp = temp + 273.15
    
    elif temp_type == "F" and convert_type == "C":
        new_temp = (temp - 32)*5/9
    
    elif temp_type == "C" and convert_type == "F":
        new_temp = (temp*9/5) + 32

    elif temp_type == "F" and convert_type == "K":
        new_temp = (temp + 459.67)*5/9 

    elif temp_type == "K" and convert_type == "F":
        new_temp = temp*9/5 - 459.67
    else:
        break
    print(f"{temp} degrees of {temp_type} is {new_temp} degrees of {convert_type}")
    ans = input(">>")
