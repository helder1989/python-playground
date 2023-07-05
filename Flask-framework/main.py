from flask import Flask

app = Flask(__name__)

# criar a 1ª página do site
# route > hastagsilva.com/

@app.route("/")
def homepage():
    return "Esse é o meu site, sejam bem vindos"

@app.route("/rota2")
def rota2():
    return "<H1> Essa é a segunda rota da minha aplicação... </H1>"

# colocar o site no ar

app.run()

