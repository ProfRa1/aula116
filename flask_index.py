from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

@app.route("/")
def first_flask():
    name = 'Flask'
    #Passe a variável no modelo
    return render_template('index.html', index_variable = name)

if __name__ == "__main__":
    app.run()
