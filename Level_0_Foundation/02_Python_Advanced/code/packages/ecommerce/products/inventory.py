# ecommerce/products/inventory.py

def get_product_details(product_id):
    products = {
        101: {"name": "Laptop", "price": 1200},
        102: {"name": "Smartphone", "price": 800}
    }
    return products.get(product_id, "Product not found")
