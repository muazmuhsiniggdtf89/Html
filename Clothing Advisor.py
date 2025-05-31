#Clothing Advisor Program

#Temperature from the user
temperature = float(input("Enter the current temperature in °C: "))

# Suggest clothing based on temperature
if temperature < 10:
    print("It's too cold! Should wear a jacket and pullover.")
elif 10 <= temperature <= 20:
    print("It's a bit chilly. Should wear a sweater or hoodie.")
elif 21 <= temperature <= 30:
    print("Nice weather! Can wear light and soft clothes.")
else:
    print("It's hot! Should wear very light clothes and stay hydrated.")
