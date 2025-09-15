from flask import Flask, render_template, url_for, request, make_response, redirect, jsonify, abort


app = Flask(__name__)

myToken = "myToken"

users = {
    'joao': '2708',
    'vih': '0305'
}

ctgs = ["sport", "cold", "expensive", "all"]

reviews = [
    {"user": "Maria P.", "rating": 5, "comment": "O moletom é de ótima qualidade e muito confortável. Chegou super rápido!"},
    {"user": "João C.", "rating": 4, "comment": "Muito bom, mas a cor é um pouco mais escura do que eu esperava."},
    {"user": "Pedro A.", "rating": 5, "comment": "Muito satisfeito com o produto. Chegou certinho e a qualidade é excelente."},
    {"user": "Ana L.", "rating": 4, "comment": "O tênis é lindo, mas demorou um pouco mais que o esperado para ser entregue."},
    {"user": "Carlos P.", "rating": 5, "comment": "Ótima para academia, veste super bem e é bem leve."},
    {"user": "Marta F.", "rating": 4, "comment": "Gostei do produto, mas achei o tamanho um pouco apertado para a minha medida."},
    {"user": "Ricardo P.", "rating": 5, "comment": "Excelente qualidade e um design incrível. Fiel torcedor aprovou!"},
    {"user": "Joana S.", "rating": 5, "comment": "Comprei de presente para o meu pai e ele amou. A entrega foi rápida."},
    {"user": "Felipe R.", "rating": 5, "comment": "Caimento perfeito e muito confortável. Recomendo!"},
    {"user": "Carolina B.", "rating": 4, "comment": "A calça é ótima, mas o elástico da cintura poderia ser um pouco mais firme."},
    {"user": "Lucas P.", "rating": 5, "comment": "Material de ótima qualidade e muito resistente. Me ajudou a aumentar minhas cargas nos treinos!"},
    {"user": "Juliana G.", "rating": 4, "comment": "Funciona muito bem. A única coisa é que poderia ser um pouco mais macio no pulso."}
]


class Clothe:

    def __init__(self, id, name, price, ctg, imgurl, description, reviews_list):
        self.id = id
        self.name = name
        self.price = price
        self.ctg = ctg
        self.imgurl = imgurl
        self.description = description
        self.reviews = reviews_list

    def getPrice(self):
        return self.price

    def getName(self):
        return self.name

    def toDict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "ctg": self.ctg,
            "imgurl": self.imgurl,
            "description": self.description,
            "reviews": self.reviews
        }


clothes = [
    Clothe(2, "Moletom Cinza", 200.00, "cold",
           "assets/products/grey.jpeg", "Este moletom cinza é perfeito para qualquer ocasião. Feito com material 100% algodão, ele oferece conforto e durabilidade, ideal para o dia a dia.", reviews[0:2]),
    Clothe(1, "Nike Shoes", 320.00, "sport",
           "assets/products/green_nike_shoes.jpeg", "Tênis de alta performance da Nike, com design moderno e cores vibrantes. Ideal para quem busca estilo e conforto em um único produto.", reviews[2:4]),
    Clothe(3, "Camisa de compressão Nike", 150.00, "sport",
           "assets/products/nike_compression_tshirt.jpeg", "Camisa de compressão da Nike, ideal para treinos de alta intensidade. Ajuda a manter a temperatura corporal e oferece suporte muscular durante o exercício.", reviews[4:6]),
    Clothe(4, "Calça Jogger da Puma", 75.00, "sport",
           "assets/products/puma_jogger.jpeg", "A calça jogger da Puma oferece conforto e estilo para o seu treino ou dia a dia. Com tecido respirável e design moderno, é uma peça essencial para o seu guarda-roupa.", reviews[8:10]),
    Clothe(5, "Camisa do Corinthians", 350.00, "sport",
           "assets/products/corinthians_tshirt.png", "A camiseta oficial do Corinthians é ideal para mostrar sua paixão pelo time. Feita com tecido leve e respirável, é perfeita para torcer ou para usar no dia a dia.", reviews[6:8]),
    Clothe(6, "Strap", 30.00, "sport", "assets/products/strap.jpeg", "O strap é um acessório essencial para levantamento de peso. Ele aumenta sua aderência, permitindo que você levante cargas mais pesadas com segurança e maximize seu desempenho na academia.", reviews[10:12])
]


@app.route("/")
def default():
    return redirect(url_for("login"))


@app.route("/login", methods=["POST", "GET"])
def login():

    method = request.method
    if method == "POST":
        name = request.form.get("name")
        password = request.form.get("password")
        if ((name in users.keys()) and password == users[name]):
            resp = make_response(redirect(url_for("home")))
            resp.set_cookie("token", myToken, 60*60)
            return resp
        msg = "Ops, você errou algum campo, tente novamente"

        return render_template("login.html", msg=msg)

    return render_template("login.html")


@app.route("/ssr", methods=["POST", "GET"])
def home():
    if request.cookies.get("token") == myToken:
        if request.method == "POST":
            ctg = request.form.get("ctg")
            filtered_clothes = []
            if ctg == "all":
                filtered_clothes = clothes
            else:
                for clothe in clothes:
                    if clothe.ctg == ctg:
                        filtered_clothes.append(clothe)
            return render_template("index.html", clothes=filtered_clothes, ctgs=ctgs, bannerClothes=clothes)
        return render_template("index.html", clothes=clothes, ctgs=ctgs, bannerClothes=clothes)
    abort(403)


@app.errorhandler(403)
def unathorizedPage(error):
    return render_template("403.html")


@app.route("/ssr/clothe/<id>")
def info(id):
    if request.cookies.get("token") == myToken:
        for clothe in clothes:
            if int(clothe.id) == int(id):
                return render_template('clothe.html', clothe=clothe)
        return "Produto não encontrado", 404
    abort(403)


if __name__ == "__main__":
    app.run(debug=True)