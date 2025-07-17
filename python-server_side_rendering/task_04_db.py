from flask import Flask, render_template, request
import json, csv, sqlite3

app = Flask(__name__)

def read_json():
    with open('products.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def read_csv():
    with open('products.csv', 'r', encoding='utf-8') as f:
        return [row for row in csv.DictReader(f)]

def read_sql():
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row  # permet un accès par clé
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Products")
        rows = cursor.fetchall()
        return [dict(row) for row in rows]
    except Exception as e:
        print(f"Erreur SQL : {e}")
        return []
    finally:
        conn.close()

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
    elif source == 'sql':
        products = read_sql()
    else:
        error = "Wrong source"

    # Si un id est fourni, on filtre
    if product_id and not error:
        product_id = str(product_id)
        products = [p for p in products if str(p.get("id")) == product_id]
        if not products:
            error = "Product not found"

    return render_template("product_display.html", products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
