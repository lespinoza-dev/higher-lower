import random
from flask import Flask

app = Flask(__name__)
secret_number = random.randint(0,9)

@app.route('/')
def game_instruction():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src='/static/welcome.gif'>")

#logic to generate the random number and validate it from the guessed one

@app.route("/<int:guessed_number>")
def input_number(guessed_number):
    if guessed_number == secret_number:
        return "<h2>You guessed it right!</h2><img src='/static/correct.gif'>"
    elif guessed_number < secret_number:
        return "<h2>Your guessed number is too low!/h2><img src='/static/too_low.gif'>"
    elif guessed_number > secret_number:
        return "<h2>Your guessed number is too high!</h2><img src ='/static/too_high.gif'>"




if __name__ =="__main__":
    app.run(debug=True)


