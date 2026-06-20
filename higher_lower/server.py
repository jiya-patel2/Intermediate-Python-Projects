from flask import Flask
from random import randint

# Make server
app = Flask(__name__)

# Home page
@app.route('/')
def home_page():
    return "<h1>Guess a number between 0 to 9</h1>" \
            '<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExanJmbm41MHBhOTIwZHU0anJ4ZzNhN3Btb3phaTBzbWp5ZXc3Mm8wMiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/JdFEeta1hLNnO/giphy.gif" width= 300>'
# choose random number
number = randint(0,9)
print(number)
# compare numbers
@app.route('/<int:guess_number>')
def compare_number(guess_number):
    if number == guess_number:
        return '<h2  style="color:green">Correct Guess</h2>'\
               '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcjU5eDBhaGhiemg0amk2bW82YWpjanMwcmVkamVkaTY2eWJ5enAyNiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/MMquV2oInK40V86Q7g/giphy.gif" width= 300>'
    
    elif number < guess_number:
        return '<h2 style="color:purple">Too high<h2>'\
               '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcjU5eDBhaGhiemg0amk2bW82YWpjanMwcmVkamVkaTY2eWJ5enAyNiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/M9C8PHLkh0hQxraaLG/giphy.gif" width= 300>'
    
    elif number > guess_number:
        return '<h2  style="color:red">Too low<h2>'\
               '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcjU5eDBhaGhiemg0amk2bW82YWpjanMwcmVkamVkaTY2eWJ5enAyNiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/f54Or4wFysQ7vVGeKb/giphy.gif" width= 300>'
    
    else :
        return '<h2>Invalid input<h2>'\
               '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcjU5eDBhaGhiemg0amk2bW82YWpjanMwcmVkamVkaTY2eWJ5enAyNiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/pY8jLmZw0ElqvVeRH4/giphy.gif" width= 300>'
    
if __name__ == "__main__":
    app.run()

