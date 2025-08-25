# Esse é o modelo ssr

## Os dados são processados em

```python
clothes = [Clothe(1,"NikeM4",50,"sport"),Clothe(2,"Zara",200,"expensive"),Clothe(3,"North Ocean",150,"cold")]


@app.route("/ssr")
def home():
    return render_template('index.html',clothes=clothes
```

## E carregados:
```html
{% for clothe in clothes %}
            <div class="clothe__card" style="width: 150px;padding: 10px; height: 200px;background-color: aliceblue; color: antiquewhite;border-radius: 8px; display: flex;flex-direction: column; gap: 10px;justify-content: space-between;">
                <div class="title" style="font-size: 12px; height: 50px;">
                    <h1>{{ clothe.name }}</h1>
                </div>
                <div class="price" style="color: green;">
                <p>{{ clothe.price }}</p>
                </div>
                <div style="display: flex;justify-content: center;">
                    <a href="/clothe/{{clothe.name}}">
                    <button class="card__button" >Comprar</button>
                    </a>
                </div>    
            </div>
```

# Feito em Flask