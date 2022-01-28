def any_weather_alert(season, temp, action):
    print(season, "Warning!")
    print("Temperatures will be", temp)
    print("Make sure to", action)


any_weather_alert("Summer", "above 100 degrees.", "go swimming!")



# Add parameter to function and include in print statement
# to print "My favorite color is `color`"

def my_favorite_color(color):
    print("My favorite color is", color)


# Call function and pass in argument with your favorite color
my_favorite_color("blue")
