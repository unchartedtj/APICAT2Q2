from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for products
products = []

# POST /products: Create a new product
@app.route('/products', methods=['POST'])
def add_product():
    try:
        data = request.get_json()
        
        # Validate input data
        if not data or 'name' not in data or 'description' not in data or 'price' not in data:
            return jsonify({"error": "Invalid input data. Please provide 'name', 'description', and 'price'."}), 400

        # Validate price
        try:
            price = float(data['price'])
        except ValueError:
            return jsonify({"error": "Invalid price value, it must be a number."}), 400

        product = {
            "name": data['name'],
            "description": data['description'],
            "price": price
        }
        products.append(product)
        return jsonify(product), 201  # Created
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# GET /products: Retrieve all products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products), 200  # OK

if __name__ == '__main__':
    app.run(debug=True)
