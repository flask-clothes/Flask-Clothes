from flask import Flask, render_template, url_for, request, make_response, redirect


app = Flask(__name__)

class Clothe:

    def __init__(self,id,name,price,ctg):
        self.id = id
        self.name = name
        self.price = price
        self.ctg = ctg

    def getPrice(self):
        return self.price
    def getName(self):
        return self.name


clothes = [Clothe(1,"NikeM4",50,"sport"),Clothe(2,"Zara",200,"expensive"),Clothe(3,"North Ocean",150,"cold")]


@app.route("/ssr")
def home():
    return render_template('index.html',clothes=clothes)

@app.route("/ssr/clothe/<id>")
def info(id):
    print(id)
    selected_clothe = clothes[0]
    for clothe in clothes:
        print("Clothe id:" ,clothe.id)
        print("Clothe id:" ,clothe.id, id)
        print(clothe.id == id)
        if int(clothe.id) == int(id):
            print("hi")
            selected_clothe = clothe
            return render_template('clothe.html',clothe=selected_clothe)

    return redirect(url_for('home'))
    
    


if __name__ == "__main__":
    app.run(debug=True)