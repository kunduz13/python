# Get user input
my_name = input("Enter your name: ")
fave_food = input("Enter your favorite food: ")
fave_season = input("Enter your favorite season: ")

# Text with placeholders
text = "Hello! My name is <my_name>. My favorite food is <fave_food>, and my favorite season is <fave_season>."

# Replace placeholders with user variables
text = text.replace("<my_name>", my_name)
text = text.replace("<fave_food>", fave_food)
text = text.replace("<fave_season>", fave_season)

# Print the updated text
print(text)
