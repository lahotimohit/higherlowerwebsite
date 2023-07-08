from flask import Flask
import random

app = Flask(__name__)
@app.route("/")
def home_page():
    return '<h1 style= "text-align: center">Guess a number between 0 and 9</h1>' \
           '<img src ="https://i.giphy.com/3o7aCSPqXE5C6T8tBC.gif"">' \
           ''


number = random.randint(0,9)
@app.route("/<u_number>")
def result(u_number):
    user_number = int(u_number)
    if user_number < number:
        return '<h1 style= "color: red">Too low, try again!</h1>' \
               '<img src="https://media.giphy.com/media/TgmiJ4AZ3HSiIqpOj6/giphy.gif">'
    elif user_number > number:
        return '<h1 style= "color: purple">Too high, try again!</h1>' \
               '<img src="https://media.giphy.com/media/2cei8MJiL2OWga5XoC/giphy.gif">'
    else:
        return '<h1 style= "color: green">You found me!</h1>' \
               '<img src = "https://media.giphy.com/media/SSE36LAhb1m9dHz7HI/giphy.gif">'

if __name__ =="__main__":
    app.run(debug=True)