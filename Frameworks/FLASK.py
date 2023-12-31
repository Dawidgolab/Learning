"""
CREATING A SERVER:
1.
# we install the FLASK and next we import FLASK and render_template from flask.

-->  __name__ -> In practice, when you use __name__ in the context of a Flask application,
it is often used in the construction of a web application to determine(ustalic) the location of folders
where HTML templates, static files, etc. are located.

-->  template_folder and static_folder -> template_folder specifies the folder where the application's
HTML templates are located (in this case '../html'),
and static_folder is the folder where static files such as CSS stylesheets,
images, etc. are located. (in this case '../css').

--> @app.route("/home") -> The @app.route decorator defines the URL that will be served by the function
below which we will enter what exactly it should do on a given page .

--> return render_template('MainPage.html') -> The render_template function renders an HTML template
named 'MainPage.html'. This template will be displayed as a response to an HTTP request to "/home"

--> if __name__ == "__main__": -> A condition that checks whether the file was run directly
(and not imported as a module from another file).

--> app.run(debug=True) -> Starts the Flask application. The debug=True parameter turns on debug mode,
which allows more detailed error information to be displayed and makes it easier to debug
the application.

2. if we want to check our server then we make this steps in terminal:
-> set FLASK_APP=Name_of_the_file
-> set FLASK_ENV=develompment
-> we can run a program to check the server -> python file_name

3. Error 304
If you see multiple 304 response codes for static files,
such as JavaScript (button-start.js) and CSS (MainPage.css),
it means that the browser tried to download these files, but received a response that the files
have not been modified since the last so download, they are already in the browser cache


///////////!!!!!!!!!!SAMPLE py. Flask CODE!!!!!!!!!//////////////////////

from flask import Flask,render_template

app=Flask(__name__,template_folder='../html',static_folder='../css')


@app.route("/home")
def home():
    return render_template('MainPage.html')

@app.route('/klient/<number>')
def klient(number):
    return f' The client with number {numer} is ....'

@app.route('/add/<zmienna1>+<zmienna2>')
def dodaj(zmienna1,zmienna2):
    sum = int(zmienna1) + int(zmienna2)
    return f'suma liczb: {zmienna1} + {zmienna2} = {sum}'| --------> wwe write on the page /add/2+3


if __name__=="__main__":
    app.run(debug=True)


/////////////////////////////////////////////////////////////////
"""


