import requests

BASE_URL = 'http://127.0.0.1:5000'

# Add a new product
def add_product(name, description, price):
    payload = {
        "name": name,
        "description": description,
        "price": price
    }
    try:
        response = requests.post(f"{BASE_URL}/products", json=payload)
        response.raise_for_status()  # Will raise an HTTPError for bad responses
        print(f"Add Product Response: {response.status_code}, {response.json()}")
    except requests.exceptions.RequestException as e:
        print(f"Error while adding product: {e}")

# Get all products
def get_products():
    try:
        response = requests.get(f"{BASE_URL}/products")
        response.raise_for_status()  # Will raise an HTTPError for bad responses
        print(f"Get Products Response: {response.status_code}, {response.json()}")
    except requests.exceptions.RequestException as e:
        print(f"Error while retrieving products: {e}")

if __name__ == "__main__":
    # Example Usage
    add_product("Laptop", "High-performance laptop", 1500.0)
    add_product("Phone", "Latest smartphone", 800.0)
    get_products()
