# Nada, James, Sadi of Soup Sharks
# SoftDev
# Oct 2022

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   #Pred: Both this and the above print statement will appear in the terminal; Pred was right
    return "No hablo queso!"

app.run()
<<<<<<< HEAD
=======

>>>>>>> 4f7fb035e718d08d9243a815e326fb9d2fed379d
