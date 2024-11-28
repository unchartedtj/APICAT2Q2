# Product Management API

## Overview
This project is a simple REST API built using Flask to manage products. The API provides endpoints for adding new products and retrieving a list of all products. Each product includes the following fields: `name`, `description`, and `price`.

## Models
- **Product**
    - `name`: The name of the product (string).
    - `description`: A description of the product (string).
    - `price`: The price of the product (float).

## REST API Endpoints

### Products
- **POST /products**: Create a new product.
    - Request Body:
      ```json
      {
          "name": "Laptop",
          "description": "High-performance laptop",
          "price": 1500.0
      }
      ```
    - Response:
        - **201 Created**: Product created successfully.
        - **400 Bad Request**: Invalid input data.
        - **400 Bad Request (Invalid Price)**: Price must be a valid number.

- **GET /products**: Retrieve a list of all products.
    - Response:
        - **200 OK**: Returns a list of products in JSON format.

## Steps to Set Up the Environment and Run the API Server

1. **Clone the Repository**
   ```bash
   git clone https://github.com/unchartedtj/APICAT2Q2.git
   cd APICAT2Q2
"# APICAT2Q2" 
