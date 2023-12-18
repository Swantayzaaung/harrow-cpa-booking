# Greets user
import socket
from flask import Flask, render_template, request
from socket import socket, AF_INET, SOCK_DGRAM 
from flask_ngrok import run_with_ngrok 

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
run_with_ngrok(app)

@app.route("/")
def index():
    return render_template("index.html", name=request.args.get("name", "world"))


# Run the flask server on the local network
if __name__ == '__main__':
    app.run()
