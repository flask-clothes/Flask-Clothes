from flask import Flask, render_template, url_for, request, make_response, redirect


app = Flask(__name__)

token = "ssrToken"

users = {
    'joao': "2708",
    "vih": "0305"
}


class Clothe:

    def __init__(self, id, name, price, ctg, imgurl):
        self.id = id
        self.name = name
        self.price = price
        self.ctg = ctg
        self.imgurl = imgurl

    def getPrice(self):
        return self.price

    def getName(self):
        return self.name


ctgs = [
    'sport',
    "expensive",
    "cold",
    "all",

]

clothes = [
    Clothe(2, "Moletom Cinza", 200, "expensive",
           "/static/assets/products/grey.jpeg"),
    Clothe(1, "Nike Shoes", 50, "sport",
           "/static/assets/products/green_nike_shoes.jpeg"),
    Clothe(3, "Camisa de compressão Nike", 150, "cold",
           "/static/assets/products/nike_compression_tshirt.jpeg"),
    Clothe(4, "Calça Jogger da Puma", 100, "cold",
           "/static/assets/products/puma_jogger.jpeg"),
    Clothe(5, "Camisa do Corinthians", 100, "sport",
           "/static/assets/products/corinthians_tshirt.png"),
    Clothe(6, "Strap", 100, "sport", "/static/assets/products/strap.jpeg")
]


@app.route("/ssr", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        ctg = request.form.get("ctg")
        filteredclothes = []
        for clothe in clothes:
            if clothe.ctg == ctg:
                filteredclothes.append(clothe)
        if ctg == "all":
            filteredclothes = clothes
        return render_template("index.html", clothes=filteredclothes, ctgs=ctgs, bannerClothes=clothes)
    return render_template('index.html', clothes=clothes, ctgs=ctgs, bannerClothes=clothes)


@app.route("/login", methods=["POST", "GET"])
def login():
    method = request.method
    if method == "POST":
        name = request.form.get("name")
        password = request.form.get("password")
        print(password, name)
        if ((name in users.keys()) and password == users[name]):
            resp = make_response(redirect(url_for("home")))
            resp.set_cookie("token", token, 60)
            return resp
        msg = "Ops, você errou algum campo, tente novamente"

        return render_template("login.html", msg=msg)
    return render_template("login.html")


@app.route("/")
def default():
    return redirect(url_for("login"))


@app.route("/ssr/clothe/<id>")
def info(id):
    print(id)
    selected_clothe = clothes[0]
    for clothe in clothes:
        print("Clothe id:", clothe.id)
        print("Clothe id:", clothe.id, id)
        print(clothe.id == id)
        if int(clothe.id) == int(id):
            print("hi")
            selected_clothe = clothe
            return render_template('clothe.html', clothe=selected_clothe)

    return redirect(url_for('home'))


@app.route("/deletecookies")
def deletingcookies():
    resp = make_response(redirect(url_for("login")))
    resp.delete_cookie("user")
    resp.delete_cookie("user")
    return resp


if __name__ == "__main__":
    app.run(debug=True)
