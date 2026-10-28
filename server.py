import random
from flask import Flask
from functools import wraps

app = Flask(__name__)
secret_number = random.randint(0,9)

@app.route('/')
def game_instruction():
    return "<h1>Guess a number between 0 and 9</h1>"

#logic to generate the random number and validate it from the guessed one
#decorator func

@app.route("/<int:guessed_number>")
def input_number(guessed_number):
    if guessed_number == secret_number:
        return "You guessed it right!"
    else:
        return "Your guess is wrong!"




if __name__ =="__main__":
    app.run(debug=True)


