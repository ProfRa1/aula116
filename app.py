from flask import Flask
app = Flask(__name__)
@app.route("/")
def first_flask():
    return "primeira tentativa"
@app.route("/flask2")
def second_flask():
    return "segunda"
if __name__ == "__main__":
    app.run(port=8080)
