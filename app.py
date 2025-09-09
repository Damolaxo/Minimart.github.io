from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.context_processor
def inject_globals():
    return {
        "cart_count": 0,
        "current_year": datetime.utcnow().year,
        "current_user": type("u", (), {"is_authenticated": False, "name":"Guest"})()
    }

@app.route("/")
def index():
    featured = [
        {"id":1,"title":"Classic Shirt","price":29.99,"image_url":"/static/shirt.jpg",
         "short_description":"Cotton shirt","description":"Nice shirt","sku":"CS-001",
         "brand":"BrandA","category":"Clothing","category_slug":"clothing"}
    ]
    categories = [{"name":"Clothing","slug":"clothing"}]
    return render_template("index.html", featured=featured, categories=categories)

@app.route("/products")
def products():
    return render_template("products.html", products=[], pagination=None, category_name=None)

if __name__ == "__main__":
    app.run(debug=True)
