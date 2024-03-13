import turtle
import pandas


screen = turtle.screen()
screen.setup(width=1200, height=600)
screen.title("guess turkish cities")
image = "turkish_map.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("cities_with_coordinates.csv")

count = 0
guessed_cities = []
while len(guessed_cities) < 81:
    guess = screen.textinput(title=f"{count}/81 Correct", prompt="Guess a city")
    guessed_city = data[data["Cities"] == guess.strip().lower().capitalize()]
    if (len(guessed_city["Coordinates"].to_list()) != 0 and
            not guessed_cities.__contains__(guessed_city["Cities"].to_list()[0])):
        guessed_cities.append(guessed_city["Cities"].to_list()[0])
        count += 1
        import ast

        string_data = guessed_city["Coordinates"].to_list()[0]
        dictionary_data = ast.literal_eval(string_data)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(dictionary_data["x"]), int(dictionary_data["y"]))
        t.write(guessed_city["Cities"].to_list()[0])

guess = screen.textinput(title=f"You won!!!", prompt="Well played :)")
