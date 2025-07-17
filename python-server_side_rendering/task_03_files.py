from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json():
    try:
        with open('products.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Erreur JSON : {e}")
        return []

def read_csv():
    try:
        with open('products.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return [row for row in reader]
    except Exception as e:
        print(f"Erreur CSV : {e}")
        return []

@app.route('/products')
def show_products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    error = None
    products = []

    if source == 'json':
        products = read_json()
    elif source == 'csv':
        products = read_csv()
    else:
        error = "Wrong source"

    # Si un id est fourni, on filtre
    if product_id and not error:
        try:
            product_id = str(product_id)
            products = [p for p in products if str(p.get("id") or p["id"]) == product_id]
            if not products:
                error = "Product not found"
        except Exception as e:
            error = "Error during filtering"

    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
